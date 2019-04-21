# -*- coding: utf-8 -*-
# @Time    : 19-4-21 下午10:45
# @Author  : Baiyj

# @File    : test_flask_wsgi
import threading
import time

import requests


def test():

    r = requests.get('http://127.0.0.1:10080', data = '%s'%time.time())
    print r.text
    print r.status_code


if __name__ == "__main__":
    while 1:
        threadlist = []
        for i in range(0, 9):
            t = threading.Thread(target=test)
            threadlist.append(t)

        for t in threadlist:
            t.start()
            print "start threading test"
            t.join(timeout=2)

        time.sleep(2)

