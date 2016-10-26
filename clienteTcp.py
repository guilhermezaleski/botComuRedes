#!/usr/bin/python

import socket
from tkinter import *


class conectServidor:

    def conectar(self):
        #host = socket.gethostname()
        self.host = '192.168.216.34'
        self.port = 8888
        self.BUFFER_SIZE = 1024
        self.print("host: ", self.host)
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

class App:

    def __init__(self, master):

        self.master = master

        frame = Frame(master)
        frame.pack()

        self.textString = StringVar()

        self.conect = Button(frame, text="Conectar", command=self.enviar_mensagem)
        self.conect.grid(row=0, column=0)

        self.desconect = Button(frame, text="Desconectar", command=self.enviar_mensagem)
        self.desconect.grid(row=0, column=2)

        scrollbar = Scrollbar(master)
        scrollbar.grid(row=1, column=3, sticky=W)

        self.text = Listbox(frame, bd=0, yscrollcommand=scrollbar.set)
        self.text.grid(row=1, column=3, sticky=W)
        scrollbar.config(command=self.text.yview)

        self.msg = Label(frame, text='Mensagem: ', textvariable=self.textString)
        self.msg.grid(row=2, sticky=W)

        self.entry = Entry(frame)
        self.entry.grid(row=2, column=1, sticky=W+E)

        self.enviar = Button(frame, text="Enviar", command=self.enviar_mensagem)
        self.enviar.grid(row=2, column=2, sticky=E)

        self.master.after(500, self.oi)


    def enviar_mensagem(self):
        conectServidor.enviar_mensagem(self.msg.getvar())


    def oi(self):
        self.master.after(500, self.oi)
        self.text.delete(1.0, END)
        self.text.insert(END, "server")



root = Tk()

app = App(root)

root.mainloop()
