# -*- coding: utf-8 -*-
# @Time    : 19-5-9 下午9:36
# @Author  : Baiyj

# @File    : urllib_test


'''
httpbin.org
搭建自己的httpbin.org
    python包：    pip install gunicorn httpbin
    gunicorn服务器安装： apt-get install gunicorn

    我使用的是 pipenv 中启动gunicron 的时候，提示我的真实python 环境中没有httpbin包。
    但是教程中使用的是Virtualenv 就可顺利启动。说明 pipenv 和 virturalenv 在有些方面还是有区别的。

curl -v http://www.baidu.com > tem.txt

'''
import urllib2
import urllib

import requests

URL_IP = "http://127.0.0.1:8000/ip"
URL_GET = "http://127.0.0.1:8000/get"

def use_simple_urllib2():
    response = requests.get(URL_IP)
    print ">>>>> Response Headers:"
    print response.headers
    print ">>>> Response Body"
    print response.text

def use_para_urllib2():
    params = {"param1":'hello', "param2":'world'}
    response = requests.get(URL_GET, params = params)
    print "Request Params:"
    print ">>>> Response Headers:"
    print response.headers
    print ">>>> Response Body"
    # print response.text
    print response.json()
    print ">>>> Status code"
    print response.status_code
'''
headers 的 'Connection': u'keep-alive' ，保持链接可以消耗更少的资源

数据交换标准
ifc 的7230 ～7235条款 
'''

if __name__ == "__main__":
    # print ">>>> Use simple urllib2:"
    # use_simple_urllib2()

    print ">>>> Use simple use_para_urllib2"
    use_para_urllib2()
