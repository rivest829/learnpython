# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# 消息以轮询的方式分发到各个客户端上
import pika, time

credentials = pika.PlainCredentials('jiang', 'jiang123')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.226.129', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='jiang_queue')
while True:
    msg = input('>>:') + str(time.time())
    channel.basic_publish(exchange='',
                          routing_key='jiang_queue',
                          properties=pika.BasicProperties(
                              delivery_mode=1
                          ),
                          body=msg,
                          )
    print(' [x] Sent --%s--' % msg)
connection.close()
