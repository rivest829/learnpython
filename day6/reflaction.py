# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
class Reflaction(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ss(self):
        print('i m fucking %s'%self.name)

    def __getattr__(self, item):
        self.item()
r1=Reflaction('chiang',24)


choice=input('what you want?:')
if hasattr(r1,choice):
    getattr(r1,choice)()