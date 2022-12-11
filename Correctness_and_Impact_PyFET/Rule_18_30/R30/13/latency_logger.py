def graph_timestamps(timestamps, start_times, end_times, relative, offset_services=False, title=""):
  # mpld3 doesn't convert properly to D3 font sizes
  plt.rcParams.update({'font.size': 18})

  t0 = find_t0(start_times)
  fig, ax = plt.subplots()
  ax.set_xlim(0, 130 if relative else 750)
  ax.set_ylim(0, 17)
  ax.set_xlabel('Time (milliseconds)')
  colors = ['blue', 'green', 'red', 'yellow', 'purple']
  offsets = [[0, -5*j] for j in range(len(SERVICES))] if offset_services else None
  height = 0.3 if offset_services else 0.9
  assert len(colors) == len(SERVICES), 'Each service needs a color'
  return
