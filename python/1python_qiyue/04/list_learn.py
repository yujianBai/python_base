#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: list_learn.py.py
@time: 2019/2/18 17:46
"""

class my_lsit(object):
    def __init__(self, a):
        self.a = a

    def __mul__(self, cls):
        self.a = self.a - cls.a
        return self.a

if __name__ == "__main__":
    a = my_lsit(10)
    # print(a)
    b = my_lsit(8)
    # print(b)
    print(a.__mul__(b))
