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

URL_IP = "http://127.0.0.1:8000/ip"
URL_GET = "http://127.0.0.1:8000/get"

def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print ">>>>> Response Headers:"
    print response.info()
    print ">>>> Response Body"
    print ''.join([line for line in response.readlines()])

def use_para_urllib2():
    params = urllib.urlencode({"param1":'hello', "param2":'world'})
    print "Request Params:"
    print params
    response = urllib2.urlopen('?'.join([URL_GET, '%s'])%params)
    print ">>>> Response Headers:"
    print response.info()
    print ">>>> Response Body"
    print ''.join([line for line in response.readlines()])
    print ">>>> Status code"
    print response.getcode()


if __name__ == "__main__":
    # print ">>>> Use simple urllib2:"
    # use_simple_urllib2()

    print ">>>> Use simple use_para_urllib2"
    use_para_urllib2()
