# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import time
def cosumer(name):
    name=name
    while True:
        note=yield
        print('%s play the %s note' %(name,note))
def producer(song):
    print('now , its time to play the %s' %song)
    c1=cosumer('ji')
    c2=cosumer('du')
    c1.__next__()
    c2.__next__()
    for i in range(10):
        c1.send('A'+str(i))
        c2.send('F'+str(i))
        time.sleep(1)

producer('money bussiness')