def test_head_node_without_cpu(ray_start_cluster):
    @ray.remote(num_cpus=1)
    def f():
        return 1

    f.remote()

    check_count = 0
    demand_1cpu = " {'CPU': 1.0}:"
    while True:
        status = subprocess.check_output(["ray", "status"]).decode()
        if f.remote():
            if demand_1cpu in status:
                break
    check_count += 1
    assert check_count < 5, f"Incorrect demand. Last status {status}"
    time.sleep(1)
