def __init__(
    self,
    cluster_manager: ClusterManager,
    session_controller: Optional["SessionController"] = None,
):
    from anyscale.controllers.session_controller import SessionController

    super(SessionControllerFileManager, self).__init__(cluster_manager)
    self.session_controller = session_controller or SessionController()

    # Write legacy anyscale project yaml
    with open(os.path.join(os.getcwd(), ".anyscale.yaml"), "wt") as f:
        f.write(f"project_id: {self.cluster_manager.project_id}")
