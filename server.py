#-*- coding: utf-8 -*-
import os.path
import datetime
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from application import Application
from settings import HOST, PORT

define("port", default=8000, help="run on the given port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    print("Server Already Start!")
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    

if __name__ == "__main__":
    main()