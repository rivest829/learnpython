# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import redis, time

start_time = time.time()
r = redis.Redis(host='192.168.226.129', port=6379)
l1 = []
for i in range(10000):
    r.set(i, 'jiang' + str(i))
print(time.time() - start_time)
