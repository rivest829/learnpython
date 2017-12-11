# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import threading,time

num=0
t_objs=[]

def demo():
    lock.acquire()
    global num
    time.sleep(0.8)
    num+=1
    lock.release()
lock=threading.Lock()
for i in range(1000):
    t=threading.Thread(target=demo)
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print('num is ',num)