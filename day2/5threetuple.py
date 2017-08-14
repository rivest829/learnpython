# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# info={
#     "guitar":"Du",
#     "bass":"Jiang",
#     'drum':'zhang'
#
# }
# print(info)
# print(info['bass'])
#
# print(info.values())
# print(info.keys())
#
# c=dict.fromkeys([1,2,3],['a','b','c'])
# print(c)
# c[1][0]='zz'
# print(c)
import time
dict={}
for i in range(0,100000):
    dict[i]=i+98
fun2_start = time.time()
for k, v in dict.items():
    print(k, v)
fun2_end = time.time()
fun1_start=time.time()
for i in dict:
    print(i,dict[i])

fun1_end=time.time()
fun1=fun1_end-fun1_start

fun2=fun2_end-fun2_start
print('第一次运行的时间：',fun1,'s')
print('第二次运行的时间：',fun2,'s')
