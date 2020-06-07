# auth Bernard
# date 2020-06-07

'''
1.二维数组中的查找
Q: 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

A1： 遍历整个二维数组，O(n2)

A2: 从右上或者左下开始查找。从右上开始查找：如果数组中的数比这个整数大，向左移动一位，如果数组中的数比这个数小，向下移动一位，O(n) O(n)O(n)。
'''


def find(target, array):
    if array == []:
        return False
    num_row = len(array)
    num_col = len(array[0])

    i, j = 0, num_col - 1

    while j >= 0 and i < num_col:
        if array[i][j] > target:
            j -= 1
        elif array[i][j] < target:
            i += 1
        else:
            return True, array[i][j]
    return False, None


if __name__ == "__main__":
    search_arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    ret, tar = find(7, search_arr)
    print(ret, tar)
