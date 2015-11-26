__author__ = 'JuanFrancisco'
# coding=utf-8
import socket
import threading
import sys
import pickle
from Cuenta import MainForm
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
        self.hijos={}
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port))
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
            self.nueva = NuevaCuenta(self)
            self.login = Login(self,self.nueva)
            self.login.show()
            # self.gucliente=None
            self.gucliente=MainForm(self)
            make_dir('Cliente')
            # escuchar=EscucharTread(self.login,self)
            # escuchar.start()
            print('Conectado')
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        salir=True
        while self.connection and salir is True:
            data = self.s_cliente.recv(2048)
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
            elif mensaje.split(':')[1]==' 010':
                print('aquii')
                s_cliente, codigo, largo = mensaje.split(':')
                data = b''
                l = int(largo)
                while l > 0:
                    d = self.s_cliente.recv(l)
                    l -= len(d)
                    data += d
                mensaje = pickle.loads(data)
                client, codigo, archivo = mensaje
                print(archivo)
                print(client,codigo)
                with open('./Cliente/{}'.format(archivo.nombre),'wb') as afile:
                    afile.write(archivo.valor.archivo)
            elif mensaje.split(':')[1]==' 014':
                print('layaut')
                s_cliente, codigo, largo = mensaje.split(':')
                data = b''
                l = int(largo)
                while l > 0:
                    d = self.s_cliente.recv(l)
                    l -= len(d)
                    data += d
                mensaje = pickle.loads(data)
                client, codigo, camino = mensaje
                self.hijos=camino
                # self.gucliente=MainForm(self)
                escuchar=EscucharTread(self.gucliente.form,self,'014')
                escuchar.start()
            print(mensaje)
        print('afuera de recibir mensajes')
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
