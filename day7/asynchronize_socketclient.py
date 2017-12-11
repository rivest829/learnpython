import gevent,socket
from gevent import monkey
monkey.patch_all()

def client():
    client=socket.socket()
    client.connect(('localhost',9527))
    while True:
        data=input(">>:")
        if len(data)==0:continue
        client.sendall(data.encode())
        response=client.recv(1024).decode()
        print(response)
client()