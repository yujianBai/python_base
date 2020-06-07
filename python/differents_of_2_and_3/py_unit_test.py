# auth Bernard
# date 2020-04-17

"""
python单元测试：
    Unit Testing
        针对程序模块进行正确性验证
        一个函数， 一个类进行验证
        自底向上保证程序的正确性

为什么要单元测试？
    三无代码不可取（无文档， 无注释， 无单侧）
        保证代码逻辑的正确性 (甚至有些采用测试驱动开发（TDD))
        单侧影响设计， 易测的代码往往是高内聚低耦合的
        回归测试， 防止改一处整个服务不可用


单元测试相关的库：
    nose/ pytest
    mock 模块用来模拟替换网络请求
    coverage 统计测试覆盖率
"""


def binary_search(array, target):
    if not array:
        return -1
    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            beg = mid + 1
    return -1


def test():
    """
    如何设计测试用例：
        正常值功能测试
        边界值 （比如最大最小， 嘴做最有值）
        异常值 （比如 None, 空值， 非法值）
    """
    assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], -1) == -1


if __name__ == "__main__":
    pass
