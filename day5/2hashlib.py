# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import hashlib
import hmac
a=hashlib.md5()
a.update(b'hello')
print(a.hexdigest())
a2=hashlib.sha512()
a2.update(b'wokao')
print(a2.hexdigest())


h=hmac.new(b'gibson',b'very good')
print(h.hexdigest())
print(h.digest())