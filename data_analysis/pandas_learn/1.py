# auth Bernard
# date 2021-05-09

import numpy as np
import pandas as pd


def main():
    s = pd.Series([i * 2 for i in range(1, 11)])
    print(type(s))
    n = 5
    datas = pd.date_range("20170401", periods=n)
    df = pd.DataFrame(np.random.randn(n, 5), index=datas, columns=list("ABCDE"))
    print(df)


if __name__ == '__main__':
    main()
