def main(logfile, outfile):
  logging.info("Parsing %s", logfile)
  try:
    with open(logfile, 'r') as f:
      reports = (parse_line(line) for line in f)
      failures = (r for r in reports if r.outcome == "failed")
      summary = "\n".join(f"{f.nodeid}: {f.longrepr.chain[0][1].message}"
                          for f in failures)
    logging.info("Parsed summary:\n%s", summary)
  except Exception:
    err_info = traceback.format_exc()
    logging.info("Parsing failed:\n%s", err_info)
    summary = f"Log parsing failed; traceback:\n\n{err_info}"
  logging.info("Writing result to %s", outfile)
  with open(outfile, 'w') as f:
    f.write(MSG_FORMAT.format(summary=summary))
