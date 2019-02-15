#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c1.py.py
@time: 2019/2/15 15:21
"""

from contextlib import contextmanager
@contextmanager
def book_mark():
    print '{}'.format("《"),
    yield
    print '{}'.format("》"),

with book_mark():
    print '{}'.format("且将生活一饮而尽"),

