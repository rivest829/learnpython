# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
def logger():
    with open("log.txt","a") as f:
        f.write("end of the fucking work \n")

def t1():
    print("test1")
    logger()

def t2():
    print("test2")
    logger()

def t3():
    print("test3")
    logger()

t1()
t2()
t3()