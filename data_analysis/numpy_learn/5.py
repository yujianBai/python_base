# auth Bernard
# date 2021-05-09

'''
线性方程组 矩阵操作

'''

import numpy as np
from numpy.linalg import *

print(np.eye(3))

lst = np.array([
    [1, 2],
    [3, 4]
])

print("原本的矩阵")
print(lst)

print("Inv:")
print(inv(lst))

print("T:")
print(lst.transpose())

print("Det")
print(det(lst))

print(eig(lst))

y = np.array([[5.], [7.]])
print("Solve")
print(solve(lst, y)) # what happen?
