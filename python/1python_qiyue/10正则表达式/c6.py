# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午10:58
# @Author  : Baiyj

# @File    : c6

import re

s = "life is short , i use python"
r = re.search('(life)(.*)(python)', s)
print(r.group())
print('分组组成的一个tuple: ', r.groups())
print(r.group(0), r.span(0))
print(r.group(1), r.span(1), type(r.span()))
print(r.group(2), r.span(2))
print(r.group(3))

# r = re.findall('life.*python', s)
# print(r[0])
