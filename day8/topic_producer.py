# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pika

credenntial = pika.PlainCredentials('jiang', 'jiang123')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.226.129', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='topic_log', exchange_type='topic')

while True:
    msg = input('>>:')
    if not msg:
        print('input like this: [error/info] message')
    else:
        routing, msg = msg.split(' ')
        print(msg, routing)

    channel.basic_publish(exchange='topic_log', routing_key=routing, body=msg)
    print('[x]send %s' % msg)
