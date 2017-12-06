# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket
class Conn(object):
    def __init__(self,conn,addr):
        self.conn=conn
        self.addr=addr
    def connn(self):
        while True:
            if len(result)==0:
                break
            result = self.conn.recv(1024)
            print(result)
            self.conn.send(result.upper())
        return 1

sock2=socket.socket()
sock2.bind(('localhost',9527))
sock2.listen(0)
while True:
    conn,addr=sock2.accept()
    if Conn(conn,addr).connn()==1:
        conn.close()

