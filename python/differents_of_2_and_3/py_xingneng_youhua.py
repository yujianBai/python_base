# auth Bernard
# date 2020-04-17
"""
python性能分析和优化， GIL常考题

什么是GIL, Golbal Interpreter Lock
    Cpython 解释器的内存管理并不是线程安全的
    保护多线程情况下对python对象的访问
    Cpython使用简单的锁机制避免多个线程同时执行字节码

    这个锁机制， 保护多线程访问资源，但是对于cpu密集的程序，也无法使用多核计算

GIL的影响：
    限制了程序的多核执行
        同一个时间只能有一个线程执行字节码
        CPU密集程序难以利用多核优势
        IO期间会释放GIL, 对IO密集程序影响不大 (因为IO密集程序本来就有个IO等待时间)

如何规避GIL影响：
    CPU密集 可以使用多进程 + 进程池 (还可以使用cython扩展)
    IO密集使用多线程 / 协程


GIL的实现：
   ?
"""

if __name__ == "__main__":
    # import threading
    #
    # n = [0]
    #
    #
    # def foo():
    #     n[0] += 1
    #     n[0] += 1
    #
    #
    # threads = []
    # for i in range(5000):
    #     t = threading.Thread(target=foo)
    #     threads.append(t)
    #
    # for t in threads:
    #     t.start()
    #
    # print(n)
    """
    这里的n的结果 大多数情况是 1000 ， 也有极个别是小于1000， 说明不是线程安全的
    
    这里为什么不是线程安全的， 在python中什么才是  原子操作 ？ 
    """

    """
    为什么有了GIL还有关注线程安全？
        python中什么操作才是原子的？ 一步到位执行完
            一个操作如果是一个字节码指令可以完成就是原子的
            原子的是可以保证线程安全的
            使用dis操作来分析字节码
            
    分析 原子操作 dis
    import dis
    
    def update_list(l):
        l[0] = 1
        
    dis.dis(update_list)
    
    """

    # import dis
    #
    #
    # def update_list(l):
    #     l[0] = 1  # 原子操作
    #
    #
    # dis.dis(update_list)
    #
    #
    # def incr_list(l):
    #     l[0] += 1 # 非线程安全的
    #
    #
    # dis.dis(incr_list)

    """
    解决线程安全 加锁 ！！！
    """
    import threading
    lock = threading.Lock()

    n = [0]

    def foo2():
        n[0] += 1
        n[0] += 1

    def foo():
        with lock:
            n[0] += 1
            n[0] += 1
            n[0] += 1

    def foo1():
        lock.acquire()
        n[0] += 1
        n[0] += 1
        n[0] += 1
        lock.release()


    threads = []
    for i in range(5000):
        t = threading.Thread(target=foo2)
        threads.append(t)

    for t in threads:
        t.start()

    print(n)


    """
    剖析程序性能
        使用各种 profile工具 （内置， 或第三方）
            二八定律， 大部分时间消耗在少量代码上
            内置的 profile/ cprofile等工具
            使用  pyflame (uber开源）的火焰图工具
            
    服务端性能优化措施:
        1， 数据结构和算法优化
        2， 数据库层：索引优化， 慢查询消除， 批量操作减少IO, NoSQL
        3， 网络IO: 批量操作， pipeline 操作， 减少IO
        4， 缓存：使用内存数据库 redis/ memcached
        5， 异步：asyncio , celery
        6， 并发： gevent/ 多线程
    """
