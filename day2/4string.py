# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
# 把玩一些字符串方法
name = "hsin han {family_name},i'm fucking {age}"
print(name.encode())
print(name.endswith('chiang'))
print(name.find('s'))
print(name.format_map({'family_name':'chiang','age':24}))
print(name.format(family_name = 'chiang',age=24))
print(name.isidentifier())#是否为合法标识符m
print('damn'.join('==='))
print(name.title())