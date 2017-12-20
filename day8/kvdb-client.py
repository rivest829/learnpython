# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import redis, time

start_time = time.time()
redis_pool=redis.ConnectionPool(host='192.168.226.129',port=6379)
r = redis.Redis(connection_pool=redis_pool)
for i in range(10000):

    r.get(i)
print(time.time() - start_time)
