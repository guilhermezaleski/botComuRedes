#coding: UTF-8
#!/usr/bin/python

import socket
import _thread as thread
import bot
from datetime import datetime


try:
    arquivolog = open('servidorLog.txt', 'a')
    linha = '\n\n' + str(datetime.now()) + '   Serviço iniciado em ' + socket.gethostname() + '\n'
    arquivolog.write(linha)
    arquivolog.close()
except:
    print('--- ERRO ao abrir arquivo de log!')



HOST = ''              # Endereco IP do Servidor
PORT = 8888            # Porta que o Servidor esta

BUFFER_SIZE = 1024

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(999)

def conectado(con, cliente, arquivolog):
    try:
        arquivolog = open('servidorLog.txt', 'a')
        arquivolog.write(str(datetime.now()) + '   Conectado por: '+ str(cliente) + '\n')
        arquivolog.close()
    except:
        pass

    while True:
        msg = con.recv(BUFFER_SIZE)
        msg = msg.decode('utf8')

        try:
            arquivolog = open('servidorLog.txt', 'a')
            arquivolog.write(str(datetime.now()) + '   Recebido do Cliente:' + str(cliente) + ' Mensagem: '+ msg + '\n')
            arquivolog.close()
        except:
            pass

        if msg == 'exit@1234?':
            break

        msgEnvia = bot.comando(msg)

        con.send(msgEnvia.encode('utf8'))

        try:
            arquivolog = open('servidorLog.txt', 'a')
            arquivolog.write(str(datetime.now()) + '   Enviado  ao cliente:' + str(cliente) +
                                                                            ' Mensagem: ' + msgEnvia + '\n')
            arquivolog.close()
        except:
            pass



    con.close()

    try:
        arquivolog = open('servidorLog.txt', 'a')
        arquivolog.write(str(datetime.now()) + '   Finalizada conexção com cliente: '+ str(cliente) + '\n')
        arquivolog.close()
    except:
        pass

    thread.exit()

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente, arquivolog]))

tcp.close()
