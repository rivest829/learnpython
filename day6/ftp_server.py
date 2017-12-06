# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket, hashlib, os

server = socket.socket()
server.bind(('localhost', 9608))
#server.bind(('0.0.0.0', 9608))
server.listen(10)
while True:
    file_str=b''
    conn, addr = server.accept()
    print('waiting for command')
    while True:
        try:
            filename = conn.recv(1024)
        except ConnectionResetError as e:
            print(e)
            break
        print('got the filename %s' % filename)
        try:
            file = open(filename, 'rb')
        except FileNotFoundError as e:
            conn.send(str(e).encode())
            break
        else:
            conn.send('file exists,reading......'.encode())
        file_size = str(os.stat(filename).st_size)
        print(conn.recv(1024).decode())
        conn.send(file_size.encode())
        hash_obj = hashlib.md5()
        print('file info send done,start send file')
        for line in file:
            hash_obj.update(line)
            conn.send(line)
        print(conn.recv(1024).decode())
        file_md5=hash_obj.hexdigest()
        conn.send(file_md5.encode())
        print('send done')
