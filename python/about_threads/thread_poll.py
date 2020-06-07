# auth Bernard
# date 2020-03-16

import threadpool
import time


def sayhello(a):
    print("hello: " + a)
    time.sleep(2)


def main():
    # global result
    seed = ["a", "b", "c"]
    start = time.time()
    task_pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(sayhello, seed)

    # 并发调用
    for req in requests:
        task_pool.putRequest(req)
    task_pool.wait()

    end = time.time()
    time_m = end - start
    print("time: " + str(time_m))

    #以下测试不是并发， 依次调用sayhello()
    start1 = time.time()
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))


if __name__ == '__main__':
    main()
