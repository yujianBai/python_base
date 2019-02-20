#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: c1.py.py
@time: 2019/2/19 16:21
"""

import re

a = "c|c++|Java|C#|Python|Javascript"
b = "c0c++9Java3C#2Python9Javascript"

# print(a.index("Python") > -1)
# print("Python" in a)

pattern1 = "(Python)"
r = re.findall(pattern1, a)
if len(r) > 0:
    print(r)


r2 = re.findall("\d", b)
print(r2)

r3 = re.findall("[a-zA-Z+]+", b)
print(r3)

r4 = re.findall("^\d", b)
print(r4)

c = "python0python1pythonn2"
r5 = re.findall("python*", c)# * 前的一个字符出现一次， 或多次
print(r5)

d = "python python python python python"
r6 = re.findall("(python ){2}", d) #组的概念， 没太了解
print("r6",r6)
