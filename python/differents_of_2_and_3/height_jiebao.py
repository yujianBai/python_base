# auth Bernard
# date 2020-04-16

'''
高级解包操作
'''

if __name__ == "__main__":
    a, b, *rest = range(10)
    print(a)
    print(b)
    print(rest)
