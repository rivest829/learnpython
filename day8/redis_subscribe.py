# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
from day8 import redis_middleware
import time
middle=redis_middleware.RedisMiddleware()
sub=middle.subscribe()
while True:
    msg = sub.parse_response(block=False)#非阻塞
    time.sleep(0.5)
    if msg is not None:
        print(msg[-1])
    else:
        print('NONE')