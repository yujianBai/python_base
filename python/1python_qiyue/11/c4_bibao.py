#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c4_bibao.py
@time: 2019/2/21 15:11
"""

def curve_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve

a = 50
f = curve_pre()
print(f(2))


# f 的环境变量
print(f.__closure__)
print(f.__closure__[0].cell_contents) #环境变量 a= 25

'''
函数外修改a的值， 调用结果不变，
这个是闭包的现象

闭包：
    函数 + 定义环境变量
    
    闭包把当时调用的现场也保存下来了
'''

print("闭包测试\n")
def f1():
    a = 10
    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)
#上述函数不是闭包， 内部函数中对函数外部的a赋值， 导致它没有引用外部环境变量a
#是不是闭包， 看看函数有没有 __closure__属性
f1()