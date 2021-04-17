# auth Bernard
# date 2021-04-17

from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED

from ProcessPoolExecutor.task import add

pool = ThreadPoolExecutor(max_workers=5)

# 单个提交
# t1 = pool.submit(add, 1, 2, 1)
# t2 = pool.submit(add, 2, 3, 8)
# t3 = pool.submit(add, 3, 4, 3)
# t4 = pool.submit(add, 4, 5, 4)
#
# print("task's status is t1:{}, t2:{}, t3:{}, t4:{} ".format(t1.done(), t2.done(), t3.done(), t4.done()))
#
# print("t1's result is:{}".format(t1.result()))
# print("t2's result is:{}".format(t2.result()))
# print("t3's result is:{}".format(t3.result()))
# print("t4's result is:{}".format(t4.result()))


# 批量提交
params = [
    [2, 3, 1],
    [1, 2, 10],
    [3, 4, 2],
]
#
# Ts = [pool.submit(add, *(param)) for param in params]
#
# for t in as_completed(Ts):
#     print(t.result())


all_task = [pool.submit(add, *(param)) for param in params]
wait(all_task, return_when=ALL_COMPLETED)  # 所有的线程执行完后才返回
# wait(all_task, return_when=FIRST_COMPLETED)  # 提交在前的， 且耗时较短的先返回结果

for task in all_task:
    print(task.result())

print('done')