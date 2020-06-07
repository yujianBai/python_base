# auth Bernard
# date 2020-05-12

a = [[1], [2, 3, 4], [5, 6], [7, 8, 9]]


def test1():
    tmp = []
    for tmp_list in a:
        for item in tmp_list:
            tmp.append(item)

    print(tmp)


def test1_1():
    print([i for j in a for i in j])


def test1_2():
    from itertools import chain
    print(list(chain.from_iterable(a)))
    print(a)


def test2():
    n = (i for i in range(9))
    print(9 in n)
    print(1 in n)
    # TODO
    """ 
    n 得到的是一个迭代器 9， 1都不在 n 里 
    n 是一个 generator
    """


def test3():
    for item in range(1, 101):
        if item % 3 == 0:
            print("Fizz")
        elif item % 5 == 0:
            print("Buzz")
        elif item % 5 == 0 and item % 3 == 0:
            print("FizzBuzz")
        else:
            print(item)


def runupstairs1(n):  # 每一步都是前两步和前一步的和
    pre, cur = 1, 1
    for i in range(1, n):
        pre, cur = cur, pre + cur
    return cur


def runupstairs2(n):  # 用列表记录每个n对应的值，最后的n取最后一个值即可
    if n < 1:
        raise "n should large than 1"
    if n == 1:
        return 1
    if n == 2:
        return 2
    res = [1, 2]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res[-1]


import queue


class NumQueue():
    def __init__(self):
        self.queue = queue.Queue(10)

    def length(self):
        return self.queue.qsize()

    def put(self, x):
        """
        x 只能是一个由0~9 组成的数字字符串
        """
        if isinstance(x, str):
            if not x.isdigit():
                raise "please input a string just include 0~9"
            if not self.queue.full():
                self.queue.put(x)
            else:
                return "queue is full"
        else:
            raise "please input a string"

    def get(self):
        if self.queue.empty():
            return None
        return self.queue.get(block=True, timeout=None)


def print_directory_contents(sPath, sPath_files):
    import os
    for sSon in os.listdir(sPath):
        sSonPath = os.path.join(sPath, sSon)
        if os.path.isdir(sSonPath):
            print_directory_contents(sSonPath, sPath_files)
        else:
            sPath_files.append(sSonPath)
    return sPath_files

def print_directory_contents1(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents1(sChildPath)
        else:
            print(sChildPath)

def test_queue():
    q = NumQueue()
    q.put("12")
    q.put("13")
    q.put("14")
    q.put("15")
    q.put("16")
    q.put("17")
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == "__main__":
    # ff = print_directory_contents("/home/baiyj/Desktop/面试整理", [])
    # for item in ff:
    #     print(item)


    print_directory_contents1("/home/baiyj/Desktop/面试整理")
