#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print ('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    # udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'), addr)  # python3 这里需要bytes类型的数据
    print ('...received from and returned to:', addr)

udpSerSock.close()
