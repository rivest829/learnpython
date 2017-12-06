# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socket, hashlib,os
client = socket.socket()
client.connect(('localhost', 9608))
#client.connect(('172.16.1.169', 9608))
while True:
    file=b''
    recv_file_size = 0
    hash_obj = hashlib.md5()
    filename = input('what you want:')
    if len(filename) == 0: continue
    client.send(filename.encode())
    file_exists = client.recv(1024).decode()
    if file_exists[0] != 'f':
        print(file_exists)
        continue
    file_get = open('bak' + filename, 'wb')
    client.send('ready to get file size'.encode())
    file_size = int(client.recv(1024).decode())
    while recv_file_size < file_size:
        if file_size-recv_file_size>1024:
            trans_size=1024
        else:
            trans_size=file_size-recv_file_size
            print('last trans_size is %s'% trans_size)
        print('now the file size is %s,total size is %s' % (recv_file_size, file_size))
        file = client.recv(trans_size)
        file_get.write(file)
        recv_file_size += len(file)
        hash_obj.update(file)

    client.send('ready to check md5'.encode())
    target_md5=client.recv(1024).decode()
    file_md5=hash_obj.hexdigest()
    if target_md5==file_md5:
        print('file check done!the same file.\nTarget md5 is %s,recv file md5 is %s'%(target_md5,file_md5))
    else:
        print('file check done!wrong file.\nTarget md5 is %s,recv file md5 is %s'%(target_md5,file_md5))
    print('transfer is done')

