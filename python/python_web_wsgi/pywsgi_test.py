# -*- coding: utf-8 -*-
# @Time    : 19-4-21 下午10:56
# @Author  : Baiyj

# @File    : pywsgi_test


from gevent import monkey

monkey.patch_all()
from flask import Flask
from gevent import pywsgi

app = Flask(__name__)


@app.route('/')
def index():
    import time
    time.sleep(10)
    return 'Hello World'


server = pywsgi.WSGIServer(('localhost', 10080), app)
server.serve_forever()