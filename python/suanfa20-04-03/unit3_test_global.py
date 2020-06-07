# auth Bernard
# date 2020-04-06

"""
global x
x = 1


def change_x():
    x = 2
# global 定义在函数之外， 函数内部无法修改global x
"""

"""
x = 1


def change_x():
    global x
    x = 2
    
# global x定义在函数内，函数可以修改x
"""

"""
x = 1


def change_x():
    x = 2
    
# 函数内部无法修改函数外的x的值
"""

"""
# 只在函数内部定义 global x 按照如下测试方法是没有语法错误的
# 当change_x 递归调用的时候，会出错，应该在函数外部定义x初值，函数内部将其值改变

def change_x():
    global x
    x = 2
"""

if __name__ == "__main__":
    change_x()
    print(x)
