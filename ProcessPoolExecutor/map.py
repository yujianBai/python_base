#auth Bernard
#date 2021-04-17

from concurrent.futures import ThreadPoolExecutor

from ProcessPoolExecutor.task import add


params = [
    [1, 2, 5],
    [2, 3, 1],
    [3, 4, 2]
]

pool = ThreadPoolExecutor(max_workers=5)
rets = pool.map(add, *params)

for ret in rets:
    print(ret)


