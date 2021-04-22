# auth Bernard
# date 2021-04-22
import numpy  as np


def main():
    # array
    print(np.arange(1, 11))

    lst = np.arange(1, 11).reshape([2, 5])

    print('\nlst:\n ', lst)
    print('\nnp.exp(lst):\n', np.exp(lst))
    print('\nnp.exp2(lst):\n', np.exp2(lst))
    print('\nnp.sqrt(lst):\n', np.sqrt(lst))
    print('\nnp.sin(lst):\n', np.sin(lst))
    print('\nnp.log(lst):\n', np.log(lst))

    lst = np.array([
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[9, 10, 11, 12], [13, 14, 15, 16]],
        [[17, 18, 19, 20], [21, 22, 23, 24]],
    ])

    print('\nlst.sum axis=0: \n', lst.sum(axis=0))
    print('\nlst.sum axis=1: \n', lst.sum(axis=1))
    print('\nlst.sum axis=2: \n', lst.sum(axis=2))  # axis 深入中括号的程度不一
    print('\nlst.sum : \n', lst.sum())

    print('Max:')
    print('\nmax lst axis=0\n', lst.max(axis=0))
    print('\nmax lst axis=1\n', lst.max(axis=1))
    print('\nmax lst axis=2\n', lst.max(axis=2))

    l1 = np.array([1, 2, 3, 4])
    l2 = np.array([5, 6, 7, 8])
    print('l1 + l2: ', l1 + l2)
    print('l1 - l2: ', l1 - l2)
    print('l1 * l2: ', l1 * l2)
    print('l1 / l2: ', l1 / l2)

    print("\nDot\n")
    print(l1.reshape([2, 2]))
    print(l2.reshape([2, 2]))
    print(np.dot(l1.reshape([2, 2]), l2.reshape([2, 2]))) # ? Dot

    print("\nCancatenate\n")
    print(np.concatenate((l1, l2), axis=0))
    print("\nv h stack\n")
    print(np.vstack((l1, l2)))
    print(np.hstack((l1, l2)))
    print('\nsplit:\n')
    print(np.split(l1, 4))
    print(np.split(l1, 2))

if __name__ == "__main__":
    main()
