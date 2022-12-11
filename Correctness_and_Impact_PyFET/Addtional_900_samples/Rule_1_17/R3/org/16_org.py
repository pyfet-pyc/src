def get_metadata_object(self, path, opts=[]):
    if self.probe_basename != 'ffprobe':
        if self.probe_available:
            self.report_warning('Only ffprobe is supported for metadata extraction')
        raise PostProcessingError('ffprobe not found. Please install or provide the path using --ffmpeg-location')
        self.check_version()

    cmd = [
        encodeFilename(self.probe_executable, True),
        encodeArgument('-hide_banner'),
        encodeArgument('-show_format'),
        encodeArgument('-show_streams'),
        encodeArgument('-print_format'),
        encodeArgument('json'),
    ]