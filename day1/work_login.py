# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import io, os, getpass

userlist = open(r'E:\learnpython\day1\userlist.txt', 'r')
userdenyr = open(r'E:\learnpython\day1\userdeny.txt', 'r')
userdenyw = open(r'E:\learnpython\day1\userdeny.txt', 'w')
flag = True
name = input('Please input your name:')
for deny in userdenyr:
    if name == deny:
        flag = False
for n in userlist:
    if name+'\n' == n and flag:
        print('Login successd!')
        break
else:
    userdenyw.write(name+'\r\n')