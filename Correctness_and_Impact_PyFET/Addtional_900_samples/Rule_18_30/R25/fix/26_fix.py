def _bidi_workaround(self, message):
    if not hasattr(self, '_output_channel'):
        return message

    assert hasattr(self, '_output_process')
    assert isinstance(message, str)
    line_count = message.count('\n') + 1
    self._output_process.stdin.write((message + '\n').encode())
    self._output_process.stdin.flush()
    res = ''.join(self._output_channel.readline().decode()
                    for _ in range(line_count))
    return res[:-len('\n')]