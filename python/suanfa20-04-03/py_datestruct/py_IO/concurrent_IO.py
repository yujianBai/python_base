#auth Bernard
#date 2020-04-20

"""
五中IO模型：

Unix网络编程中提到了5中网络编程模型
    Blocking IO

    Nonblocking IO

    IO multiplexing

    这两种不常用, 一般使用IO多路复用比较多
        Singnal Driven IO
        Asynchronous IO

"""

"""
如何提升并发能力：
    一些常见的提升并发能力的方式：
        多线程模型， 创建新的线程处理请求
        多进程模型， 创建新的进程处理请求
"""

"""
什么是IO多路复用？
    操作系统提供的同时监听多个socket的机制
        为了实现高并发需要一种机制处理多个socket
        Linux 常见的是 select /pool/ epoll
        可以使用单线程 单进程 处理多个socket
"""


"""
python如何实现io 多路复用
    pyhton的io多路复用基于操作系统 实现（select /pool/epool)
    python2 select模块
    python3 selectors模块
    
事件类型： EVENT_READ, EVENT_WRITE
DefaultSelector: 自动根据平台选取合适的IO模型
    register()
    unregister()
    modify()
    select()
    close()
"""

if __name__ == "__main__":
    pass