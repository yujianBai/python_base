#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c6_zhuangshiqi.py
@time: 2019/2/21 17:41
"""
import time
from datetime import datetime
TIMEFMART = '%Y-%m-%d %H:%M:%S'

def get_now(func):
    def warpper(*args):
        print(datetime.now())
        func(*args)
    return warpper



# 对修改时封闭的， 对扩展时开放的


@get_now
def f1(func_name):
    print("this is a funcetion" + func_name)

@get_now
def f2(func_name, func_name2):
    print("this is a funcetion" + func_name + func_name2)

if __name__ == "__main__":
    # f = get_now(f1)
    # f()

    f1('name1')
    f2('name1', 'name2')


