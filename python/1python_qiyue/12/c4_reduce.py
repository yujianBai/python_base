#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c4_reduce.py.py
@time: 2019/2/21 17:18
"""

from functools import reduce

print(reduce(lambda x, y : x + y, range(1,11)))

print(sum(range(1, 11)))


list_str = ['h', 'e', 'l', 'l', 'o']
print(reduce(lambda x, y:x + y, list_str, 'i'))
#recude 的第三个参数， 是第一个函数参数的初始值

print(reduce(lambda x, y:x * y, range(1, 6)))


'''
编程模型：
    map/reduce 
    映射， 归约
'''

