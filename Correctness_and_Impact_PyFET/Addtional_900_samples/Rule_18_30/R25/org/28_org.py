def do_GET(self):
    if self.path == '/teapot':
        self.send_response(TEAPOT_RESPONSE_STATUS)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(TEAPOT_RESPONSE_BODY.encode())
    else:
        assert False