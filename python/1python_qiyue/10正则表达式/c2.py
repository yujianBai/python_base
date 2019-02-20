# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午9:34
# @Author  : Baiyj

# @File    : c2


import re

'''
匹配模式： 

re.I:忽略大小写
re.S: . (点号)匹配所有字符， 包括换行符
re.findall(正则表达式， 匹配字符串， 模式)
'''

lanuage = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', lanuage, re.I|re.S)
print(r)


r1 = re.findall('c#', lanuage, re.I)
print(r1)
