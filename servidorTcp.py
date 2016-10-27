#coding: UTF-8
#!/usr/bin/python

import socket
import _thread as thread


HOST = ''              # Endereco IP do Servidor
PORT = 8888            # Porta que o Servidor esta

BUFFER_SIZE = 1024

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(999)

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(BUFFER_SIZE)
        msg = msg.decode('utf8')
        print ('Cliente:', cliente,' Msg: ', msg)

        if msg == 'exit':
            break

        if msg == 'ok':
            msgEnvia = "ok"
            con.send(msgEnvia.encode('utf8'))
            print ('ok')
        else:
            msgEnvia = "no"
            con.send(msgEnvia.encode('utf8'))
            print ('nada ok')

    print ('Finalizando conexao do cliente: ', cliente)
    con.close()
    thread.exit()

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()