#auth Bernard
#date 2020-04-06

"""
数字分解
num = 7
1+1+1+1+1+1+1
1+2+4
...

所有的分解
# 1, 老大拿到这个数之后， 先尝试所有可能取值，上一个分给自己的值
# 2，
"""

datas = []
def search(rest):
    if rest <= 0:
        print(datas)
    else:
        for i in range(1, rest+1):
            # 1, 设置现场
            datas.append(i)
            # 2， 递归
            search(rest-i)
            # 3， 恢复现场
            datas.pop()

if __name__ == "__main__":
    search(7)