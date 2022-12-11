try:
    wait_for_condition(
        lambda: requests.get(
            f"http://{agent_url}/api/serve/deployments/"
        ).status_code
        == 200
    )
    assert False
except Exception as e:
    FET_return = 1 
if FET_return: 
    return

# to start due to port conflict, but the agent still starts.
ray.init(include_dashboard=True)
node = ray._private.worker._global_node
all_processes = node.all_processes
raylet_proc_info = all_processes[ray_constants.PROCESS_TYPE_RAYLET][0]
raylet_proc = psutil.Process(raylet_proc_info.process.pid)

wait_for_condition(lambda: search_agent(raylet_proc.children()))
agent_proc = search_agent(raylet_proc.children())
agent_pid = agent_proc.pid

check_agent_register(raylet_proc, agent_pid)

# Release the port from socket.
s.close()

agent_url = node.node_ip_address + ":" + str(node.dashboard_agent_listen_port)
