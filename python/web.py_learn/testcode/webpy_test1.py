#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: webpy_test1.py.py
@time: 2019/2/13 10:32
"""

import web

urls = (
    '/index', 'index',
    '/(.*)', 'hello', #带组匹配， 这么写每次匹配到的都是hello这个处理函数
)
app = web.application(urls, globals())

class index:
    def GET(self):
        return "in index"


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run()