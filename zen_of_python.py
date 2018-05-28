# -*- coding: utf-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import requests

class TodoHandler(BaseHTTPRequestHandler):
    """A simple TODO server

    which can display and manage todos for you.
    """

    # Global instance to store todos. You should use a database in reality.

    def do_GET(self):
        # return all todos

        if self.path != '/':
            self.send_error(404, "File not found.")
            return


        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        res = requests.get('http://wiki.python.org.tw/The Zen Of Python')
        print(res.text)
        self.wfile.write("test")

if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()