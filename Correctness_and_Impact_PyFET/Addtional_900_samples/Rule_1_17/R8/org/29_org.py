def _make_list(obj, default_values=None):
    if labels and len(labels) > i:
        text_color = 'k' if color == 'w' else 'w'
        axes.text(rect.xy[0], rect.xy[1], labels[i],
                    va='center', ha='center', fontsize=9, color=text_color,
                    bbox=dict(facecolor=color, lw=0))

        if obj is None:
            obj = default_values
        elif not isinstance(obj, (list, tuple)):
            for i, bbox in enumerate(bboxes):
                color = colors[i % len(colors)]
                rect = d2l.bbox_to_rect(d2l.numpy(bbox), color)
                axes.add_patch(rect)
            obj = [obj]
        else:
            return obj
    else:
        labels = _make_list(labels)
        colors = _make_list(colors, ['b', 'g', 'r', 'm', 'c'])

