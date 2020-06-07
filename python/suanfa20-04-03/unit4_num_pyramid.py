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
total_path = []


def search(depth, x, y):
    if depth == 5:
        # print(datas)
        total_path.append(datas[:])
        # print(total_path)
    else:
        # 选择垂直下方
        datas.append(pyramid[depth][y])
        search(depth + 1, x + 1, y)
        datas.pop()

        # 选择右下方
        datas.append(pyramid[depth][y + 1])
        search(depth + 1, x + 1, y + 1)
        datas.pop()


if __name__ == "__main__":
    search(1, 0, 0)
    max = 0
    max_pos = 0
    for index, data in enumerate(total_path):
        if sum(data) > max:
            max_pos = index
            max = sum(data)
    print(total_path[max_pos])
