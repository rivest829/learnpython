# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import redis, time


pool = redis.ConnectionPool(host='192.168.226.129', port=6379)
connection=redis.Redis(connection_pool=pool)
pipe=connection.pipeline(transaction=True)

pipe_start_time = time.time()
for i in range(10000):
    pipe.set(i, 'jiang%s'%i)
pipe.execute()
print('Pipe time:%s'%(time.time() - pipe_start_time))


pool_start_time=time.time()
for i in range(10000):
    connection.set(i+10000, 'jing%s' %(i+10000))
print('Pool time:%s'%(time.time()-pool_start_time))