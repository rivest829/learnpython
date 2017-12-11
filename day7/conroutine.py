# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
#使用gevent实现的自动切换，使用协程实现了并发的效果
import gevent
def func1():
    print('func1 gogogo')
    gevent.sleep(1)
    print('func1 done')
def func2():
    print('func2 gogogo')
    gevent.sleep(2)
    print('func2 done')
def func3():
    print('func3 gogogo')
    gevent.sleep(1.5)
    print('func3 done')
gevent.joinall([
    gevent.spawn(func1),#注意此处函数是通过参数的方式传给spawn方法的，不可以加括号
    gevent.spawn(func2),
    gevent.spawn(func3),
])
