# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket
class client(object):
    def __init__(self,addr,port):
        self.addr=addr
        self.port=port
    def send(self,filename):
        sock = socket.socket()
        sock.connect((self.addr,self.port))
        f=open(filename,'rb')
        pack=f.read()
        sock.sendall(pack)
        sock.close()
    def recv(self,filename):
        sock = socket.socket()
        sock.connect((self.addr,self.port))
        res=sock.recv(8196)
        f=open(filename,'wb')
        f.write(res)
        sock.close()
while True:
    choice=input('what you want?(send or recv)')
    filename=input('your filename:')
    addr=input('target address:')
    port=int(input('target port:'))
    s = client(addr,port)
    if hasattr(s,choice):
        getattr(s,choice)(filename)
    else:
        print('no such function like this!')