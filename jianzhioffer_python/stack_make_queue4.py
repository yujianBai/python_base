# auth Bernard
# date 2020-06-07

'''
4.两个栈实现一个队列：
stack2作为中转stack，直接对stack1做push，
pop的时候将stack1的pop到stack2中，

便可以实现。stack：先入后出，queue：后入先出
'''
from jianzhioffer_python.util import Stack


class MyQueue:
    def __init__(self, stack_a, stack_b):
        self.in_stack = stack_a
        self.out_stack = stack_b

    def push(self, node):
        self.in_stack.push(node)

    def pop(self):
        while not self.in_stack.isEmpty():
            node = self.in_stack.pop()
            self.out_stack.push(node)
        return self.out_stack.pop()


def test_stack():
    a_s = Stack()
    a_s.push(1)
    a_s.push(2)
    print(a_s.pop())
    print(a_s.pop())

if __name__ == "__main__":

    # test_stack()
    stack_a = Stack()
    stack_b = Stack()
    my_queue = MyQueue(stack_a, stack_b)
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    my_queue.push('aaaa')
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())
    print(my_queue.pop())
