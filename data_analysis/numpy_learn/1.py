# auth Bernard
# date 2021-04-22

import numpy as np


def main():
    lst = [[1, 3, 4], [2, 4, 6]]
    print(type(lst))

    np_lst = np.array(lst)
    print(type(np_lst))

    np_lst = np.array(lst, dtype=np.float)
    # bool, int, int8, int16, int32, int64, uint8, uint32, uint64, uint128,
    # float, float16, 32, 64, complex
    # complex 复数

    print('shape : ', np_lst.shape)
    print('ndim : ', np_lst.ndim)
    print('dtype : ', np_lst.dtype)
    print('itemsize : ', np_lst.itemsize)
    print('size : ', np_lst.size)

    print(np.zeros([2, 4]))  # 数值的初始化
    print(np.ones([3, 5]))
    print('Rand:')
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print('randint : ', np.random.randint(1, 10))

    print('Randn:')
    print(np.random.randn(2, 4))
    print("choice")
    print(np.random.choice([10, 20, 30]))  # 随机数只能在这几个书中选

    print('Distribute: ')
    print(np.random.beta(1, 10, 100)) # 贝塔分布




if __name__ == "__main__":
    main()
