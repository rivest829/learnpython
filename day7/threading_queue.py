# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import queue,time,threading,random
q=queue.Queue()
def Producer(name):
    print('ready to put')
    while True:
        q.put('%s put things'%name)
        print('搞了一个!')
        time.sleep(random.randrange(4))
def Consumer(name):
    print('ready to get')
    while True:
        time.sleep(random.randrange(4))
        if not q.empty():
            goods = q.get()
            print('%s got %s'%(name,goods))
p=threading.Thread(target=Producer,args=('chiang',))
c=threading.Thread(target=Consumer,args=('ching',))
p.start()
c.start()