#coding:utf-8

import datetime


def test_timeformat():
    s_time = "2019-01-21 11:36:42"
    e_time = "2019-01-21 12:06:16"

    print datetime.datetime.now()
    format = "%Y-%m-%d %H:%M:%S"
    start_time = datetime.datetime.strptime(s_time, format)
    end_time = datetime.datetime.strptime(e_time, format)
    print start_time
    print end_time
    stop_time = end_time - start_time
    print stop_time.seconds
    print stop_time

if __name__ == "__main__":
    test_timeformat()
