# auth Bernard
# date 2020-04-19

"""
常考题型：
    常见的数据结构链表， 队列， 栈， 二叉树， 堆
    使用内置数据结构实现高级数据结构， 比如内置的list/ deque实现
    Leetcode 或者剑指offer上的常见题
"""

"""
常考数据结构链表
    链表单链表， 双链表， 循环链表
        如何用python实现链表结构
        实现链表常见操作， 比如插入节点， 
"""

"""
单链表 |val|nest|

双链表 |pre|val|next|
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre


"""
数据结构之队列：
    Collections.deque 双端队列
"""
from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


"""
栈 stack, 是后进先出

    如何使用python 栈
    实现栈的push, 和 pop，如何做到后进先出
    同样可以用 python list 或者collections.deque实现栈
"""


class Stack():
    def __init__(self):
        self.stack = deque()
        # self.stack = list()

    def pop(self):
        if self.empty():
            return None
        return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def empty(self):
        return len(self.stack) == 0


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


"""
课后题：
    实现最小值栈, MiniStack 可以获取栈的最小值
    
    用两个栈实现一个先进先出的队列
"""

"""
python dict/set 底层都是哈希表
    哈希表的实现原理， 底层其实就是一个数组
    根据哈希函数快速定位一个元素， 平均查找O(1)，非常快
    不断加入元素会引起哈希表重新开辟空间， 拷贝之前元素到新数组

哈希表如何解决冲突：
    链接法和开放寻址法
        元素key冲突之后使用一个链表填充相同的key元素
        开放寻址法是冲突之后根据一种方式（二次查探）寻找下一个可用的槽
        cpython使用的就是 二次探查
"""

"""
常考数据结构之二叉树
    先序遍历， 中序， 后序
    先（根）序：先处理根， 之后是左子树， 然后是右字树
    中（根）序：先左， 后根， 然后右
    后（根）序：先左， 后右， 然后根
    
    二叉树：
        |val|left|right|
"""


# 树的遍历，

class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_trav(self, subtree):
        # 先根序遍历
        if subtree is not None:
            print(subtree.data)  # 先序遍历
            self.preorder_trav(subtree.left)  # 递归处理左子树
            self.preorder_trav(subtree.right)  # 递归处理右子树

    def inorder_trav(self, subtree):
        if subtree is not None:
            self.preorder_trav(subtree.left)
            print(subtree.data)  # 中序遍历
            self.preorder_trav(subtree.right)


"""
堆其实是完全二叉树， 有最大堆 和最小堆
    最大堆：对于每个非叶子节点v, V的值都比它的两个孩子大
    最大堆支持每次pop操作获取最大元素， 最小堆获取最小元素
    常见问题： 用堆来完成topk问题， 从海量数字中寻找最大的k个元素
"""
import heapq


class Topk:
    """
    获取大量元素topk 大个元素， 固定内存
    思路：
        1， 先放入元素前k个建立一个最小堆
        2， 迭代剩余元素：
            如果当前元素小于堆顶元素， 跳过该元素(肯定不是前K大)
            否则替换堆顶元素为当前元素， 并重新调整堆
    """

    def __init__(self, iterable, k):
        self.minheap = []  # 最小堆
        self.capacity = k  # 容量
        self.iterable = iterable  # 查找对象

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)
                # 返回并且pop堆顶最小值， 推入新的val值并调整堆
        else:
            heapq.heappush(self.minheap, val)  # 前k个元素直接放入minheap

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap


def test_get_topk():
    import random
    i = list(range(20))
    random.shuffle(i)
    print(i)
    k = Topk(i, 10)
    print(k.get_topk())


if __name__ == "__main__":
    # re_l = Solution()
    # print(re_l.reverseList([1, 2, 3, 4, 5]))
    # test_queue()
    # test_stack()
    test_get_topk()
