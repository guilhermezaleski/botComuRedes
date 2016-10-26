#!/usr/bin/python

import socket

#host = socket.gethostname()
host = '192.168.216.34'
port = 8888
BUFFER_SIZE = 1024
print("host: ", host)
MESSAGE = input("tcpClient: Insira messagem ou exit:")

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect((host, port))

while MESSAGE != 'exit':
    tcpClient.send(MESSAGE.encode('utf8'))
    data = tcpClient.recv(BUFFER_SIZE)
    print (" Cliente menssagem recebida: :", data)
    MESSAGE = input("tcpClient: Insira messagem ou exit:")

    if MESSAGE == 'exit':
        tcpClient.send(MESSAGE.encode('utf8'))
        print ('Finalizando conexão com o servidor: ', socket.gethostname())
        tcpClient.close()