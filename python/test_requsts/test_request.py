#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test_request.py
@time: 2019/4/19 18:20
"""
import requests


def get_data_from_webserver():
    r = requests.get('http://121.199.49.228:13668/api/get_real_time_data')
    print(r)

if __name__ == "__main__":
    get_data_from_webserver()