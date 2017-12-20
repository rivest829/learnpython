# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='error_log', exchange_type='direct')
while True:
    log = input('>>:')
    if len(log) > 3:
        severity = 'error'
    elif log == 'q':
        break
    else:
        severity = 'info'
    channel.basic_publish(exchange='error_log', routing_key=severity, body=log)
    print('Send %s' % log)

connection.close()
