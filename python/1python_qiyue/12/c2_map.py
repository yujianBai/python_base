#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c2_map.py
@time: 2019/2/21 17:09
"""

def squre(x):
    return x * x

list_x = [1, 2, 3, 4, 5, 6]

r = map(squre, list_x)
print(list(r))


