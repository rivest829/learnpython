# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            try:
                self.data = self.request.recv(1024).strip()
            except ConnectionResetError as e:
                print(e)
                break
            if not self.data:
                print('Connection down')
                break
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9527

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()