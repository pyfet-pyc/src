def stream_and_remove_file():
    yield from file_handle
    file_handle.close()
    tmp_dir.cleanup()

    return current_app.response_class(
        stream_and_remove_file(),
        headers={"Content-Disposition": "attachment", "filename": basename},
    )

