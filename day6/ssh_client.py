# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket
client=socket.socket()
client.connect(('172.16.1.169',9999))
#client.connect(('localhost',9999))
while True:
    res_clilength=0
    output=''
    commend=input('>>:').strip()
    if len(commend)==0:continue
    client.send(commend.encode('utf-8'))
    sign=client.send('sign from client'.encode())
    res_length=client.recv(1024)
    while int(res_length) != res_clilength:
        res=client.recv(1024)
        output+=res.decode('utf-8')
        res_clilength+=len(res)
    print(output)
client.close()