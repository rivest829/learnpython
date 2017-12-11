# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
#使用yield实现并发
import time
def consumer(name,sleeptime):

    while True:
        call=yield
        time.sleep(sleeptime)
        print('%s is done by %s'%(call,name))
def producer(name):
    r=c1.__next__()
    r=c2.__next__()
    print('r is %s'%r)
    while True:
        call=input(">>:")
        c1.send(call)
        print('%s send %s' % (name, call))
        c2.send(call)

if __name__=='__main__':
    c1=consumer('chiang',1)
    c2=consumer('ching',2)
    p=producer('anti')
#不是真正的并发，不能在阻塞的时候进行切换。