# auth Bernard
# date 2020-04-16
'''
python3 type hint 帮助ide 实现类型检查
py2 中没有这个方法

'''


def hello(name : str) -> str:
    return 'hello ' + name


if __name__ == "__main__":
    print(hello('world'))
