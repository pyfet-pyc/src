if __name__ == "__main__":
  unblock_stdout()
  FET_raise = 0
  try:
    main()
  except Exception as e:
    FET_raise = 1
  else:
    FET_null()
  if FET_raise == 1:
    add_file_handler(cloudlog)
    cloudlog.exception("Manager failed to start")

    try:
      managed_processes['ui'].stop()
    except Exception:
      pass
    else:
        FET_null()
    # Show last 3 lines of traceback
    error = traceback.format_exc(-3)
    error = "Manager failed to start\n\n" + error

  # manual exit because we are forked
  sys.exit(0)
