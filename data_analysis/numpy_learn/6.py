#auth Bernard
#date 2021-05-09

import numpy as np

#numpy 在其他方面的应用
print("FFT")
print(np.fft.fft(np.array([1, 1, 1, 1, 1, 1, 1, 1])))

print("Coef:")
print(np.corrcoef([1, 0, 1],[0, 2, 1]))

print("Poly")
# print(np.polyld([2, 1, 3])) #?