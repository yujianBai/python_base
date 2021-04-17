# auth Bernard
# date 2021-04-17
import threading
from concurrent.futures import ThreadPoolExecutor


def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


pool = ThreadPoolExecutor(max_workers=5)
future1 = pool.submit(action, 10)
future2 = pool.submit(action, 20)
future3 = pool.submit(action, 30)

print(future1.done())
print(future2.done())
print(future3.done())

pool.shutdown()
