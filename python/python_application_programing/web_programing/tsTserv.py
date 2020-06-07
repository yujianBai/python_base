#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建套接字
"""
socket()函数两个参数， 第一个参数，socket_family； 第二个参数socket_type

为了创建TCP套接字， 必须使用SOCK_STREAM，基于流套接字的表示， AF_INET:表示套接字的网络版本,基于IP寻找主机
创建UDP套接字，使用SOCK_DGRAM作为套接字类型，使用AF_INET作为协议族，构成 udp/ip 协议
"""

tcpSerSock.bind(ADDR)  # 套接字和地址绑定
tcpSerSock.listen(5)   # 监听链接

while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()  # 接收客户端链接
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)  # 接收客户端消息
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))  #发送客户端消息

    tcpCliSock.close()   # 关闭客户端套接字
tcpSerSock.close()    # 关闭服务器套接字
