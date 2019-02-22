#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c3.py
@time: 2019/2/22 10:47
"""
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        func()
    return wrapper

@decorator
def f1():
    '''
    This is f1
    :return:
    '''
    print("func in %s "%f1.__name__)

print(help(f1))
# f1()