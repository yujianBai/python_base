#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c3_enum.py
@time: 2019/2/21 14:32
"""

# from enum import Enum, unique
from enum import Enum

# @unique #unique 装饰器 unique 限制枚举数据不可重复
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3

a = 1
print(VIP(a))

#枚举转换


