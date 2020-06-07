# auth Bernard
# date 2020-04-19

"""
数据结构之堆
堆的常考题基本围绕在合并多个有序数据/链表； Topk问题
    理解堆的概念， 堆是完全二叉树， 有最大堆和最小堆
    会使用python内置的heapa模块实现堆的操作
    常考题： 合并K个有序链表， leetcode merge-k-sorted-list
"""

"""
1, 读取所有链表值
2， 构造一个最小堆heapq很容易实现
3， 根据最小堆构造一个链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from heapq import heapify, heappop


class Solution:
    def mergeKlists(self, lists):
        # 读取所有节点值
        h = []  # 最小堆
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        # 构造一个最小堆
        if not h:
            return None
        heapify(h) # 转换为最小堆

        # 构造链表
        root = ListNode(heappop(h))
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root

"""
heapq 构造最小堆
>>> import heapq
>>> h = []
>>> h.append(1)
>>> h.append(2)
>>> h.append(3)
>>> h.append(4)
>>> h.append(0)
>>> h
[1, 2, 3, 4, 0]
>>> heapq.heappop(h)
1
>>> heapq.heappop(h)
0
>>> heapq.heappop(h)
2
>>> heapq.heappop(h)
3
>>> heapq.heappop(h)
4
"""

if __name__ == "__main__":
    pass
