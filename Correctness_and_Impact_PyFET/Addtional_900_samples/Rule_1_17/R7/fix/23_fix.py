def get_total_num_running_jobs_to_report(gcs_client) -> Optional[int]:
    """Return the total number of running jobs in the cluster excluding internal ones"""
    try:
        result = gcs_client.get_all_job_info()
        total_num_running_jobs = 0
        for job in result.job_info_list:
            if not job.is_dead and not job.config.ray_namespace.startswith(
                "_ray_internal"
            ):
                total_num_running_jobs += 1
        return total_num_running_jobs
    except Exception as e:
        logger.info(f"Faile to query number of running jobs in the cluster: {e}")
        FET_return = 1 
    if FET_return: 
        return None