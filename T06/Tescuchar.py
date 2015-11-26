__author__ = 'JuanFrancisco'

from PyQt4 import QtCore


class MoveMySupEvent:
    def __init__(self, texto, accion):
        self.texto = texto
        self.accion = accion

class ActualizarLayaut:
    def __init__(self,camino):
        self.camino=camino


class EscucharTread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMySupEvent)
    trigger2= QtCore.pyqtSignal(ActualizarLayaut)

    def __init__(self, login, cliente, mensaje):
        super().__init__()
        self.cliente = cliente
        self.ventana = login
        self.mensaje=mensaje
        self.numero = 0
        self.numero2 = 0
        self.texto = ''
        self.accion = ''
        if mensaje!='014':
            self.trigger.connect(login.actualizarimagen)
        else:
            self.trigger2.connect(login.init_GUI)
        self.__position = (self.numero, self.numero2)
        self.position = (self.numero, self.numero2)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        # El trigger emite su senal a la ventana
        if self.mensaje=='014':
            self.trigger2.emit(ActualizarLayaut(self.mensaje))
        else:
            self.trigger.emit(MoveMySupEvent(self.texto, self.accion))

    def run(self):
        mensaje = self.mensaje
        print('aquii')
        if mensaje == 'quit':
            self.cliente.desconectar()
        elif mensaje == '001':
            self.texto = 'Usuario o clave incorrectos'
            self.accion = '001'
        elif mensaje == '002':
            self.texto = 'Usuario y clave correctos'
            self.accion = '002'
        elif mensaje == '004':
            self.texto = 'Usuario ya existe'
            self.accion = '004'
        elif mensaje == '006':
            self.texto = 'Cuenta creada, has log-in'
            self.accion = '006'

        print(mensaje)
        self.position = (self.numero, self.numero2)
