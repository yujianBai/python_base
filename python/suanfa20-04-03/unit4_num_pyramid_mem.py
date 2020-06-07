# auth Bernard
# date 2020-04-06

pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]
datas = [13]
max_value = 0


def search(depth, x, y):
    if depth == 5:
        global max_value
        if max_value < sum(datas):
            max_value = sum(datas)
    else:
        # 选择垂直下方
        datas.append(pyramid[depth][y])
        search(depth + 1, x + 1, y)
        datas.pop()

        # 选择右下方
        datas.append(pyramid[depth][y + 1])
        search(depth + 1, x + 1, y + 1)
        datas.pop()

info = {}
def search_max(depth, y):
    if depth == 4:
        return pyramid[depth][y]
    # 1, 把左下方的值交给下一个人得到最大值
    # 2, 把右下方的值交给下一个人得到最大值
    # 1, 任务可以下分， 2， 最优子结构， 3，决策
    if "{}_{}".format(depth, y)in info:
        return info["{}_{}".format(depth, y)]
    else:
        max_value = pyramid[depth][y] + max(search_max(depth + 1, y),
                                       search_max(depth + 1, y + 1))
        info["{}_{}".format(depth, y)] = max_value
        return max_value


if __name__ == "__main__":
    search(1, 0, 0)
    print(max_value)
    # print(search_max(1, 0))
