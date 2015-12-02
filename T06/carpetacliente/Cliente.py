__author__ = 'JuanFrancisco'
# coding=utf-8
import socket
import threading
import sys
import pickle
import os
from PyQt4 import QtGui

from Cuenta import MainForm
from Tescuchar import EscucharTread
from Gui import Login, NuevaCuenta
from serializar import make_dir, existe_persona, get_persona,crear_persona


class Cliente:
    def __init__(self):
        self.usuario = ''
        self.host = '127.0.0.1'
        self.port = 3491
        self.port2 = 3492
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_cliente2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = True
        self.hijos = {}
        self.conectados=['Pepito','Juan']
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port))
            self.s_cliente2.connect((self.host, self.port2))
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
            recibidor2 = threading.Thread(target=self.recibir_mensajes2, args=())
            recibidor2.daemon = True
            recibidor2.start()
            self.nueva = NuevaCuenta(self)
            self.login = Login(self, self.nueva)
            self.login.show()
            self.gucliente = MainForm(self)
            make_dir('Cliente')
            print('Conectado')
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        salir = True
        while self.connection and salir is True:
            data = self.s_cliente.recv(2048)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.desconectar()
            elif mensaje.split(': ')[1] == '001':
                self.login.label_4.setText('Usuario o clave incorrectos')
            elif mensaje.split(': ')[1] == '002':
                print('Usuario y clave correctos')
                self.usuario = mensaje.split(': ')[2]
                print(self.usuario)
                escuchar = EscucharTread(self.login, self, '002')
                escuchar.start()
                self.login.label_4.setText('Usuario y clave correctos')
                self.comprobar_cambios()
                print('termino de comprobar')
            elif mensaje.split(': ')[1] == '004':
                self.nueva.label_4.setText('Usuario ya existe')
            elif mensaje.split(': ')[1] == '006':
                escuchar = EscucharTread(self.login, self, '006')
                escuchar.start()
                self.login.label_4.setText('Cuenta creada, has log-in')
            elif mensaje.split(':')[1] == ' 010':
                print('aquii')
                s_cliente, codigo, largo = mensaje.split(':')
                data = b''
                l = int(largo)
                while l > 0:
                    d = self.s_cliente.recv(l)
                    l -= len(d)
                    data += d
                mensaje = pickle.loads(data)
                client, codigo, lugar, archivo = mensaje
                path = lugar + '\\' + archivo.nombre
                print(client, codigo)
                with open('{}'.format(path), 'wb') as afile:
                    afile.write(archivo.archivo)
            elif mensaje.split(':')[1] == ' 014':
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
                self.hijos = camino
                # self.gucliente=MainForm(self)
                escuchar = EscucharTread(self.gucliente.form, self, '014')
                escuchar.start()
                # print(mensaje)
            elif mensaje.split(':')[1] == ' 017':
                s_cliente, codigo, largo = mensaje.split(':')
                data = b''
                l = int(largo)
                while l > 0:
                    d = self.s_cliente.recv(l)
                    l -= len(d)
                    data += d
                mensaje = pickle.loads(data)
                self.conectados=mensaje
                escuchar = EscucharTread(self.gucliente.elchat, self, '014')
                escuchar.start()
        print('afuera de recibir mensajes')

    def recibir_mensajes2(self):
        salir = True
        while self.connection and salir is True:
            data = self.s_cliente2.recv(2048)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.desconectar()
            else:
                s_cliente, s_a ,codigo, largo = mensaje.split(':')
                cenviar=self.conectados.index(s_a)
                if codigo == '019':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = self.s_cliente2.recv(l)
                        l -= len(d)
                        data += d
                    mensaje = pickle.loads(data)
                    client, codigo, lugar, archivo = mensaje
                    path = lugar + '\\' + archivo.nombre
                    with open('{}'.format(path), 'wb') as afile:
                        afile.write(archivo.archivo)
                else:
                    self.clientes2[cenviar].sendall(mensaje.encode('utf-8'))

    def comprobar_cambios(self):
        if existe_persona(self.usuario, 'Cliente'):
            persona = get_persona(self.usuario, 'Cliente')
            print('archivo usuario:',persona.archivos.nombre)
            print(persona.archivos.hijos)
            print(persona.archivos)
            for i in persona.archivos.hijos:
                print('a revisar')
                self.revisar_archivos(i)
        else:
            crear_persona(self.usuario, self.usuario,'','Cliente')

    def revisar_archivos(self,nodo):
        print('aquiiii revisando')
        if os.path.exists(nodo.nombre):
            for i in nodo.hijos:
                if i.valor=='013':
                    self.revisar_archivos(i)
                else:
                    if not os.path.exists(i.nombre):
                        nombre=i.nombre.split('\\')
                        print('mande a borrar:',nombre)
                        self.s_cliente.sendall('{}: 016:{}'.format(self.usuario,nombre[-1]))
        else:
            nombre=nodo.nombre.split('\\')
            print('mande a borrar:',nombre)
            self.s_cliente.sendall('{}: 016:{}'.format(self.usuario,nombre[-1]))

    def nuevo_escuchar(self, codigo):
        if codigo == '002':
            self.login.hide()
            self.gucliente.show()
        elif codigo == '006':
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
        self.s_cliente2.close()
        sys.exit()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    client = Cliente()
    app.exec_()
