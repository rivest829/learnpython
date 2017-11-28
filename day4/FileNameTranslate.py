# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import zipfile
flag=zipfile.ZipFile('prd.zip')
for item in flag.namelist():
    tag=item.split('.')[0]
    if tag.endswith('-uat') :
        print(item,item.replace('-uat',''))
        print(type(item))
    elif tag.endswith('-sit'):
        print(item, item.replace('-sit', ''))
    elif  tag.endswith('-uat3'):
        print(item, item.replace('-uat3', ''))
    else:
        pass
        #print(item, item)