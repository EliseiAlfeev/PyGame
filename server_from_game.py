import socket
import threading
import sqlite3
import os
import time
localhost="192.168.21.149"
port=1488
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((localhost,port))
main = [[]]
class ClientTread(threading.Thread):
    iam=""
    def __init__(self,clientAdress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket=clientsocket
        print("Новый", clientAdress)

    def run(self):
        global main
        msg = self.csocket.recv(4096).decode().split()
        iam = msg[1]
        id=0
        if len(main) == 1:
            main[0] = msg
            index =0
        else:
            for g in main:
                if g[0] == iam:
                    g[1] = msg[1]
                    g[2] = msg[2]
                    id = 1
                    index = main.index(g)
            if id == 0:
                index = len(main)
                main[len(main)].append(msg)
        while True:
            msg=self.csocket.recv(4096).decode().split("z")
            hj = msg[0]
            msg = hj.split()
            iam = msg[0]

            if len(main) == 0:
                main[0] = msg
            else:
                for g in main:
                    if g[0]==iam:
                        g[1]=msg[1]
                        g[2]=msg[2]
                        id=1
                if id==0:
                    main[len(main)].append(msg)
            v = " ".join(main[index])+"z"
            self.csocket.sendall(bytes(v, "UTF-8"))
            print(" ".join(main[index])+"z")
            time.sleep(0.02)
while True:
    server.listen(2)
    clientsocket, clientadress = server.accept()
    newtread = ClientTread(clientadress, clientsocket)
    newtread.start()