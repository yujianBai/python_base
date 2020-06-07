# auth Bernard
# date 2020-04-19
"""
二叉树：
    二叉树涉及到递归和指针操作， 常结合递归考察：
        二叉树的操作可以用递归的方式解决， 不了解递归可能会比较吃力
        常考题：二叉树镜像， 如何层序遍历二叉树(广度优先)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class TreeNode1:
    def __int__(self, val, left, right):
        self.val, self.left, self.right = val, left, right


# 反转二叉树， 二叉树镜像
def invert(root):
    if root:
        root.left, root.right = root.right, root.left
        invert(root.left)
        invert(root.right)
    return root


# 遍历二叉树, 广度优先



if __name__ == "__main__":
    pass
