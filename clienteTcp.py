#coding: UTF-8
#!/usr/bin/python

import socket
from tkinter import *
gui = Tk()

class conectServidor:

    def conectar(self, servidor):

        if servidor != 'localhost':

            self.host = servidor

        else:

            self.host = socket.gethostname()

        self.port = 8888
        self.BUFFER_SIZE = 1024

        try:

            self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcpClient.connect((self.host, self.port))

        except:
            return 'Erro ao conectar!'

        else:
            return 'Conectado!'

    def desconectar(self):

        MESSAGE = 'exit@1234?'
        self.tcpClient.send(MESSAGE.encode('utf8'))
        self.tcpClient.close()

        return 'Desconectado!'

    def enviarmensagem(self, MESSAGE):

        self.tcpClient.send(MESSAGE.encode('utf8'))

        return str('Recebido: '+ (self.tcpClient.recv(self.BUFFER_SIZE)).decode('utf8') + '\n')

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
        self.buttonDesconectar.configure(state=DISABLED)
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
        self.entryMensagem.bind("<Return>", self.enviar)
        self.entryMensagem.pack(side=LEFT)

        self.buttonEnviar = Button(self.frame02, text="Enviar")
        self.buttonEnviar.bind("<Any-Button>", self.enviar)
        self.buttonEnviar.pack(side=LEFT)

    def setText(self, texto):

        self.text.configure(state=NORMAL)
        self.text.see('end')
        self.text.insert(INSERT, texto + '\n')
        self.text.see('end')
        self.text.configure(state=DISABLED)

    def enviar(self, event):

        msg = self.entryMensagem.get()

        if msg != '':

            self.entryMensagem.delete(0, END)
            self.setText('Enviado:  ' + msg )
            self.setText(conectServidor.enviarmensagem(self, msg ))

    def conectar(self):

        self.servidor = self.entryServidor.get()
        self.setText('Conectando ao servidor ' + self.servidor +' ...')
        self.statusConexcao = conectServidor.conectar(self, self.servidor)
        self.setText(self.statusConexcao)

        if self.statusConexcao == 'Conectado!':

            self.buttonDesconectar.configure(state=NORMAL)
            self.buttonConectar.configure(state=DISABLED)

    def desconectar(self):

        self.setText('Desconectando do servidor ...')
        self.statusConexcao = conectServidor.desconectar(self)
        self.setText(self.statusConexcao)

        if self.statusConexcao == 'Desconectado!':

            self.buttonConectar.configure(state=NORMAL)
            self.buttonDesconectar.configure(state=DISABLED)

Janela(gui)
janela = Janela

gui.title('Cliente')
gui.mainloop()

