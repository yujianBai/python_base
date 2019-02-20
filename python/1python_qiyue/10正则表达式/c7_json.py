# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午11:29
# @Author  : Baiyj

# @File    : c7_json

import json

#json 的规范，这种key 和 字符串类型的value需要使用双引号
#json 的bool值是小写的false, true
json_str = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18}]'

'''
字符串中间要使用 双引号，那么字符串外面的边界引号，要使用单引号
'''


'''
    反序列化：
        json 有着自己的数据格式， 我们用loads函数将json格式的数据
        转化为python 格式的数据，
        在编程中有这么一个术语定义：
            从字符串到某种语言的格式的解析过程，就叫做反序列化
        
'''
j_str = json.loads(json_str)
print(j_str, "type:", type(j_str))
# print(j_str['name'])
# print(j_str['age'])
