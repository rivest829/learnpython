# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket,os
server=socket.socket()
server.bind(('localhost',9999))
server.listen(10)
while True:
    conn,addr=server.accept()
    while True:
        try:
            commend=conn.recv(1024)
        except ConnectionResetError as e:
            print(e)
            break
        if not commend:
            break
        res=os.popen(commend.decode('utf-8')).read()
        if len(res)==0:
            res='no input!'

        conn.send(str(len(res.encode('utf-8'))).encode('utf-8'))
        print(str(conn.recv(1024)))
        conn.send(res.encode('utf-8'))
server.close()