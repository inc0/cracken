import sys

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import request


dest_url = sys.argv[1]


class CrackenHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        resp = request.urlopen(dest_url + self.path)
        self.send_response(200)
        self.wfile.write(bytes(resp.read().decode('UTF-8'), "UTF-8"))
        return


httpd = HTTPServer(('127.0.0.1', 8080), CrackenHandler)
httpd.serve_forever()