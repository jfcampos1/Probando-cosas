__author__ = 'JuanFrancisco'
# coding=utf-8
import socket
import threading
import sys
from Gui_cliente import Cuenta
from PyQt4 import QtGui
from Tescuchar import EscucharTread
from Gui import Login,NuevaCuenta
from serializar import make_dir


class Cliente:
    def __init__(self):
        self.usuario = ''
        self.host = 'Juanfra'
        self.port = 3491
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = True
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port))  # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
            self.nueva = NuevaCuenta(self)
            self.login = Login(self,self.nueva)
            self.login.show()
            self.gucliente=Cuenta(self)
            # escuchar=EscucharTread(self.login,self)
            # escuchar.start()
            print('Conectado')
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        codigo=''
        while self.connection and codigo=='':
            data = self.s_cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.desconectar()
            elif mensaje.split(': ')[1] == '001':
                self.login.label_4.setText('Usuario o clave incorrectos')
            elif mensaje.split(': ')[1] == '002':
                print('Usuario y clave correctos')
                self.usuario=mensaje.split(': ')[2]
                print(self.usuario)
                escuchar=EscucharTread(self.login,self,'002')
                escuchar.start()
                self.login.label_4.setText('Usuario y clave correctos')
            elif mensaje.split(': ')[1] == '004':
                self.nueva.label_4.setText('Usuario ya existe')
            elif mensaje.split(': ')[1] == '006':
                escuchar=EscucharTread(self.login,self,'006')
                escuchar.start()
                self.login.label_4.setText('Cuenta creada, has log-in')
            print(mensaje)
        # self.nuevo_escuchar(codigo)

    def nuevo_escuchar(self,codigo):
        if codigo=='002':
            self.login.hide()
            self.gucliente.show()
        elif codigo=='006':
            self.nueva.hide()
            self.login.show()

    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.s_cliente.send(msj_final.encode('utf-8'))

    def desconectar(self):
        self.connection = False
        print('El servidor se ha desconectado')
        print(self.connection)
        self.s_cliente.close()
        sys.exit()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    client = Cliente()
    app.exec_()
