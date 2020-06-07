# auth Bernard
# date 2020-04-04

data = [1, 7, 17, 19, 21, 22, 35, 66, 77, 99, 101]


# 二分查找，有效的方式是查找一个有序的数列
# 因为在查找过程中，是通过下标访问去和目标数去比较


def serach_binary(array, target):
    length = len(array)
    mid = length // 2
    while mid < length and mid >= 0:
        if target == array[mid]:
            return mid + 1
            break
        elif target > array[mid]:
            mid = (mid + length) // 2
        else:
            mid = mid // 2
    return -1


def search_bin(data_list, target):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        # 1, 找到[left, right]中间的值
        mid = int((left + right) / 2)
        # 2, 判断中间位置的值和目标值的大小
        if data_list[mid] == target:
            print("查询到数据，所在位置：{}".format(mid + 1))
            break
        elif data_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test_search():
    assert serach_binary(data, 1) == 1
    assert serach_binary(data, 19) == 4
    assert serach_binary(data, 101) == 11


if __name__ == "__main__":
    # print(serach_binary(data, 22))
    # print(serach_binary(data, 7))
    # print(serach_binary(data, 17))
    # print(serach_binary(data, 1))
    # print(serach_binary(data, 35))
    search_bin(data, 22)
    search_bin(data, 99)
    search_bin(data, 101)
