#auth Bernard
#date 2020-04-20

import socket
import time

ss = socket.socket()
s.bind('', 8888)
s.listen()

while True:
    client, addr = s.accept()
    print(client, addr)
    timestr = time.ctime(time.time()) + "\r\n"
    client.sent(timestr.encode())  # 默认编码为 utf-8
    client.close()

