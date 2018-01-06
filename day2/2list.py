# -*- coding:utf-8 -*-
# Author Hsinhan
list1 = ['led zeppelin','nightwish',['tilo woldof','drumer'],'beyond',['manson','john5']]
def printer(list1):
    for i in list1:
        if type(i)==None:
            printer(i)
        else:
            print(i)
printer(list1)
print(list1[-1])