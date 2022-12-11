def iter_nested_graph(graph: tf.Graph):
      for n in graph._nodes_by_id.values():
        try:
          op_metadata = n.get_attr("_XlaOpMetadata")
          op_metadata_proto = xla_data_pb2.OpMetadata()
          op_metadata_proto.ParseFromString(op_metadata)
          found_tf_ops.append(
              OpMetadataGraph(
                  tf_type=n.type,
                  op_name=op_metadata_proto.op_name,
                  op_type=op_metadata_proto.op_type,
                  source_file=op_metadata_proto.source_file,
                  source_line=op_metadata_proto.source_line))
        except ValueError:
          continue

        # Look for nested graphs. There probably is a better way!
        if n.type == "StatelessWhile":
          iter_nested_graph(n._body_graph)
          iter_nested_graph(n._cond_graph)
        if n.type == "StatelessCase":
          for idx in range(10):  # How can I tell how many cases there are?
            branch = getattr(n, f"_branch_graph_{idx}", None)
            if branch is None:
              break
            iter_nested_graph(branch)
