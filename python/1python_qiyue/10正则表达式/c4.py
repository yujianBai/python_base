# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午10:40
# @Author  : Baiyj

# @File    : c4

import re

s = "A8C372D82"

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    return '0'

r = re.sub('\d', convert, s)
print(s)
print(r)


def convert1(value):
    matched = value.group()
    if int(matched) >= 50:
        return '100'
    return '001'

r = re.sub('\d\d', convert1, s)
print(s)
print(r)
