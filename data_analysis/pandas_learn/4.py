#auth Bernard
#date 2021-05-09

import numpy as np
import pandas as pd


def main():
    n = 5
    datas = pd.date_range("20170401", periods=n)
    df = pd.DataFrame(np.random.randn(n, 5), index=datas, columns=list("ABCDE"))

    df1 = df.reindex(index=datas[:4], columns=list('ABCD') + ['G'])
    df1.loc[datas[0]:datas[1], 'G'] = 1
    df1 = df1.fillna(value=2)
    print(df1)

    # Staticstic
    print('df.mean')
    print(df.mean())
    print('df.var 方差')
    print(df.var())


if __name__ == "__main__":
    main()