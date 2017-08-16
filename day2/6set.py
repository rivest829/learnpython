# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
list1=[1,3,5,3,7,8,9]
list2=[2,4,6,4,7,11,6]
set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.issubset(set2))
print(set([2,6]).issubset(set2))
print(set2.issuperset(set([2,6])))
print(set1.isdisjoint(set2))
print(type(set2))