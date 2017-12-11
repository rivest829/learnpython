# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import multiprocessing,threading
import time,os
print('dddddddddddddfatheris %s' % os.getppid())
print('ddddddddddddd%s'%os.getpid())

def run (name):
    time.sleep(0)
    for i in range(10):
        t=threading.Thread(target=threadtun,args=('%s====%s'%(name,i),))
        t.start()
def threadtun(name):
    time.sleep(0)
    print(os.getpid())
    print('fatheris %s' % os.getppid())
    print('my name is %s' % name)
    time.sleep(10)
if __name__=='__main__':
    for i in range(10):
        p1=multiprocessing.Process(target=run ,args=('chiang%s'%i,))
        p1.start()


