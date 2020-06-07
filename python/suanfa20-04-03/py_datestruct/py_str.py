# auth Bernard
# date 2020-04-19

"""
python 字符串常考算法题
了解字符串造作：
    python内置的方法： split, upper, replace等

    常考题：
        1， 反转字符串
        2， 判断一个数字是否回文数
"""


class solution:
    def reverseString(self, s):
        """
        input:
        ["h", "e", "l", "l", "o"]
        只能原地修改, 不能开辟额外空间 !!!
        """
        # s.reverse()
        start = 0
        end = len(s) - 1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def huiwenshu(self, i):
        """
        从前往后， 和从后往前一样
        """
        if i < 0:
            return False
        s = str(i)
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


"""
python 内置函数
>>> s = ["h", "e", "l", "l", "o"]
>>> reversed(s)
<listreverseiterator object at 0x7f33abd4e0d0>
>>> s
['h', 'e', 'l', 'l', 'o'] # 没有变化
>>> 

>>> s.reverse()
>>> 
>>> s  # 调用s.reverse(), s 被修改了
['o', 'l', 'l', 'e', 'h']
"""

if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    ss = solution()
    ss.reverseString(s)
    print(ss.huiwenshu(12345))
    print(ss.huiwenshu(1234554321))
    print(ss.huiwenshu(1))
