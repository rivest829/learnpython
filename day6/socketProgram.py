# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket,time
count=0

sock0 = socket.socket()
sock0.connect(('localhost', 9527))
while True:
    time.sleep(0.1)
    count+=1
    # text=input('say it:')
    text='hello i\'m +++'+str(count)
    sock0.send(text.encode('utf-8'))
    result=sock0.recv(1024)
    print(result)
    if count==100:
        sock0.close()
        break
