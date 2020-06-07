#auth Bernard
#date 2020-04-20

""" Gevent
高性能并发网络库：
    基于轻量级绿色线程（greenlet)实现并发
    需要注意mokney patch , gevent 修改了内置的socket改为非阻塞
    配合gunicorn和 gevent 部署作为wsgi server
"""

import gevent.monkey
gevent.monkey.patch_all() # 修改内置的一些库非阻塞

import gevent
import request

def fetch(i):
    usr = 'http://httpbin.org/get'
    resp = requests.get(url)
    print(len(resp.text), i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print("Asynchronous")
asynchronous()
