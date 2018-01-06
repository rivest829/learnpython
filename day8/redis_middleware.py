# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import redis
class RedisMiddleware:
    def __init__(self):
        self.__connection=redis.Redis(host='192.168.226.129',port=6379)
        self.publish_channel='elwynn'
        self.subscribe_channel='elwynn'
    def publish(self,msg):
        self.__connection.publish(self.publish_channel,msg)
        return True
    def subscribe(self):
        sub=self.__connection.pubsub()
        sub.subscribe(self.subscribe_channel)
        sub.parse_response()
        return sub


