# -*- coding:utf-8 -*-

# Author Hsinhan Chiang
import sys
import time
for i in range(500):
    if i%50 == 0:
        sys.stdout.write('\r\n')
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)