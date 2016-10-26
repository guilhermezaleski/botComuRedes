#!/usr/bin/python

import socket
from tkinter import *
gui = Tk()

class conectServidor:

    def conectar(self):
        #host = socket.gethostname()
        self.host = '192.168.216.34'
        self.port = 8888
        self.BUFFER_SIZE = 1024
        print("host: ", self.host)
       # self.MESSAGE = input("tcpClient: Insira messagem ou exit:")

        try:
            self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcpClient.connect((self.host, self.port))

        except:
            print ("Erro ao conectar")


    def desconectar(self):
        MESSAGE = 'exit'
        self.tcpClient.send(MESSAGE.encode('utf8'))
        print ('Finalizando conexão com o servidor: ', socket.gethostname())
        self.tcpClient.close()

    def enviar_mensagem(self, MESSAGE):

        self.tcpClient.send(MESSAGE.encode('utf8'))
        data = self.tcpClient.recv(self.BUFFER_SIZE)
        print (" Cliente menssagem recebida: :", data)
        MESSAGE = input("tcpClient: Insira messagem ou exit:")


        if MESSAGE == 'exit':
           self.tcpClient.send(MESSAGE.encode('utf8'))
           print ('Finalizando conexão com o servidor: ', socket.gethostname())
           self.tcpClient.close()


class Janela:

    def __init__(self, janela):

        self.servidor = ''
        self.mensagem = ''

        self.frame00 = Frame(janela)
        self.frame00.pack(side=TOP)

        self.labelServidor = Label(self.frame00, text="Servidor: ")
        self.labelServidor.pack(side=LEFT)

        self.entryServidor = Entry(self.frame00, width=30, textvariable=self.servidor)
        self.entryServidor.insert(END, 'localhost')
        self.entryServidor.pack(side=LEFT)

        self.buttonConectar = Button(self.frame00, text = "Conectar", command=self.conectar)
        self.buttonConectar.pack(side=LEFT)

        self.buttonDesconectar = Button(self.frame00, text="Desconectar", command=self.desconectar)
        self.buttonDesconectar.pack(side=LEFT)

        self.frame01 = Frame(janela)
        self.frame01.pack(side=TOP)

        self.text = Text(self.frame01, height=20, width=44)
        self.vsb = Scrollbar(self.frame01, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set, state=DISABLED)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both")

        self.frame02 = Frame(janela)
        self.frame02.pack(side=TOP)

        self.labelMensagem = Label(self.frame02, text="Mensagem: ")
        self.labelMensagem.pack(side=LEFT)

        self.entryMensagem = Entry(self.frame02, width=30, textvariable=self.mensagem)
        self.entryMensagem.pack(side=LEFT)

        self.buttonEnviar = Button(self.frame02, text="Enviar", command=self.enviar)
        self.buttonEnviar.pack(side=LEFT)


    def setText(self, texto):
        self.text.configure(state=NORMAL)
        self.text.insert(INSERT, texto + '\n')
        self.text.see('end')
        self.text.configure(state=DISABLED)

    def enviar(self):
        self.setText('Enviado: ' + self.entryMensagem.get())

    def conectar(self):
        self.setText('Conectando ao servidor ' + self.entryServidor.get()+' ...')

    def desconectar(self):
        self.setText('Desconectando do servidor ...')




Janela(gui)
janela = Janela

gui.mainloop()

