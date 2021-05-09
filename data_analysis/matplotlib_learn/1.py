#auth Bernard
#date 2021-05-09


# Line

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c, s = np.cos(x), np.sin(x)

plt.figure(1)
plt.plot(x, c, color='yellow', linewidth=1.0, linestyle='-', label='COS', alpha=0.5)
plt.plot(x, s, color='green', label='sin', linestyle=':')
plt.title('cos & sin')


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.xticks([])



plt.show()
