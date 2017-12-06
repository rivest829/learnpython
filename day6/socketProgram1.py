# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket,time
count=0
sock1 = socket.socket()
sock1.connect(('localhost', 9527))
while True:
    time.sleep(0.1)
    count+=1
    # text=input('say it:')
    text='hello,i\'m --sb-'+str(count)
    sock1.send(text.encode('utf-8'))
    result=sock1.recv(1024)
    print(result)
    if count==100:
        sock1.close()
        break