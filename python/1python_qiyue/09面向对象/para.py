#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: para.py.py
@time: 2019/2/19 11:09
"""

class A():
    aa = 'class aa'
    bb = 2

    def __init__(self, aa, bb):
        self.aa = aa
        self.dd = bb
        print(aa)
        print(bb)
        print(A.aa)


class B:
    def __init__(b):
        print("init class B")
        b.a = 1
        b.b = 2

    def get_a(b):
        return b.a

class C(object):
    def __init__(self):
        pass

a = A("a aa", "b bb")
# print(dir(a))


print('类变量' + str(a.aa))                   #这里打印的是实例变量,pythong 类的属性参数，访问的顺序是先访问
                                             # 实例变量， 再访问类变量（ __dict__ ）

print ('A 实例变量{}'.format(a.__dict__))     #实例变量

print ('class A 类变量{}'.format(a.__class__.__dict__))
print ('class A 类变量{}'.format(A.__dict__)) #类变量

# print(dir(a))
print(a.bb)

print("calss para type")
#打印实例属性，不会告诉你这个变量是啥类型的变量（类变量，实例变量），只有简单的变量类型
print(type(a.aa))
print(type(a.dd))

#==================
b = B()

