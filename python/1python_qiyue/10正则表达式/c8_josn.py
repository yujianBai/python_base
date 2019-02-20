# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午11:50
# @Author  : Baiyj

# @File    : c8_josn


import json


str_d = [
    dict(age = 19, name = 'qiyue', job = 'IT Web'),
    dict( age = 18, name = 'bai', job = 'IT', flag = False)
]

'''
序列化：
    将编程语言的格式的数据转化为json字符串
'''


str_j = json.dumps(str_d)
print(str_j, type(str_j))


