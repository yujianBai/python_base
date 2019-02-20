# -*- coding: utf-8 -*-
# @Time    : 19-2-20 下午9:48
# @Author  : Baiyj

# @File    : c3.py

'''
re.findall()

re.sub() //查找之后替换

'''
import re
lanuage = r'PythonC#\nJavaPHPC#C#'
r = re.sub('C#', 'GO', lanuage, 0)
#这里的0，的意思是继续向下无限匹配

# r = re.sub('C#', 'GO', lanuage, 1)
print(r)


# print(lanuage.replace('C#', 'GO'))
#和上述正则同理


def convert(value):
    '''
    print(value)

    <_sre.SRE_Match object; span=(6, 8), match='C#'>
    <_sre.SRE_Match object; span=(17, 19), match='C#'>
    <_sre.SRE_Match object; span=(19, 21), match='C#'>
    这个value 不是简单的 传入参数
    '''
    # return 'Redis'
    matched = value.group()
    return '!!' + matched +'!!'

rdef = re.sub('C#', convert, lanuage, 0)
'''
convert 调用流程:

这个应用场景：
    可以根据不通的场景， 将同一个匹配对象替换为不同的值
    
'''
print(rdef)
