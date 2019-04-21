# -*- coding: utf-8 -*-
# @Time    : 19-4-21 下午10:25
# @Author  : Baiyj

# @File    : flask_wsgi

from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    data = ''
    data = request.args.to_dict()
    import time
    time.sleep(10)
    return "hello world :%s"%data

app.run(host = '0.0.0.0', port = 10080)