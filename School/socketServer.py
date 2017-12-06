# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket,os
class Conn(object):
    def __init__(self,conn,addr):
        self.conn=conn
        self.addr=addr
    def connn(self):
        result = self.conn.recv(8196)
        f=open('server.mp3','wb')
        f.write(result)
        return 1



sock2=socket.socket()
sock2.bind(('localhost',9527))
sock2.listen(0)
while True:
    conn,addr=sock2.accept()
    if Conn(conn,addr).connn()==1:
        conn.close()