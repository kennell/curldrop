#!/usr/bin/env python3
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from os.path import isfile, isdir
from os import makedirs
from curldrop import app, init_db

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(app.config['PORT'])

if not isfile(app.config['DATABASE']):
		init_db()

if not isdir(app.config['UPLOADDIR']):
		makedirs(app.config['UPLOADDIR'])

IOLoop.instance().start()