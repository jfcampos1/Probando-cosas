__author__ = 'JuanFrancisco'
import time
from random import randint

from PyQt4 import QtGui, QtCore


class MoveMySupEvent:
    def __init__(self, image, x, y, imagen, vida):
        self.imagen = imagen
        self.image = image
        self.x = x
        self.y = y
        self.vida = vida


class Supply:
    def __init__(self, x, y, imagen):
        self.posicion = [x, y]
        self.imagen = imagen
        self.vida = True
        self.vida2 = True
        self.tipo = 'supply'

    def mover(self, parent):
        parent.borrar_del_mapa(self, int(self.posicion[0]), int(self.posicion[1]))
        vacio = parent.revisar_mapa(int(self.posicion[0]), int(self.posicion[1]))
        if vacio is True:
            parent.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
        elif vacio == 'fuera':
            self.vida = False
            parent.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
        elif vacio.tipo == 'jugador':
            parent.vida += 10
            parent.balas += 15
            self.vida = False


class SuplementoTread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMySupEvent)

    def __init__(self, parent):
        super().__init__()
        self.ventana = parent
        self.path = 'supply'
        self.numero = 0
        self.numero2 = 0
        self.espacio_aparecer()
        self.image = QtGui.QLabel(parent)
        self.image.resize(50, 50)
        self.image.setPixmap(QtGui.QPixmap(self.path + '.png'))
        self.image.adjustSize()
        self.image.show()
        self.trigger.connect(parent.actualizarImagen)
        self.sup = Supply(self.numero, self.numero2, self.path)
        self.ventana.actualizar_mapa(int(self.numero), int(self.numero2), self.sup)
        self.__position = (self.numero, self.numero2)
        self.position = (self.numero, self.numero2)

    def espacio_aparecer(self):
        b = True
        while b is True:
            x = randint(0, 800)
            y = randint(0, 600)
            vacio = self.ventana.revisar_mapa(x, y)
            if vacio is True:
                self.numero = x
                self.numero2 = y
                b = False

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if self.sup.vida is True:
            self.sup.mover(self.ventana)
        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMySupEvent(
            self.image, self.sup.posicion[0], self.sup.posicion[1], self.sup.imagen, self.sup.vida2
        ))

    def run(self):
        a = True
        while a is True:
            time.sleep(0.1)
            while self.ventana.tiempo != 0:
                time.sleep(self.ventana.tiempo)
            if self.sup.vida is False:
                a = False
                time.sleep(0.1)
                self.sup.vida2 = False
            if self.ventana.vida == 0:
                a = False
                self.sup.vida2 = False
            self.position = (self.numero, self.numero2)
