__author__ = 'JuanFrancisco'
from math import radians, cos, sin
import time

from PyQt4 import QtGui, QtCore


class MoveMyDisparoEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """

    def __init__(self, image, x, y, imagen,vida):
        self.imagen = imagen
        self.image = image
        self.x = x
        self.y = y
        self.vida=vida


class Disparo:
    def __init__(self, x, y, angulo, direccion, imagen):
        self.puntero = direccion
        self.angulo = angulo
        self.posicion = [x, y]
        self.imagen = imagen
        self.vida = True
        self.vida2=True
        self.tipo = 'disparo'

    def mover(self, parent):
        x = 0
        y = 0
        if self.puntero[0] == -1:
            if self.puntero[1] == -1:
                x = self.posicion[0] + 10 * cos(radians(self.angulo))
                y = self.posicion[1] + 10 * sin(radians(self.angulo))
                if self.angulo >= 60:
                    x = self.posicion[0]
                    y = self.posicion[1] + 10
            elif self.puntero[1] == 1:
                x = self.posicion[0] + 10 * cos(radians(self.angulo))
                y = self.posicion[1] - 10 * sin(radians(self.angulo))
                if self.angulo >= 60:
                    x = self.posicion[0]
                    y = self.posicion[1] - 10
            if self.angulo < 30:
                x = self.posicion[0] + 10
                y = self.posicion[1]
        elif self.puntero[0] == 1:
            if self.puntero[1] == -1:
                x = self.posicion[0] - 10 * cos(radians(self.angulo))
                y = self.posicion[1] + 10 * sin(radians(self.angulo))
                if self.angulo >= 60:
                    x = self.posicion[0]
                    y = self.posicion[1] + 10
            elif self.puntero[1] == 1:
                x = self.posicion[0] - 10 * cos(radians(self.angulo))
                y = self.posicion[1] - 10 * sin(radians(self.angulo))
                if self.angulo >= 60:
                    x = self.posicion[0]
                    y = self.posicion[1] - 10
            if self.angulo < 30:
                x = self.posicion[0] - 10
                y = self.posicion[1]
        parent.borrar_del_mapa(self, int(self.posicion[0]), int(self.posicion[1]))
        vacio = parent.revisar_mapa_disparo(int(x), int(y))
        if vacio is True:
            self.posicion = [x, y]
            parent.actualizar_mapa_disparo(int(x), int(y), self, False)
        elif vacio=='fuera':
            self.vida=False
            parent.actualizar_mapa_disparo(int(self.posicion[0]), int(self.posicion[1]), self, True)
        elif vacio.tipo == 'zombie':
            print('diste a un zombiee')
            parent.actualizar_mapa_disparo(int(self.posicion[0]), int(self.posicion[1]), self, True)
            self.vida = False
            vacio.vida = False




class DisparoTread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMyDisparoEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEvent

    def __init__(self, parent):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.ventana = parent
        self.direccion = parent.puntero
        self.angulo = parent.angulo
        self.numero = parent.posicion[0]
        self.numero2 = parent.posicion[1]
        self.path = ''
        self.espacio_aparecer()
        self.image = QtGui.QLabel(parent)
        self.image.resize(50, 50)
        self.image.setPixmap(QtGui.QPixmap(self.path + '.png'))
        self.image.adjustSize()
        self.image.show()
        self.trigger.connect(parent.actualizarImagendisparo)
        self.bala = Disparo(self.numero, self.numero2, self.angulo, self.direccion, self.path)
        self.ventana.actualizar_mapa(int(self.numero), int(self.numero2), self.bala)
        self.__position = (self.numero, self.numero2)
        self.position = (self.numero, self.numero2)

    def espacio_aparecer(self):
        if self.direccion[0] == 1:
            if self.direccion[1] == 1:
                if self.angulo >= 60:
                    self.path = 'disparos/d_arriba'
                    self.numero += 25
                    self.numero2 -= 0
                elif 30 < self.angulo < 60:
                    self.path = 'disparos/d_dizq'
                    self.numero -= 0
                    self.numero2 -= 0
            elif self.direccion[1] == -1:
                if self.angulo >= 60:
                    self.path = 'disparos/d_abajo'
                    self.numero += 25
                    self.numero2 += 50
                elif 30 < self.angulo < 60:
                    self.path = 'disparos/d_dabajo'
                    self.numero -= 0
                    self.numero2 += 50
            if self.angulo <= 30:
                self.path = 'disparos/d_izq'
                self.numero -= 0
                self.numero2 += 25
        elif self.direccion[0] == -1:
            if self.direccion[1] == 1:
                if self.angulo >= 60:
                    self.path = 'disparos/d_arriba'
                    self.numero += 25
                    self.numero2 -= 0
                elif 30 < self.angulo < 60:
                    self.path = 'disparos/d_darriba'
                    self.numero += 50
                    self.numero2 -= 0
            elif self.direccion[1] == -1:
                if self.angulo >= 60:
                    self.path = 'disparos/d_abajo'
                    self.numero += 25
                    self.numero2 += 50
                elif 30 < self.angulo < 60:
                    self.path = 'disparos/d_ddere'
                    self.numero += 50
                    self.numero2 += 50
            if self.angulo <= 30:
                self.path = 'disparos/d_dere'
                self.numero += 50
                self.numero2 += 25

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if self.bala.vida is True:
            self.bala.mover(self.ventana)
        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMyDisparoEvent(
            self.image, self.bala.posicion[0], self.bala.posicion[1], self.bala.imagen,self.bala.vida2
        ))

    def run(self):
        a = True
        while a is True:
            time.sleep(0.04)  # con esto edito la velocidad de los disparos
            while self.ventana.tiempo!=0:
                time.sleep(self.ventana.tiempo)
            if self.bala.vida is False:
                a = False
                time.sleep(0.1)
                self.bala.vida2=False
            self.position = (self.numero, self.numero2)
