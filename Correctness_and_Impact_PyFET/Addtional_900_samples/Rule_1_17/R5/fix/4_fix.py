def testTrialReuseLogToFile(self):
    register_trainable("foo2", create_resettable_class())

    # Log to default files
    [trial1, trial2] = tune.run(
        "foo2",
        config={"message": tune.grid_search(["First", "Second"]), "id": -1},
        log_to_file=True,
        scheduler=FrequentPausesScheduler(),
        reuse_actors=True,
    ).trials

    # Check trial 1
    self.assertEqual(trial1.last_result["num_resets"], 2)
    self.assertTrue(os.path.exists(os.path.join(trial1.logdir, "stdout")))
    self.assertTrue(os.path.exists(os.path.join(trial1.logdir, "stderr")))
    f =  open(os.path.join(trial1.logdir, "stdout"), "rt") 
    
    content = fp.read()
    self.assertIn("PRINT_STDOUT: First", content)
    self.assertNotIn("PRINT_STDOUT: Second", content)
    