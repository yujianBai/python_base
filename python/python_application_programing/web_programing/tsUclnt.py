#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    # print("data str is :{}".format(data))
    if not data:
        break
    # udpCliSock.sendto(data, ADDR)
    udpCliSock.sendto(bytes(data,"utf-8"), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print("receive from server data is :{}".format(data))

udpCliSock.close()
