# auth Bernard
# date 2020-04-05
import random


# data = [1, 7, 17, 19, 21, 22, 35, 66, 77, 99, 101]

def produce_data(start, stop, length):
    # 随机生成一个长度为length的list
    data_list = []
    for i in range(length):
        data_list.append(random.randint(start, stop))
    return data_list


def search2(left, right, data_list, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == data_list[mid]:
        return mid
    elif target > data_list[mid]:
        return search2(mid + 1, right, data_list, target)
    else:
        return search2(left, mid - 1, data_list, target)


if __name__ == "__main__":
    data = sorted(produce_data(1, 100, 10))
    print(data)

    print(search2(0, len(data) - 1, data, 17))
    print(search2(0, len(data) - 1, data, 101))
