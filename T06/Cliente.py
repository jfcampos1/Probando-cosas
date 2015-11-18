__author__ = 'JuanFrancisco'
# coding=utf-8
import socket
import threading
import sys
from PyQt4 import QtGui,QtCore
from Gui import Login


class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = 'Juanfra'
        self.port = 3491
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = True
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port)) # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
            self.login = Login(self)
            self.login.show()
            print('Conectado')
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while self.connection:
            data = self.s_cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.desconectar()
            elif mensaje.split(': ')[1] == '001':
                self.login.label_4.setText('Usuario o clave incorrectos')
            elif mensaje.split(': ')[1] == '002':
                print('Usuario y clave correctos')
            elif mensaje.split(': ')[1] == '004':
                self.login.nueva.label_4.setText('Usuario ya existe')
            elif mensaje.split(': ')[1] == '006':
                self.login.nueva.botonatras()
                self.login.label_4.setText('Cuenta creada, has log-in')
            print(mensaje)

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
    nombre = input("Ingrese el nombre del usuario: ")
    client = Cliente(nombre)
    # while client.connection:
        # texto = input()
        # if texto == 'quit':
        #     client.enviar('quit')
        #     client.desconectar()
        # else:
        #     client.enviar(texto)
    app.exec_()