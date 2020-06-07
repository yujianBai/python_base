# auth Bernard
# date 2020-04-06
total = dict()
def fib(k):
    assert k > 0
    if k in [1, 2]:
        return 1
    global total
    if k in total:
        result = total[k]
    else:
        result = fib(k - 1) + fib(k - 2)
        total[k] = result
    return result

# def fib2(k):
#     assert k > 0
#     if k in [1, 2]:
#         return 1
#     else:
#         return fib(k - 1) + fib(k - 2)


if __name__ == "__main__":
    # 搜索 + 记忆算法

    from datetime import datetime
    start_time = datetime.now()
    print(fib(200))
    print("def fib 计算耗时：{}".format(
        (datetime.now()-start_time).total_seconds()))

    # start_time = datetime.now()
    # print(fib2(200))
    # print("def fib2 计算耗时：{}".format(
    #     (datetime.now()-start_time).total_seconds()))

    # 1e-05   <==> 0.00001
