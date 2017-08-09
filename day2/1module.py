# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
'''
import sys
print(sys.path)#环境变量
print(sys.argv)#此脚本路径
'''
import os
res=os.popen('dir')
print(res.read())
os.system('cd ..')