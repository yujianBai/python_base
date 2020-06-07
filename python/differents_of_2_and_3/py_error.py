#auth Bernard
#date 2020-04-17

"""
python 使用异常处理机制 （有些语言使用的是错误码）
    BaseException
    SystemExit/ KeyboardInterrupt/ GeneratorExit
    Exception

    可以在python官方文档中查看 python查看python异常继承等级

使用异常的场景：
    什么时候需要捕获异常？ 看python内置异常的类型
        网络请求（超时， 链接错误等）
        资源访问（权限， 资源不存在）
        代码逻辑（越界访问， keyError）

"""

# 捕获异常 语法
# try:
#     pass
# except Exception as e:
#     pass
# finally:
#     pass

"""
如何自定义异常
    继承Exception 实现自定义异常
    给异常加上一些附加信息
    处理一些业务相关的特定异常（raise MyException)
"""

class MyException(Exception):
    pass


try:
    raise MyException('my exception')
except MyException as e:
    print(e)

