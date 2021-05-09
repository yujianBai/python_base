# auth Bernard
# date 2021-05-09

import numpy as np
import pandas as pd


def main():
    n = 5
    datas = pd.date_range("20170401", periods=n)
    df = pd.DataFrame(np.random.randn(n, 5), index=datas, columns=list("ABCDE"))

    df1 = df.reindex(index=datas[:4], columns=list('ABCD') + ['G'])
    df1.loc[datas[0]:datas[1], 'G'] = 1
    print(df1)

    # 处理缺失值
    print('丢弃')
    print(df1.dropna())

    print('填充')
    print(df1.fillna(value=2))




if __name__ == "__main__":
    main()
