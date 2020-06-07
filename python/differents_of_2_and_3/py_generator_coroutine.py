# auth Bernard
# date 2020-04-17

"""
python的生成器 和 协程：
    生成器：generator
        生成器就是可以生成值的函数
        当一个函数有了yield 关键字 就成了生成器
        生成器可以挂起执行并且保持当前执行的状态

"""


# def simple_gen():
#     yield "hello"
#     yield "world"
#
#
# gen = simple_gen()
# try:
#     print(type(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except StopIteration as error:
#     print("get StopIteration")


"""
基于生成器的协程：
     python3之前没有原生的协程， 只有基于生成器的协程
        pep 342(Coroutines via Enhancd Generators)增强生成器功能
        生成器可以通过 yield 暂停执行和产出数据
        同时支持 send() 向生成器发送数据和throw()向生成器抛异常
"""

# def coro():
#     '''
#     python2 基于生成器的协程
#     '''
#     hello = yield "hello" # yield 关键字在= 右边作为表达式， 可以被send值
#     yield hello
#
# c = coro()
# print(type(c))
# print(next(c)) # 输出 hello ， 这里调用next 产出第一个值 'hello'，之后函数暂停
#
# print(c.send("world"))
# 再次调用 send 发送值， 此时hello 变量赋值为 'world' , 饭后yield 产出 hello
# 变量的值 'world'

# 之后协程结束， 后续在send值， 会抛出异常

"""
   协程的注意点：
        协程需要使用send() 或者 next(coroutine) 来【预激】（prime)才能启动
        在yield处协程会暂停
        单独的yield value 会传出值给调用方
        可以通过 coroutine.send(value)来给协程发送值， 发送的值会赋值给yield表达式左边的变量value=yield
        协程执行完成后（没有遇到下一个yield语句)会抛出 StopIteration异常
        
    协程装饰器：
        避免每次都要用send 预激它
        
总结：
    python2中：
        包含yield的函数， 可以产生协程
        
        流畅的python 中协程有讲解
"""

# from functions import wraps
#
# def coroutine(func):# 避免每次都用send预激它， 这样就不用每次都用send(None)启动了
#     """装饰器： 向前执行到第一个 yield表达式， 预激 func"""
#     @wraps(func)
#     def primer(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         next(gen)
#         return gen
#     return primer


"""
python3.5 原生协程：
    python3.5 引入 async/ await 支持原生协程（native corutine)
"""

import asyncio
import datetime
import random

async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()
