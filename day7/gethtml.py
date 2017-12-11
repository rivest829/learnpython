# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
#同步爬取网页与异步爬取网页，在时间上截然不同。异步爬取的耗时只和耗时最长的有关
from urllib.request import urlopen
import gevent.monkey,gevent,time

gevent.monkey.patch_all()

def gethtml(name,url):
    start_time=time.time()
    html = urlopen(url)
    f=open(name+'.html','wb')
    f.write(html.read())
    single_time=time.time()-start_time
    print(single_time)

async_start_time=time.time()
gevent.joinall([
    gevent.spawn(gethtml,'python','https://www.python.org/'),
    gevent.spawn(gethtml,'baidu','https://www.baidu.com/'),
    gevent.spawn(gethtml,'blog','http://www.cnblogs.com/alex3714/articles/5248247.html'),
])

async_time=time.time()-async_start_time
print('async_time is %s'%async_time)

sync_start_time=time.time()
urllist={'python':'https://www.python.org/',
'baidu':'https://www.baidu.com/',
'blog':'http://www.cnblogs.com/alex3714/articles/5248247.html'
         }
for filename in urllist:
    gethtml('sync'+filename,urllist.get(filename))
sync_time=time.time()-sync_start_time
print('sync_time is %s'%sync_time)