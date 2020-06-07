# auth Bernard
# date 2020-04-18

"""
算法常考题：
    排序+ 查找
    冒泡， 快速， 归并， 堆排序
    线性查找， 二分查找
    能独立实现代码， 能够分析时间空间复杂度
"""

"""
常用排序算法的时空复杂度

排序算法       最差时间分析       平均时间分析      稳定度     空间复杂度

冒泡排序        O(n^2)           O(n^2)        稳定         O(1)

选择排序        O(n^2)           O(n^2)        不稳定       O(1)

插入排序        O(n^2)           O(n^2)        稳定         O(1)

快速排序        O(n^2)         O(n*log2n)      不稳定       O(log2n)~O(n)

堆排序         O(n*log2n)      O(n*log2n)     不稳定        O(1)


排序算法中的稳定性
    相同大小的元素在排序之后依然保持相对位置不变， 就是稳定的
    r[i] = r[j] 且 r[i]在r[j]之前， 排序之后r[i]依然在r[j]之前
    稳定性对于排序一个复杂结构， 并且需要保持原有排序才有意义 
"""


# 快排 分治法，快排三步走
# Partition: 选择基准分割数组为两个子数组， 小于基准和大于基准的
# 对连个子数组分别快排
# 合并结果

def quicksort(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        pivot_index = 0  # 第一个元素作为主元
        pivot = array[pivot_index]
        less_part = [item for item in array[pivot_index + 1:] if item <= pivot]
        great_part = [item for item in array[pivot_index + 1:] if item > pivot]
        return quicksort(less_part) + [pivot] + quicksort(great_part)


# def quicksort_reverse(array):
#     # 递归出口
#     if len(array) < 2:
#         return array
#     else:
#         pivot_index = 0  # 第一个元素作为主元
#         pivot = array[pivot_index]
#         less_part = [item for item in array[pivot_index + 1:] if item <= pivot]
#         great_part = [item for item in array[pivot_index + 1:] if item > pivot]
#         return quicksort(great_part) + [pivot] + quicksort(less_part)


def test_quict_sort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(quicksort(ll))
    print(quicksort_reverse(ll))

    # assert quicksort(ll) == sorted(ll)
    # print(ll)
    # assert quicksort_reverse(ll) == sorted(ll, reverse=True)


def merge_sorted_list(sorted_a, sorted_b):
    # 归并排序， 合并两组有序数组
    len_a, len_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = []

    while a < len_a and b < len_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < len_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq


def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left_half = binary_sorted(array[:mid])
        right_half = binary_sorted(array[mid:])
        return merge_sorted_list(left_half, right_half)


# 短时间实现堆排序
def heapsort_user_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]


# 二分查找, 查找的是一个有序的数组
def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    beg = 0
    end = len(sorted_array) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            mid = mid - 1
        else:
            beg = mid + 1
    return -1


# 二分查找， 递归
def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = (beg + end) // 2
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search(sorted_array, beg, mid, val)
    else:
        return binary_search_recursive(sorted_array, mid+1, end, val)


if __name__ == "__main__":
    # test_quict_sort()
    # print(merge_sorted_list([1, 3, 6, 8], [2, 4, 5, 7, 9]))
    print(mergesort([4, 7, 8, 0, 2, 3]))
