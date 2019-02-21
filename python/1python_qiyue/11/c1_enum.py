#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c1_enum.py
@time: 2019/2/21 10:11
"""

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    # YELLOW = 5 不可使用相同标签 表示不同类型

print(VIP.YELLOW)
#枚举的意义在于他的标签， 而不是它具体的值
#所有print 打印出的结果为 VIP.YELLOW 是合理的。如果打印出的是，YELLOW代表的值。
#那就失去了 枚举的意义，这样它和其它的类， 就没有区别了


# VIP.YELLOW = 6 不可修改， 修改会报错


print(VIP.YELLOW.value) #通过value获取枚举类型的值
print(VIP.YELLOW.name) #通过name获取枚举类型的标签



for enum_type in VIP:
    print(enum_type)
