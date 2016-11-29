#coding: UTF-8
#!/usr/bin/python

import socket
import _thread as thread
import bot  # importação do arquivo com os comandos
from datetime import datetime


try:

    arquivolog = open('servidorLog.txt', 'a') # abertura do arquivo de log
    linha = '\n\n' + str(datetime.now()) + '   Serviço iniciado em ' + socket.gethostname() + '\n'
    arquivolog.write(linha)
    arquivolog.close()

except:
    pass

HOST = ''              # Endereco IP do Servidor
PORT = 8888            # Porta que o Servidor estará escutando

BUFFER_SIZE = 1024  # tamanho do buffer do pacote a ser comunicado

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket TCP/IP
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(999)   # até 999 conexões

def conectado(con, cliente, arquivolog):

    try:

        arquivolog = open('servidorLog.txt', 'a')
        arquivolog.write(str(datetime.now()) + '   Conectado por: '+ str(cliente) + '\n')
        arquivolog.close()

    except:
        pass

    while True:

        msg = con.recv(BUFFER_SIZE)  # recece pacote do cliente
        msg = msg.decode('utf8')

        try:

            arquivolog = open('servidorLog.txt', 'a')
            arquivolog.write(str(datetime.now()) + '   Recebido do Cliente:' + str(cliente) + ' Mensagem: '+ msg + '\n')
            arquivolog.close()

        except:
            pass

        if msg == 'exit@1234?': # comando para terminar conexão
            break

        msgEnvia = bot.comando(msg)  # envia, processa e recebe o resultado

        con.send(msgEnvia.encode('utf8')) # envia o resultado para cliente

        try:

            arquivolog = open('servidorLog.txt', 'a')
            arquivolog.write(str(datetime.now()) + '   Enviado  ao cliente:' + str(cliente) +
                                                                            ' Mensagem: ' + msgEnvia + '\n')
            arquivolog.close()

        except:
            pass

    con.close() # fecha conexão

    try:

        arquivolog = open('servidorLog.txt', 'a')
        arquivolog.write(str(datetime.now()) + '   Finalizada conexção com cliente: '+ str(cliente) + '\n')
        arquivolog.close()

    except:
        pass

    thread.exit() # encerra thread

while True:

    con, cliente = tcp.accept() # aguarda conexao do cliente
    thread.start_new_thread(conectado, tuple([con, cliente, arquivolog])) # a cada conexão de um cliente é criada uma
                                                                          # nova thread com socket

tcp.close()
