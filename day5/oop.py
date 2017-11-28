# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
class A(object):
    def __init__(self, name):
        self.name = name

    def go(self):
        print(self.name)


class Son(A):
    def __init__(self, name, age):
        super(Son,self).__init__(name)
        self.age=age
    def tell(self):
        print('%s is %s yeas old' % (self.name, self.age))


a1 = A('chiang')
a1.go()
s1=Son('shuang','8')
s1.tell()