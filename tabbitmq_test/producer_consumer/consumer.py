# auth Bernard
# date 2020-05-09
import pika

HOST = '127.0.0.1'
PORT = 5672

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST, port=PORT, virtual_host='/', credentials=credentials))

channel = connection.channel()
# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue='python-test', durable=False)


# 推模式

# # 定义一个回调函数来处理消息队列中的消息，这里是打印出来
# def callback(ch, method, properties, body):
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#     print(body.decode())
#
#
# # 告诉rabbitmq，用callback来接收消息
# channel.basic_consume('python-test', callback)
#
# # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
# channel.start_consuming()


# 拉模式, 返回一次， 确认一次

# 这里的代码 一次只能获取一条消息
method_frame, header_frame, body = channel.basic_get('python-test')
if method_frame:
    print(method_frame, header_frame, body)
    channel.basic_ack(method_frame.delivery_tag)
else:
    print('No message returned')

