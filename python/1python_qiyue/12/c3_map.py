#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c2_map.py
@time: 2019/2/21 17:09
"""


list_x = [1, 2, 3, 4, 5, 6]
list_y = [1, 2, 3, 4, 5, 6, 7]

r = list(map(lambda x: x*x, list_x))
print(r)


r = list(map(lambda x, y: x*x + y, list_x, list_y))
print(r)

