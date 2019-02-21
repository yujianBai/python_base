#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c5_closure.py
@time: 2019/2/21 16:02
"""

start_pos = 0
def triver(pos):
    def t_len(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return  t_len


t = triver(start_pos)
for x in range(1, 5):
    print( t(x) )
    print('闭包变量：', t.__closure__[0].cell_contents)
    # //环境变量，常驻内存， 容易内存泄漏


print ('不用闭包解决问题')
origin= 0

def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return new_pos

print(go(2))
print(go(3))
print(go(5))
