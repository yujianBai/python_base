# auth Bernard
# date 2020-04-20

import socket

s = socket.socket()
s.connect(("www.baidu.com", 80))

http = b"GET / HTTP/1.1\r\nHOST: www.baidu.com\r\n\r\n"
s.sendall(http)
bufs = []
buf = s.recv(2048)

while buf:
    bufs.append(buf)
    buf = s.recv(2048)
print(bufs)
s.close()
