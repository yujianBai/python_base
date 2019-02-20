# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午10:50
# @Author  : Baiyj

# @File    : c5


'''

re.match()

re.search()

只匹配第一次

据说这两个函数没有，findall好用
'''

import re
s = "8C372D82"

r = re.match('\d', s)
'''
match 从字符串的开始， 开始匹配，匹配不到就返回空
'''

r1 = re.search('\d', s)
'''
search 从字符串中搜索，找到第一个开始的位置
'''


'''
返回值：
    span()返回匹配字符的位置
    group()匹配的具体字符
'''
print(r.span())
print(r1.group())