#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: webpy_test1.py.py
@time: 2019/2/13 10:32
"""

import web

render = web.template.render("templates") #这里是web模板的目录
urls = (
    '/index', 'index',
    "/head", "test_request_head",
    '/(.*)', 'hello', #带组匹配， 这么写每次匹配到的都是hello这个处理函数
)
app = web.application(urls, globals())

class index:
    def GET(self):
        return web.seeother("/head")

    def POST(self):
        query = web.input()
        query["method"] = "POST"
        return query


class hello:
    def GET(self, name):
        return render.hello2(name) #rander + . + html的文件的名字

class test_request_head:
    def GET(self):
        return "see other"

if __name__ == "__main__":
    app.run()