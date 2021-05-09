# auth Bernard
# date 2021-05-09

import pandas as pd
import numpy as np
from pylab import *


def test():
    t_exam = pd.date_range('20170301', periods=10, freq='S')
    print(t_exam)

    ts = pd.Series(np.random.randn(1000), index=pd.date_range('20170301', periods=1000))
    ts = ts.cumsum()
    #
    ts.plot()
    show()

def test_file():
    # df1 = pd.read_csv('./data/test.csv')
    n = 5
    datas = pd.date_range("20170401", periods=n)
    df = pd.DataFrame(np.random.randn(n, 5), index=datas, columns=list("ABCDE"))

    df.to_csv('./data/test1.csv')


if __name__ == "__main__":
    # test()
    test_file()
