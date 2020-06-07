# auth Bernard
# date 2020-04-20
"""

哪些并发网络库：
    Tornado vs Gevent vs Asyncio
        Tornado 并发网络库和同时也是一个web微框架
        Gevnet 绿色线程（greenlet)实现并发， 猴子不定修改内置socket
        Asyncio Python3内置并发网络库， 基于原生协程
"""

"""
Tornado 框架
    适用于微服务， 实现Restful接口
    底层基于linux多路复用
    可以通过协程或者回调实现异步编程
    不过生态不完善， 相应的异步框架比如ORM不完善
"""

import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class APIHandler(tornado.web.RequestHandler):
    async def get(self):
        url = "http://httpbin.org/get"
        http_client = AsyncHTTPClient()
        resp = await
        http_client.fetch(url)
        print(resp.body)
        return resp.body


def make_app():
    return tornado.web.Application([
        (r"/api", APIHandler),
    ])




if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
