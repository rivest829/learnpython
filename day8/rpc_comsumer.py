# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,#收到消息就会调用on_response()
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:#校验返回的UUID与发出去的UUID是否一致
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc5_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,#定义服务器返回时使用的queue，就是在14行生产的随机queue
                                       correlation_id=self.corr_id,#发送通用唯一识别码
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()#非阻塞版本的start_comsuming
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()
for i in range(100):
    print(" [x] Requesting fib(%s)"%i)
    response = fibonacci_rpc.call(i)
    print(" [.] Got %r" % response)