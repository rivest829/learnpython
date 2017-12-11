# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import multiprocessing,time,os
def func(count):
    time.sleep(1)
    print(count)
    return count+10000

def bar(sb):
    print('call fucking back',sb,os.getppid())

if __name__=='__main__':
    print(os.getppid())
    pool=multiprocessing.Pool(5)
    for p in range(10):
        #pool.apply(func=func,args=(p,))#串行
        pool.apply_async(func=func,args=(p,),callback=bar)#并行


    pool.close()
    pool.join()