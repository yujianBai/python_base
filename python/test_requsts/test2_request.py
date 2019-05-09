#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: test_request.py
@time: 2019/4/19 18:20
"""
import time

import requests


def get_data_from_webserver():
    r = requests.get('http://localhost:10080/api/waiting_hall_msg')
    print(r)

if __name__ == "__main__":
    while True:
        # time.sleep(1)
        try:
            get_data_from_webserver()
        except Exception as error:
            print error