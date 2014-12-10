#!/usr/bin/env python3
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from curldrop import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(app.config['PORT'])
IOLoop.instance().start()