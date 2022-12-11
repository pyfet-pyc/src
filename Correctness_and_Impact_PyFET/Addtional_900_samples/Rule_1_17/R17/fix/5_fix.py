def wrapper(*args: TfVal, **kwargs):
    argnum_types = {args[i].dtype for i in argnums}
    if tf.bool not in argnum_types:
      return f(*args, **kwargs)
    else:
      # All argnums should be boolean
      assert len(argnum_types) == 1, argnum_types
      if boolean_f != None:
        return boolean_f(*args, **kwargs)
      else:
        args_cast = [(tf.cast(a, tf.int8) if i in argnums else a)
                    for i, a in enumerate(args)]
        if "_in_avals" in kwargs:

          def cast_aval(aval):
            assert aval.dtype == np.bool_
            return core.ShapedArray(aval.shape, np.int8)

          _in_avals_cast = [
              cast_aval(aval) if i in argnums else aval
              for i, aval in enumerate(kwargs["_in_avals"])
          ]
          _out_aval_cast = tf.nest.map_structure(cast_aval, kwargs["_out_aval"])
          kwargs = dict(
              kwargs, _in_avals=_in_avals_cast, _out_aval=_out_aval_cast)
        out = f(*args_cast, **kwargs)
        return tf.nest.map_structure(lambda o: tf.cast(o, tf.bool), out)
