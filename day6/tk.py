# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import importlib
#mod=__import__('christ.jesus')
mod=importlib.import_module('christ.jesus')
print(mod)
Jesus=getattr(mod,'Jesus')
print(Jesus)
j1=Jesus('chiang')
print(j1)
j1.tellname()