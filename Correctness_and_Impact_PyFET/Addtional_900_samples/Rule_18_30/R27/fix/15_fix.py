def main():
    # Fabric library controlled through global env parameters
    fab_config = Config(overrides={
        "connect_kwargs": {
            "key_filename": [KEYFILE], # https://github.com/fabric/fabric/issues/2007
        },
        "run": {
            "echo": True,
            "pty": True,
        },
        "timeouts": {
            "connect": 10,
        },
    })
    # no network connection, so don't worry about closing this one.
    local_cxn = Connection('localhost', config=fab_config)

    # Set up local copy of git repo
    #-------------------------------------------------------------------------------
    log_dir = tempfile.mkdtemp()  # points to logging / working directory
    print("Local dir for test repo and logs: %s"%log_dir)

    try:
        # figure out what git object to test and locally create it in log_dir
        print("Making local git repo")
        if cl_args.pull_request != '~':
            print('Testing PR %s ' % cl_args.pull_request,
                  "MERGING into master" if cl_args.merge_master else "")
            local_git_PR(local_cxn, cl_args.repo, cl_args.pull_request, log_dir,
                         cl_args.merge_master)
        elif cl_args.branch != '~':
            print('Testing branch %s of %s' % (cl_args.branch, cl_args.repo))
            local_git_branch(local_cxn, cl_args.repo, cl_args.branch, log_dir)
        else:
            print('Testing current branch of %s' % cl_args.repo, log_dir)
            local_git_clone(local_cxn, cl_args.repo, log_dir)
    except BaseException:
        print("FAIL: trouble with git repo")
        traceback.print_exc()
        exit(1)


    # Set up EC2 instances
    #-------------------------------------------------------------------------------
    configdata = yaml.safe_load(open(cl_args.config_file, 'r'))
    targetlist = configdata['targets']
    print('Testing against these images: [%d total]'%len(targetlist))
    for target in targetlist:
        print(target['ami'], target['name'])

    print("Connecting to EC2 using\n profile %s\n keyname %s\n keyfile %s"%(PROFILE, KEYNAME, KEYFILE))
    aws_session = boto3.session.Session(profile_name=PROFILE)
    ec2_client = aws_session.resource('ec2')

    print("Determining Subnet")
    for subnet in ec2_client.subnets.all():
        if should_use_subnet(subnet):
            subnet_id = subnet.id
            vpc_id = subnet.vpc.id
            break
    else:
        print("No usable subnet exists!")
        print("Please create a VPC with a subnet named {0}".format(SUBNET_NAME))
        print("that maps public IPv4 addresses to instances launched in the subnet.")
        sys.exit(1)

    print("Making Security Group")
    vpc = ec2_client.Vpc(vpc_id)
    sg_exists = False
    for sg in vpc.security_groups.all():
        if sg.group_name == SECURITY_GROUP_NAME:
            security_group_id = sg.id
            sg_exists = True
            print("  %s already exists"%SECURITY_GROUP_NAME)
    if not sg_exists:
        security_group_id = make_security_group(vpc).id
        time.sleep(30)

    instances = []
    try:
        print("Creating instances: ", end="")
        # If we want to preserve instances, do not have them self-destruct.
        self_destruct = not cl_args.saveinstances
        for target in targetlist:
            instances.append(
                create_client_instance(ec2_client, target,
                                       security_group_id, subnet_id,
                                       self_destruct)
            )
        print()

        # Install and launch client scripts in parallel
        #-------------------------------------------------------------------------------
        print("Uploading and running test script in parallel: %s"%cl_args.test_script)
        print("Output routed to log files in %s"%log_dir)
        # (Advice: always use Manager.Queue, never regular multiprocessing.Queue
        # the latter has implementation flaws that deadlock it in some circumstances)
        manager = Manager()
        outqueue = manager.Queue()
        inqueue = manager.Queue()

        # launch as many processes as clients to test
        num_processes = len(targetlist)
        jobs = [] #keep a reference to current procs


        # initiate process execution
        client_process_args=(fab_config, inqueue, outqueue, log_dir)
        for i in range(num_processes):
            p = mp.Process(target=test_client_process, args=client_process_args)
            jobs.append(p)
            p.daemon = True  # kills subprocesses if parent is killed
            p.start()

        # fill up work queue
        for ii, target in enumerate(targetlist):
            inqueue.put((ii, instances[ii].id, target))

        # add SENTINELs to end client processes
        for i in range(num_processes):
            inqueue.put(SENTINEL)
        print('Waiting on client processes', end='')
        for p in jobs:
            while p.is_alive():
                p.join(5 * 60)
                # Regularly print output to keep Travis happy
                print('.', end='')
                sys.stdout.flush()
        print()
        # add SENTINEL to output queue
        outqueue.put(SENTINEL)

        # clean up
        local_repo_clean(local_cxn, log_dir)

        # print and save summary results
        results_file = open(log_dir+'/results', 'w')
        outputs = list(iter(outqueue.get, SENTINEL))
        outputs.sort(key=lambda x: x[0])
        failed = False
        results_msg = ""
        for outq in outputs:
            ii, target, status = outq
            if status == Status.FAIL:
                failed = True
                with open(log_dir+'/'+'%d_%s.log'%(ii,target['name']), 'r') as f:
                    print(target['name'] + " test failed. Test log:")
                    print(f.read())
            results_msg = results_msg + '%d %s %s\n'%(ii, target['name'], status)
            results_file.write('%d %s %s\n'%(ii, target['name'], status))
        print(results_msg)
        if len(outputs) != num_processes:
            failed = True
            failure_message = 'FAILURE: Some target machines failed to run and were not tested. ' +\
                'Tests should be rerun.'
            print(failure_message)
            results_file.write(failure_message + '\n')
        results_file.close()

        if failed:
            sys.exit(1)

    finally:
        cleanup(cl_args, instances, targetlist, log_dir)
