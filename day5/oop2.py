# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
class Attr(object):
    def __init__(self):
        self.at={}
    def __getitem__(self, key):
        print('__getitem__', key)
        return self.at.get(key)
    def __setitem__(self, key, value):
        self.at[key]=value

class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value
#test

a=Attr()
a['jiang']='jing'
print(a['jiang'])

a=Foo()
a['jiang']='jing'
print(a['jiang'])
print(type(type))