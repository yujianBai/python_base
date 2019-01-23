#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: build_in_fun.py
@time: 2019/1/22 10:17
"""


'''
python 内置函数

all(iterable)
any(iterable)
cmp(x, y)
dict([arg])
enumerate(iterable[, start = 0])
isinstance(object, classinfo)
pow(x, y, [,z])
zip([iterable, ])

在 itertools 模块中有很多很不错的函数

'''

iterable = [1, 2, 3]

def test_all():
    _all = True
    for item in iterable:
        if not item:
            _all = False
            break
    if _all:
        print "all is True"
    else:
        print "all is False"

def test_build_in_all():
    if all(iterable):
        print "all is True"
    else:
        print "all is False"

def test_build_in_any():
    if any(iterable):
        print "any is True"
    else:
        print "any is False"

def test_build_in_dict():
    list = [(1, 'a'), (2, 'b'), (3, 'c')]
    dict_list = dict(list)
    print dict_list

def test_build_eunmrate():
    print "in enumerate"

    for i, item in enumerate(iterable):
        print i, item

    for i in range(len(iterable)):
        print i,iterable[i]

    for item in iterable:
        print item

    print "end enumerate"

def test_build_isinstance():
    if isinstance(iterable, list):
        print "iterable is list"

def test_build_zip():
    l1 = ("1", "2", "333")
    l2 = ("a", "b", "222")
    out = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            out.append((l1[i], l2[i]))
    print "by range", out

    out = zip(l1, l2)
    print "by zip()", out
    print "by zip()", zip(*out)


def test_build_pow():
    print pow(2, 3), pow(2, 4, 10)

def test_build_cmp():
    print cmp(1, 3), cmp(1, 0), cmp(1, 1)


if __name__ == "__main__":
    test_all()
    test_build_in_all()
    test_build_in_any()
    test_build_in_dict()
    test_build_eunmrate()
    test_build_isinstance()
    test_build_cmp()
    test_build_pow()
    test_build_zip()
