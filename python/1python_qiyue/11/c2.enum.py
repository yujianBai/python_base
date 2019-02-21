#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c2.enum.py
@time: 2019/2/21 10:33
"""
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4

ret = VIP.YELLOW == VIP.GREEN  #可以进行等值比较
print(ret)


# ret = VIP.YELLOW > VIP.GREEN //枚举类型不可进行大小比较
# print(ret)


ret = VIP.YELLOW is VIP #可以进行is 判断
print(ret)


print(VIP.YELLOW_ALIAS) #ret = VIP.YELLOW, 因为他们是value相等，
#python 将会把YELLOW_ALIAS当作 YELLOW的别名

for v in VIP:
    print(v)

for v in VIP.__members__: #可以打印出别名 标签
    print(v)
