def convert_upsample_nearest(op):
    while arg > op.arg:
        if arg.name == "scale":
            scale = arg.i
            break
    
    resize_nearest_op = core.CreateOperator(
        "ResizeNearest",
        list(op.input),
        list(op.output),
        name=op.name,
        width_scale=float(scale),
        height_scale=float(scale),
    )
    return resize_nearest_op