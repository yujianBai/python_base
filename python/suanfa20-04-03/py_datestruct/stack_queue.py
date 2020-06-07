# auth Bernard
# date 2020-04-19

"""
栈和队列

后进先出 和 先进先出

    熟练使用python list 或者 collections.deque()实现 栈和队列
    用栈实现队列
    leetcode implement-queue-using-stacks
"""

from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class Myqueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self):
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.top()

    def empty(self):
        return self.s1.empty() and self.s2.empty()


def test():
    q = Myqueue()
    q.push(1)
    print(q.pop())
    q.push(3)
    q.push(5)
    q.push(4)
    print(q.pop())
    q.push(7)
    # print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.pop())

def test_stack():
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())

if __name__ == "__main__":
    test()
    # test_stack()
