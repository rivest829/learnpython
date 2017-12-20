# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# 消息以轮询的方式分发到各个客户端上
import pika

credential = pika.PlainCredentials('jiang', 'jiang123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.226.129', port=5672, virtual_host='/', credentials=credential)
)
channel = connection.channel()
channel.exchange_declare(exchange='to_everyone', exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(queue=queue_name, exchange='to_everyone')


def callback(ch, method, properties, body):
    # print(' [x] recv --%s--' % body)
    pass


channel.basic_consume(callback, queue=queue_name, no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
