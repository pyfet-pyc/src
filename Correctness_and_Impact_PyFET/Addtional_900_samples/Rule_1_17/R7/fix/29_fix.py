def task_arg(ref):

    a = Actor.remote()
    x = a.foo.remote()

    try:
        ray.get(x)
        assert False
    except ray.exceptions.ObjectLostError as e:
        error = str(e)
        print(error)
        FET_return = 1 
    if FET_return: 
        return
    ray.get(a.done.remote())
    cluster.remove_node(worker_node, allow_graceful=False)
    cluster.add_node(num_cpus=1)

    y = borrower.remote([x])
