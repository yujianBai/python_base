#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c5_filter.py
@time: 2019/2/21 17:29
"""

list_x = [0, 0, 1, 12, 0, 0, 9]
print(list(filter(None, list_x)))


'''
filter特点：
    过滤器，
    根据第一个函数参数的真假， 过滤第二个参数的集合
'''


list_s = ['a', 'B', 'c', 'D']
print(list(filter(lambda x: True if 'a' <= x <='z' else False,
                  list_s)))
