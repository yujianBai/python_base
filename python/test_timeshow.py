#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test_timeshow.py.py
@time: 2019/1/4 15:08
"""


if __name__ == "__main__":
    stop_time = 1.27

    stopping_time_h = int(stop_time)
    stopping_time_m = int((stop_time - stopping_time_h) * 60)
    stopping_time_s = int(stop_time * 3600 - stopping_time_h * 3600- stopping_time_m * 60)

    print "stop_time %d时%d分%d秒"%(stopping_time_h, stopping_time_m, stopping_time_s)

    if stopping_time_s>0:
        stopping_time_m += 1
    print "stop_time %d时%d分"%(stopping_time_h, stopping_time_m)

    print "method 2"
    stop_time_sec = stop_time * 3600
    stopping_time_h = int(stop_time_sec / 3600)
    stopping_time_m = int(stop_time_sec % 3600 / 60)
    stopping_time_s = stop_time_sec % 3660 % 60
    print "stop_time %d时%d分%d秒"%(stopping_time_h, stopping_time_m, stopping_time_s)

    from datetime import datetime
    now = datetime.now()
    print now
    fmt_str = "%Y-%m-%d %H:%M:%S"
    now_str = now.strftime(fmt_str)
    print now_str
    print type(datetime.strptime(now_str, fmt_str))




