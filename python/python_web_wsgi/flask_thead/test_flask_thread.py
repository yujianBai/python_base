# -*- coding: utf-8 -*-
# @Time    : 19-4-26 下午10:55
# @Author  : Baiyj

# @File    : test_flask_thread

from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count, Process
# from bottle import Bottle
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def index():
    print request.path
    return "hello world"

server = WSGIServer(('', 11080), app, log=None)
server.start()

def serve_forever():
    server.start_accepting()
    server._stop_event.wait()

if __name__ == "__main__":
    # server.serve_forever()
    # 启动的进程数为cpu个数
    for i in range(cpu_count()):
        p = Process(target=serve_forever)
        p.start()