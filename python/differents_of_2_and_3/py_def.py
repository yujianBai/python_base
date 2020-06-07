# auth Bernard
# date 2020-04-17


def flist(l):
    l.append(0)
    print(id(l), l)


l = []
print("id l :{}".format(id(l)))
flist(l)
flist(l)


# l是list类型的可变对象， 两次调用后l 是[0, 0], 对象传递，形参和实参指向同一个对象

def fstr(s):
    s += 'a'
    print(id(s), s)


s = 'hehe'
print("id s :{}".format(id(s)))
fstr(s)
fstr(s)
# 当传递s时， 拷贝了一个s的副本给函数。, 所以s字符串的id和 函数调用过程中的id不一致

"""
这两个函数的考察点：传参方式， 可变对象
可变类型作为参数
不可变类型作为参数

python作为对象引用进行参数传递

python如何进行参数传递？
    py唯一支持的参数传递是共享传参 (python 既不是值传递， 也不是引用传递)
    Call by object (Call by Object Refrence or Call by Sharing)
    
    Call by sharing (共享传参) 函数形参使用的实参中各个引用的副本
    
    python中 一切皆对象（变量也是对象）
    list 是可变对象
    str 不是可变对象 
   
python 中的可变不可变对象：
    不可变： bool/ int/ float/ tuple/ str/ frozenset
    
    可变： list/ set/ dict 
"""

print("*" * 20, "clare_list")


def clear_list(l):
    l = []


ll = [1, 2, 3]
clear_list(ll)
print(ll)

"""
这里的结果为什么是 【1， 2， 3】
函数内部，给l 重新赋值为空列表, 并不是修改原来的变量
"""

print("*" * 10, "flist1")


def flist1(l=[1]):
    l.append(1)  # 修改原来的变量
    print(l)


flist1()
flist1()

"""
这里的结果两次调用之后为什么是 【1， 1， 1】

默认参数只计算一次
"""

print("*" * 20, "python 可变参数")
"""
    python *args , **kwargs 含义：
    用来处理可变参数
    *args 被打包为 tuple
    **kwargs 被打包为 dict
"""


def print_multiple_args(*args):
    print(type(args), args)
    for idx, val in enumerate(args):
        print(idx, val)


print_multiple_args('a', 'b', 'c')
print_multiple_args(*['a', 'b', 'c'])  # 函数参数为 *args时， 传递列表需要用 * 解包
print_multiple_args(*('a', 'b'))  # 函数参数为 *args时， 传递列表需要用 * 解包
print_multiple_args(*('a'))  # 函数参数为 *args时， 传递列表需要用 * 解包


def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    for k, v in kwargs.items():
        print("{}:{}".format(k, v))


print_kwargs(a=1, b=2)
print_kwargs(**{'a': 1, 'b': 2})  # 传参字典 需要用 ** 解包
