# auth Bernard
# date 2020-06-07

"""
3.从尾到头打印链表arrayList： 遍历链表，保存在list中，然后倒序输出
"""


def list_resolve(list):
    return list[::-1]


def pritnlistFromTailToHead(listNode):
    if listNode == None:
        return []
    result = []
    while listNode != None:
        result.append(listNode.val)
        listNode = listNode.next
    return result[::-1]


def test_list_insert():
    aa = [1, 2, 3, 4, 5]
    result = []
    for i in aa:
        result.insert(0, i)
    return result


if __name__ == "__main__":
    # print(list_resolve([1, 2, 3, 4, 5]))
    # print(sorted([1, 2, 3, 4, 5], reverse=True))
    print(test_list_insert())
