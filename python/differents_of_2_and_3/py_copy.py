# auth Bernard
# date 2020-04-17

"""
深拷贝 与 浅拷贝

区别：
    什么是深拷贝
        a = 1
        b = 1
        a, b指向的不是同一个对象 (而是这个对象的拷贝， "内容相同")

    什么是浅拷贝
        定义一个对象 a指向这个对象 （a= 1）
        b = a (b 也指向这个对象)， a修改b也修改
    python中如何实现深拷贝

"""

"""
问题：
如何实现深拷贝？

python中如何正确初始化一个二维数组
"""

def deep_copy(a):
    pass

def init_array(x, y):
    array = []
    array2 = []
    for i in range(y):
        array.append(0)

    for j in range(x):
        array2.append(array)
    return array2


if __name__ == "__main__":
    print(init_array(4, 5))
