# auth Bernard
# date 2020-04-19
"""
链表涉及到指针的操作， 比较复杂， 容易出错， 经常用作考题
    熟悉量表的定义和常见操作
    常考题： 删除一个链表的节点, 合并两个有序链表

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self, list_val):
        print("init LinkList:{}".format(list_val))
        self.len = len(list_val)
        self.head = None
        self.init_list(list_val)

    def init_list(self, list_val):
        new0_node = ListNode(list_val[0])

        new1_node = ListNode(list_val[1])
        new0_node.next = new1_node

        new2_node = ListNode(list_val[2])
        new_node.next = new2_node

        new3_node = ListNode(list_val[3])
        new2_node.next = new3_node

        new4_node = ListNode(list_val[4])
        new3_node.next = new4_node

        new5_node = ListNode(list_val[5])
        new4_node.next = new5_node

    def list_val(self):
        list_val = []
        node = self.head
        for i in range(self.len):
            if node:
                list_val.append(node.val)
                node = node.next
        return list_val


class Solution:
    def deleteNode(self, node):
        nextnode = node.next
        after_next_node = node.next.next
        node.val = nextnode.val
        node.next = after_next_node


def test_link_list():
    lk = LinkList([1, 2, 3, 4, 5, 6])
    # print("type: ", type(lk))
    # print("head: ", lk.head)
    # print("head.val: ", lk.head.val)
    # print("head.next: ", lk.head.next)

    # print("list len: ", lk.len)
    # print("list_val: ", lk.list_val())
    # Solution(ListNode(2))

    node = lk.head
    # print("ln len is :", lk.len)
    for i in range(lk.len):
        if node:
            print("in for loop node.val:{}".format(node.val))
            node = node.next


if __name__ == "__main__":
    test_link_list()
