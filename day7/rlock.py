# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
#递归锁
import threading
def run1():
    global num
    lock.acquire()
    num+=1
    lock.release()
    print(num)

lock=threading.Lock()

