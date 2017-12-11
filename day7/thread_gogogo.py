# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import threading,time

class MyThread(threading.Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.name=name
    def run(self):
        time.sleep(0.7)
        print('fuck %s' % self.name)
        print('thread is %s'%threading.current_thread(),'+++===+++',threading.active_count())
start_time=time.time()

t_objs=[]
for i in range(5000):
    t=MyThread('chiang %s' %i)
    t.setDaemon(True)
    t.start()
    t_objs.append(t)
# for t in t_objs:
#     t.join()
print('cost:',time.time()-start_time)
print('thread is %s'%threading.current_thread())