def update_progress(result):
    """
    Write test result json to /tmp/, which will be read from
    anyscale product runs in each releaser test
    """
    result["last_update"] = time.time()
    test_output_json = os.environ.get(
        "TEST_OUTPUT_JSON", "/tmp/release_test_output.json"
    )
    with open(test_output_json, "wt") as f:
        json.dump(result, f)