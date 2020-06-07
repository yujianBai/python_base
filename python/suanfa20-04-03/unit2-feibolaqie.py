# auth Bernard
# date 2020-04-03

'''
斐波拉切数列，又称黄金分割数列，因数学家以兔子繁殖例子引入也称兔子数列

指的是这样一个数列1， 1， 2， 3， 5， 8， 13， 21， 34， ...后边的数等于前两个之和


递归要素：
1， 什么地方递归调用本身
2， 什么时候递归终止
'''


def feibolaqie_1(len):
    list_fib = []
    for i in range(len):
        if i < len:
            if i > 1:
                list_fib.append(list_fib[-1] + list_fib[-2])
            else:
                list_fib.append(1)

    return list_fib


def feibolaqie_digui(n):
    # if n == 1 or n == 2:
    if n in [1, 2]:
        return 1
    else:
        return feibolaqie_digui(n - 1) + feibolaqie_digui(n - 2)


def test():
    # print(feibolaqie_1(1))
    assert feibolaqie_1(1) == [1]
    assert feibolaqie_1(2) == [1, 1]
    assert feibolaqie_1(3) == [1, 1, 2]
    assert feibolaqie_1(4) == [1, 1, 2, 3]


def test_digui():
    assert feibolaqie_digui(1) == 1
    assert feibolaqie_digui(2) == 1
    assert feibolaqie_digui(3) == 2
    # assert feibolaqie_digui(5) == 5


class TestClass(object):
    def test_zne(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'hello')

    def test_a(self):
        assert 2 == 1


def fib_test2(k):
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1
    k_1 = 1
    k_2 = 1
    for i in range(3, k + 1):
        tmp = k_1
        i_value = k_1 + k_2
        k_1 = i_value
        k_2 = tmp
    return k_1


if __name__ == "__main__":
    '''
    用pytest测试这个 TestClass类的时候需要加参数
    pytset -k "test and TestClass and not test_a" filename.py
    
    kite for pycharm idb插件 函数提示
    '''
    from datetime import datetime
    start_time = datetime.now()
    print(fib_test2(36))
    print("递归耗时：{}".format((datetime.now()-start_time).total_seconds()))
