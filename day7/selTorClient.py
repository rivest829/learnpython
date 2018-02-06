import threading,socket,time
cli_list=[]
def client(i):
    client=socket.socket()
    client.connect(('localhost',9998))
    while True:
        data='thread num'+str(i)
        client.send(data.encode())
        response=client.recv(1024)
        print(response.decode())
for i in range(10):
    t=threading.Thread(target=client,args=(i,))
    t.start()