# -*- coding:utf-8 -*-
""" 
@author: baiyj
@file: thread_learn.py.py
@time: 2019/2/11 11:11
"""

import threading


class mythread(threading.Thread):
    def __init__(self, arg):
        threading.Thread.__init__(self, name='my name' + str(arg))
        self.arg = arg

    def run(self):
        print("am in " + str(self.arg) + "\n")


def like_mythread(arg):
    print("am in " + str(arg) + "\n")


if __name__ == "__main__":

    t = threading.Thread(target=like_mythread, name="my name", args=("3"))
    print(t.name + "\n")
    t.start()
    t.join()

    thread_list = []
    for i in range(2):
        myTH = mythread(i)
        thread_list.append(myTH)

    for item in thread_list:
        item.start()
        print (item.name)

    for item in thread_list:
        item.join()
