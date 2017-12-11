# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import threading,time,random
def cat(name):
    while True:
        time.sleep(random.randrange(3))
        if event.is_set():
            print("%s gogo"%name)
        else:
            print("%s stop"%name)
def light():
    if not event.is_set():
        event.set()
    count=0
    while True:
        if count<10:
            pass
        elif count >=10 and count<20:
            if event.is_set():
                event.clear()
        else:
            count=0
            event.set()
        print(count)
        count+=1
        time.sleep(1)

if __name__=='__main__':
    event=threading.Event()
    thread1=threading.Thread(target=light)
    thread1.start()
    for i in range(4):
        thread_car=threading.Thread(target=cat,args=(i,))
        thread_car.start()