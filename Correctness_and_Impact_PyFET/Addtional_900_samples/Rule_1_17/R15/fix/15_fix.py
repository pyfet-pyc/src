def _build_key_scoped_ray_remote_args(dsk, annotations, ray_remote_args):
    # Handle per-layer annotations.
    if not isinstance(dsk, dask.highlevelgraph.HighLevelGraph):
        dsk = dask.highlevelgraph.HighLevelGraph.from_collections(
            id(dsk), dsk, dependencies=()
        )
    # Build key-scoped annotations.
    scoped_annotations  = {}
    layers  = [(name, dsk.layers[name]) for name in dsk._toposort_layers()]
    layers = dict(layers)