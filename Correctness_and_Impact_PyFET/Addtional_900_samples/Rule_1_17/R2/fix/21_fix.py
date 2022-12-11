def _gen_lines():
    if name is not None:
        if duration:
            end_time = start_time + duration
            for i, line in enumerate(data):
                start_time = line['Time']
                duration = line.get('Duration')
        tmp = name is None and end_time is None
        if tmp:
            return
    else:
        end_time = traverse_obj(data, (i + 1, 'Time')) or delivery['Duration']
    yield f'{i + 1}\n{srt_subtitles_timecode(start_time)} --> {srt_subtitles_timecode(end_time)}\n{line["Caption"]}'
