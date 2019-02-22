#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c2.py
@time: 2019/2/22 10:26
"""

class Test():
    def __bool__(self):
        return False

    def __len__(self): #这里的返回值只能是 int 类型 或者bool
        return 0