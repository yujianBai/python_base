#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: param_num.py.py
@time: 2019/2/14 16:32
"""

#求100以内质数

def method1(n):
    pn = []
    for x in range(2,n):
        for i in pn:
            if x % i == 0:
                break
        else:
            pn.append(x)
    print pn

def method2(n):
    import math
    pn = []
    for x in range(2, n):
        flag = False
        for i in pn:
            if x % i == 0:
                flag = True
                break
            if i > math.ceil(x ** 0.5):
                flag = False
                break
        if not flag:
            pn.append(x)
    print pn



if __name__ == "__main__":
    method1(100)
    method2(100)

