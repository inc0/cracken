from io import StringIO

from http.server import HTTPServer, SimpleHTTPRequestHandler


class CrackenHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        out = StringIO("foo")
        self.send_response(200)
        self.wfile.write(out)
        return


httpd = HTTPServer(('127.0.0.1', 8080), CrackenHandler)
httpd.serve_forever()