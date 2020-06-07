# auth Bernard
# date 2020-04-16

'''
限定关键字参数
keyword only arguments
'''


def add(a, b, c):
    return a + b + c


def add1(a, b, *, c):
    # py3 限定关键字参数， 需要指定参数名传参
    # py2 add1(a, b, c=0):
    return a + b + c


# 调用add1, 时传 * 后的参数需要指定参数名


'''
chained exceptins , python3 
重新抛出异常不会丢失栈信息
'''

import shutil


def mycopy(source, dest):
    try:
        shutil.copy2(source, dest)
    except OSError: # py2里， raise 会丢失原来的 traceback信息
        raise NotImplementedError("automatic sudo injection") from OSError


'''
一切返回迭代器 
range, zip, map, dict.values, etc. are all iterators.
用途:节省内存
'''



if __name__ == "__main__":
    print(add1(1, 2, c=4))
