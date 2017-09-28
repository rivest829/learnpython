# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import time
def timer():
    time_format="%X"
    time_current=time.strftime(time_format)
    return time_current
def runner():
    x=456434*94434/64+4534354-5645
    print(x)
    return  timer()

def while_in_one_second():
    count = 0
    while start_time == runner():
        count = count + 1
        print(count)

start_time=timer()
while_in_one_second()