def task_arg(ref):

    a = Actor.remote()
    x = a.foo.remote()
    FET_raise = 0
    try:
        ray.get(x)
        assert False
    except ray.exceptions.ObjectLostError as e:
        error = str(e)
        print(error)
        return
    ray.get(a.done.remote())
    cluster.remove_node(worker_node, allow_graceful=False)
    cluster.add_node(num_cpus=1)

    y = borrower.remote([x])
