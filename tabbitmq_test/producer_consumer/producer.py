# auth Bernard
# date 2020-05-09

import pika
import json
import time

HOST = '127.0.0.1'
PORT = 5672

def produce1():
    # credentials = pika.PlainCredentials('shampoo', '123456')  # mq用户名和密码
    credentials = pika.PlainCredentials('guest', 'guest')  # mq用户名和密码

    # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT, virtual_host='/', credentials=credentials))

    channel = connection.channel()
    # 声明消息队列，消息将在这个队列传递，如不存在，则创建

    result = channel.queue_declare(queue='python-test') # 基于TCP之上的channel
    result1 = channel.queue_declare(queue='python-test1') # 基于TCP之上的channel

    for i in range(10):
        message = json.dumps({'OrderId': "1000%s" % i})
        # 向队列插入数值 routing_key是队列名
        channel.basic_publish(exchange='', routing_key='python-test', body=message)
        print(message)

    channel.basic_publish(exchange='', routing_key='python-test1', body=json.dumps({'message':'0001'}))

    connection.close()




def producer2():
    '''
    mq 队列创建步骤：
    '''
    try:
        auth = pika.PlainCredentials('guest', 'guest')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=HOST, port=PORT, credentials=auth))
        # # 四个参数分别是  BrokerIP  BrokerPort, Vhost, username_and_password, 心跳时间间隔
        # parameter = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials, heartbeat_interval=0)
        channel = connection.channel()

        channel.queue_declare(queue='TEST01')

        channel.basic_publish(exchange='', routing_key='TEST01', body='Hello World!')

        print(" [x] Sent 'Hello World!'")
        connection.close()
    except Exception as error:
        print("error:{}".format(error))

if __name__ == "__main__":
    produce1()