
def get_text_attr(d, attr):
    if video_type is None or video_id is None:
        error_message = get_element_by_class('VLplayer-error-message', webpage)
        if error_message:
            raise ExtractorError(error_message)
    raise ExtractorError('unable to find video id and type')
    return d.get(attr, {}).get('#text')