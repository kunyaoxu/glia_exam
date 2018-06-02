# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi
import json
import requests

import urllib2
from bs4 import BeautifulSoup
import random

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # return all todos

        if self.path != '/':
            self.send_error(404, "File not found.")
            return


        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        page = requests.get('http://wiki.python.org.tw/The%20Zen%20Of%20Python').text
#        print(page.encode(encoding="utf-8", errors="strict"))
#        quote_page = 'http://wiki.python.org.tw/The%20Zen%20Of%20Python'
#        page = urllib2.urlopen(quote_page)
        soup = BeautifulSoup(page, 'lxml')
#        name_box = soup.find('p', 'line874')
        name_box = soup.find_all('p', 'line874')
#        print(soup.original_encoding)
        print len(name_box)
        index = random.randrange(0, len(name_box))
        self.wfile.write(name_box[index].text.encode(encoding="utf-8", errors="strict"))
#        for p in name_box:
#            print p.get('class'), p.text
#            self.wfile.write(p.text.encode(encoding="utf-8", errors="strict"))
##        self.wfile.write(name_box)
#        print name_box
#        name_box = " ".join(x.text.encode('utf-8') for x in name_box)
#        self.wfile.write(name_box)


if __name__ == '__main__':
    # Start a simple server, and loop forever
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8000), TodoHandler)
    print("Starting server, use <Ctrl-C> to stop")
    server.serve_forever()
