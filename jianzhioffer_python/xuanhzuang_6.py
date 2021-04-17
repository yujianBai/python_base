# auth Bernard
# date 2020-06-08

'''
6.旋转数组的最小数字  // 其实就是查找数组的最小数字, 和旋不旋转没关系

//旋转数组， 即不是一个有序的数组

Q: 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

A1: 遍历数组；
A2: 二分查找的变形，旋转数组的首元素肯定不小于旋转数组的尾元素，找一个中间点，如果中间点比首元素大，
说明最小数字在中间点后面，如果中间点比尾元素小，说明最小数字在中间点前面。然后循环。
但是在一次循环中，首元素小于尾元素，说明该数组是排序的，首元素就是最小数字，
如果出现首元素、尾元素、中间值三者相等，则只能在此区域中顺序查找。
'''


def answer(rotateArrey):
    if len(rotateArrey) == 0:
        return 0
    result = rotateArrey[0]
    for num in rotateArrey:
        if num < result:
            result = num
    return result


def answer2(rotateArrey):
    if len(rotateArrey) == 0:
        return 0
    left, right = 0, len(rotateArrey) - 1
    if rotateArrey[left] < rotateArrey[right]:
        return rotateArrey[left]
    else:
        while (right - left) > 1:
            middle = (right + left) // 2
            if rotateArrey[middle] <= rotateArrey[right]:
                right = middle
            elif rotateArrey[middle] >= rotateArrey[left]:
                left = middle
            elif rotateArrey[middle] == rotateArrey[left] == rotateArrey[right]:
                minval = rotateArrey[0]
                for num in rotateArrey:
                    minval = min(minval, num)
                return minval
    return rotateArrey[right]

def binary_search(target, array):
    if len(array) == 0:
        return []
    left, right = 0, len(array) -1
    while left <= right:
        middle = (left + right)//2
        if target < array[middle]:
            right = middle
        elif target > array[middle]:
            left = middle
        elif target == array[middle]:
            return middle
        else:
            return None





if __name__ == "__main__":
    # print(answer([1, 2, 3, 4, 5]))
    # print(answer([3, 4, 5, 1, 2]))
    # print(answer2([3, 4, 5, 1, 2]))
    print(binary_search(4, [1, 2, 3, 4, 6, 7]))
    print(binary_search(6, [1, 2, 3, 4, 6, 7]))
