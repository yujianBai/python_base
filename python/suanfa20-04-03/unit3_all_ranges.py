# auth Bernard
# date 2020-04-06


"""
全排列
1， 2， 3
1， 3， 2
2， 1， 3
2， 3， 1
3， 1， 2
3， 2， 1
"""

# 类似处理所有场景的问题使用回溯法

data_list = [1, 2, 3, 4]
array = []
total = 0


def search(depth, datas):
    if depth == len(data_list) + 1:
        print(array)
        global total
        total += 1
    else:
        # 解空间是变化的
        for data in datas:
            # 1, 设置现场
            array.append(data)
            # 2, 递归
            next_datas = datas[:]
            next_datas.remove(data)
            search(depth + 1, next_datas)
            # 3, 恢复现场
            array.pop()


if __name__ == "__main__":
    search(1, data_list)
    print("一共{}种排列方式".format(total))
