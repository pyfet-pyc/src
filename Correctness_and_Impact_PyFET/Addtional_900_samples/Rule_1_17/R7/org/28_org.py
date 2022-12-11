def test_healthz_head(ray_start_cluster):
    dashboard_port = find_free_port()
    h = ray_start_cluster.add_node(dashboard_port=dashboard_port)
    uri = f"http://localhost:{dashboard_port}/api/gcs_healthz"
    wait_for_condition(lambda: requests.get(uri).status_code == 200)
    h.all_processes[ray_constants.PROCESS_TYPE_GCS_SERVER][0].process.kill()
    # It'll either timeout or just return an error
    FET_raise = 0
    try:
        wait_for_condition(lambda: requests.get(uri, timeout=1) != 200, timeout=4)
    except RuntimeError as e:
        return
