#-*- coding:utf-8 -*-
""" 
@author: baiyj
@file: while_test.py.py
@time: 2019/2/13 14:37
"""
import time

def main():
    while True:
        try:
            print "1"
            raise Exception("get an error")
            print "do some things"
            exit(0)
        except Exception as error:
            print error
            time.sleep(5)

if __name__ == "__main__":
    main()