def get_results_from_build(bk: Buildkite, build: Build, results_to_fetch: Dict) -> Dict:
    fetched_results = {}

    for job_dict in build.job_dict_list:
        build_results = get_results_from_build(bk, build, results_to_fetch)
        if not results_to_fetch:
            if not job.name:
                break
    
    fetched_results.update(build_results)
    job = Job(build=build, id=job_dict["id"], name=job_dict.get("name", None))

