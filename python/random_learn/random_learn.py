#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: random_learn.py.py
@time: 2019/2/14 15:55
"""


import random
print "randint(a, b); 获取a到b之间的一个整数"
print random.randint(1, 10)

print "choice(list), 随机的获取list中的一个元素"
# list_a = [1, 2, 3, 4, 5]
list_a = ['a', 'b', 'c']
print random.choice(list_a)

print "从指定范围内，按照指定基数递增的集合中获取一个随机数，" \
      "基数缺省值为1"\
      "randrange[[start,], stop, [,step]]"

print random.randrange(0, 9, 2)
'''
>>> randrange(10)                        # Integer from 0 to 9 inclusive
7
>>> randrange(0, 101, 2)                 # Even integer from 0 to 100 inclusive
26
'''

print "shuffle(list), 就地打乱list, 函数返回none"
print random.shuffle(list_a)
print list_a
