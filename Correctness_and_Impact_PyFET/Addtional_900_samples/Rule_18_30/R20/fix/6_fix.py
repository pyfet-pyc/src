def _check_mesh_resource_axis(mesh, parsed_pspec):
  try:
    [mesh.shape[r] for p in parsed_pspec if p is not None
     for r in p]
  except KeyError as e:
    raise ValueError(f"Resource axis: {e.args[0]} of {parsed_pspec.user_spec} is "
                     "undefined.") from None
