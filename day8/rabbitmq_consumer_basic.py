# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# 消息以轮询的方式分发到各个客户端上
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.226.129')
)
channel = connection.channel()
channel.queue_declare(queue='jiang_queue')


def callback(ch, method, properties, body):
    print(' [x] recv --%s--' % body)


channel.basic_consume(callback, queue='jiang_queue', no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
