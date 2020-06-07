#auth Bernard
#date 2020-06-07

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        self.head = False


class NodeList:
    def __init__(self, list):
        pass

'''
栈的抽象数据结构
栈是有序的LIFO(后进先出)。
栈的操作有：
Stack() 创建新的空栈。
push(item) 添加新项到栈顶部。
pop() 删除栈顶项并返回栈顶项的值。栈被修改。
peek() 返回栈顶部项。不修改栈。
isEmpty() 测试栈是否为空，返回 Bool 值。
size() 返回栈长度（栈中 item 数量）。
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



if __name__ == "__main__":
    pass