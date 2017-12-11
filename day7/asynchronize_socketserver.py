import gevent,socket,time
from gevent import monkey
monkey.patch_all()

def server():
    server=socket.socket()
    server.bind(('localhost',9527))
    server.listen(5)
    while True:
        conn,addr=server.accept()
        gevent.spawn(handle,conn)
    server.close()

def handle(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
        except ConnectionResetError as e:
            print(e)
        if not data:
           conn.shutdown()
        print('get %s' % data)
        time.sleep(2)
        conn.send(data.upper().encode())
server()

