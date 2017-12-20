# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='error_log',
                         exchange_type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
serverity = input(">>:")

channel.queue_bind(queue=queue_name,
                   exchange='error_log',
                   routing_key=serverity)


def callback(ch, method, properties, body):
    print('[%s]:%s' % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
