# auth Bernard
# date 2021-05-09


import numpy as np
import pandas as pd


def main():
    n = 5
    datas = pd.date_range("20170401", periods=n)
    df = pd.DataFrame(np.random.randn(n, 5), index=datas, columns=list("ABCDE"))
    # print(df)
    print('head')
    print(df.head(3))

    print('tail')
    print(df.tail(3))

    print('index')
    print(df.index)

    print('values')
    print(df.values)
    print('T')
    print(df.T)
    print('sort C')
    # print(df.sort(columns='C')) ? 方法不存在
    print(df.sort_index(axis=1, ascending=False))
    print(df.describe())

    # select
    print('select')
    print(df['A'])
    print(df[:3])
    print('切片', df['20170401':'20170403'])

    print('get data df.loc')
    print(df.loc[datas[0]])
    print('get data df.loc : ')
    print(df.loc['20170401':'20170403', ['B', 'C']])

    print(df.at[datas[0], 'C'])

    print('下标选择')
    print(df.iloc[1:3, 2:4])
    print(df.iloc[1, 4])

    print('大于小于选择')
    # print(df[df.B > 0][df.A < 0])
    print(df[df>0])

    # Set
    s1 = pd.Series(list(range(10, 18)), index=pd.date_range('20170401', periods=8))
    df['F']=s1
    print('set')
    print(df)

    df.at[datas[0], 'A'] = 0
    print(df)

    df.iat[1, 1]=1
    print(df)

    df.loc[:,'D']=np.array([4]*len(df))
    print(df)

    df2 = df.copy()
    df2[df2>0] = -df2
    print(df2)

if __name__ == "__main__":
    main()
