# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import time

def runner():
    x=456434*94434/64+4534354-5645
    with open("pcRun.txt","w") as f :#加入骚写硬盘，速度明显下降
        f.write(str(x)+"\n")

def tes():
    start=time.time()
    for i in range(8000):
        runner()
    end=time.time()
    return "cost time is %s" %(end-start)
print(tes())