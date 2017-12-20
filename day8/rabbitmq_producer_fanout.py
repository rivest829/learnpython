# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# 消息以轮询的方式分发到各个客户端上
import pika, time

start_time = time.time()
credential = pika.PlainCredentials('jiang', 'jiang123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.226.129', port=5672, virtual_host='/', credentials=credential)
)
channel = connection.channel()
channel.exchange_declare(exchange='to_everyone', exchange_type='fanout')

for i in range(10000):
    msg = str(i)
    # msg = input('>>:') + str(time.time())
    channel.basic_publish(exchange='to_everyone',
                          routing_key='',
                          body=msg,
                          )
    # print(' [x] Sent --%s--' % msg)
connection.close()
print(time.time() - start_time)
