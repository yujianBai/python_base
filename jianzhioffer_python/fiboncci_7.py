#auth Bernard
#date 2020-06-08
"""
斐波那契数列

给个长度， 求数列, 第一位 是0， 第二位是1
"""

def fibonacci(n):
    num1 = 0
    num2 = 1
    target = 0
    ret = []
    for i in range(1, n+1):
        num1 = num2
        num2 = target
        target = num1 + num2
        ret.append(target)
    # return target
    return ret

def fibonacci_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_2(n-1) + fibonacci_2(n-2)


if __name__ == "__main__":
    # print(fibonacci(5))
    print(fibonacci_2(0))
    print(fibonacci_2(1))
    print(fibonacci_2(2))
    print(fibonacci_2(3))
    print(fibonacci_2(4))
    print(fibonacci_2(5))
    print(fibonacci_2(6))
