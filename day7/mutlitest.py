# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import multiprocessing,os

def son(d,count):
    d[count]=os.getpid()

if __name__=="__main__":
    manager = multiprocessing.Manager()
    d=manager.dict()
    p_list=[]

    for count in range(10):
        process=multiprocessing.Process(target=son,args=(d,count))
        process.start()
        p_list.append(process)

    for p in p_list:
        p.join()
    print(d)