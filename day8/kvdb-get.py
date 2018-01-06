# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import redis, time

start_time = time.time()
redis_pool=redis.ConnectionPool(host='192.168.226.129',port=6379)
pool = redis.Redis(connection_pool=redis_pool)
pipe=pool.pipeline(transaction=True)
for i in range(20000):
    pipe.get(i)
for i in pipe.execute():
    print(i)

print(time.time() - start_time)