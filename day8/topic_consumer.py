# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pika


def callback(ch, method, propertis, body):
    print(body)


credenntial = pika.PlainCredentials('jiang', 'jiang123')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.226.129', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='topic_log', exchange_type='topic')
while True:
    routing = input('>>:')
    if not routing:
        print('input [error or info]')
    queue_name = channel.queue_declare(exclusive=True)
    channel.queue_bind(queue=queue_name.method.queue, exchange='topic_log', routing_key=routing)
    channel.basic_consume(callback, queue=queue_name.method.queue)
    channel.start_consuming()
