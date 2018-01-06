# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
from day8 import redis_middleware
import time
middleware=redis_middleware.RedisMiddleware()
while True:
    msg =time.time()
    time.sleep(2)
    middleware.publish(msg)