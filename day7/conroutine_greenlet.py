# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
#gevent是greenlet的更高一层封装，greenlet只可以实现手动的协程切换
import time
from greenlet import greenlet
def func1():
    print('func1 start run...')
    f2.switch()
    time.sleep(1)
    print('func1 done!')
    f2.switch()
def func2():
    print('func2 start run...')
    f1.switch()
    time.sleep(2)
    print('func2 done!')


f1=greenlet(func1)
f2=greenlet(func2)
f1.switch()