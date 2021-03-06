__author__ = 'JuanFrancisco'
from random import randint
from math import atan, degrees, radians, cos, sin
import time

from PyQt4 import QtGui, QtCore


class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """

    def __init__(self, image, x, y, imagen, vida):
        self.imagen = imagen
        self.image = image
        self.x = x
        self.y = y
        self.vida = vida


class Zombie:
    def __init__(self, x, y, imagen):
        self.jugador = [0, 0]
        self.angulo = 0
        self.posicion = [x, y]
        self.imagen = imagen
        self.vida = True
        self.tipo = 'zombie'
        self.ataco = False
        self.vida2 = True

    def mover(self, parent):
        if self.ataco is True:
            time.sleep(0.4)
            self.ataco = False
        self.jugador = parent.posicion
        x1 = self.jugador[0]
        y1 = self.jugador[1]
        dif_x = self.posicion[0] - x1
        dif_y = self.posicion[1] - y1
        tg = 0
        try:
            tg = abs(dif_y) / abs(dif_x)
        except ZeroDivisionError:
            tg = 0
        angulo = degrees(atan(tg))
        self.angulo = angulo
        x = 0
        y = 0
        if dif_x >= 0 and dif_y >= 0:
            if angulo > 60:
                self.revisar_pie('zombie/z_arriba_q')
                x = self.posicion[0]
                y = self.posicion[1] - 3
            elif 30 <= angulo <= 60:
                self.revisar_pie('zombie/z_dizq_q')
                x = self.posicion[0] - 3 * cos(radians(self.angulo))
                y = self.posicion[1] - 3 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('zombie/z_izq_q')
                x = self.posicion[0] - 3
                y = self.posicion[1]
        elif dif_y < 0 <= dif_x:
            if angulo > 60:
                self.revisar_pie('zombie/z_abajo_q')
                x = self.posicion[0]
                y = self.posicion[1] + 3
            elif 30 <= angulo <= 60:
                self.revisar_pie('zombie/z_dabajo_q')
                x = self.posicion[0] - 3 * cos(radians(self.angulo))
                y = self.posicion[1] + 3 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('zombie/z_izq_q')
                x = self.posicion[0] - 3
                y = self.posicion[1]
        elif dif_x < 0 and dif_y < 0:
            if angulo > 60:
                self.revisar_pie('zombie/z_abajo_q')
                x = self.posicion[0]
                y = self.posicion[1] + 3
            elif 30 <= angulo <= 60:
                self.revisar_pie('zombie/z_ddere_q')
                x = self.posicion[0] + 3 * cos(radians(self.angulo))
                y = self.posicion[1] + 3 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('zombie/z_dere_q')
                x = self.posicion[0] + 3
                y = self.posicion[1]
        elif dif_x < 0 < dif_y:
            if angulo > 60:
                self.revisar_pie('zombie/z_arriba_q')
                x = self.posicion[0]
                y = self.posicion[1] - 3
            elif 30 <= angulo <= 60:
                self.revisar_pie('zombie/z_darriba_q')
                x = self.posicion[0] + 3 * cos(radians(self.angulo))
                y = self.posicion[1] - 3 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('zombie/z_dere_q')
                x = self.posicion[0] + 3
                y = self.posicion[1]
        parent.borrar_del_mapa(self, int(self.posicion[0]), int(self.posicion[1]))
        vacio = parent.revisar_mapa(int(x), int(y))
        if self.vida is False:
            self.imagen = self.imagen[:-1] + 'm'
        else:
            if vacio is True:
                self.posicion = [x, y]
                parent.actualizar_mapa(int(x), int(y), self)
            elif vacio.tipo == 'supply':
                self.posicion = [x, y]
                parent.actualizar_mapa(int(x), int(y), self)
            elif vacio.tipo == 'zombie':
                parent.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
            elif vacio.tipo == 'jugador':
                if parent.vida > 0:
                    parent.vida -= 10
                self.imagen = self.imagen[:-1] + 'a'
                parent.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
                self.ataco = True

    def revisar_pie(self, imagen):
        if self.imagen == imagen:
            if self.imagen[-1] == 'q':
                self.imagen = self.imagen[:-1] + 'd'
            elif self.imagen[-1] == 'd':
                self.imagen = self.imagen[:-1] + 'i'
            elif self.imagen[-1] == 'i':
                self.imagen = self.imagen[:-1] + 'q'
        else:
            self.imagen = imagen


class Character(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMyImageEvent)

    def __init__(self, parent, path):
        super().__init__()
        self.ventana = parent
        self.image = QtGui.QLabel(parent)
        self.image.resize(50, 50)
        self.image.setPixmap(QtGui.QPixmap(path))
        self.image.adjustSize()
        self.image.show()
        self.trigger.connect(parent.actualizarImagen)
        x, y = self.espacio_aparecer()
        self.numero = x
        self.numero2 = y
        self.zombie = Zombie(self.numero, self.numero2, 'zombie/z_arriba_q')
        self.ventana.actualizar_mapa(int(x), int(y), self.zombie)
        self.__position = (self.numero, self.numero2)
        self.position = (self.numero, self.numero2)

    def espacio_aparecer(self):
        b = True
        while b is True:
            lado = randint(0, 4)
            x = 0
            y = 0
            if lado == 0:
                x = randint(0, 750)
                y = randint(0, 100)
            elif lado == 1:
                x = randint(0, 100)
                y = randint(0, 550)
            elif lado == 2:
                x = randint(650, 750)
                y = randint(0, 550)
            elif lado == 4:
                x = randint(0, 750)
                y = randint(450, 550)
            vacio = self.ventana.revisar_mapa(x, y)
            if vacio is True:
                return x, y

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        self.zombie.mover(self.ventana)
        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.zombie.posicion[0], self.zombie.posicion[1], self.zombie.imagen, self.zombie.vida2
        ))

    def run(self):
        a = True
        while a is True:
            time.sleep(0.1)  # con esto edito la velocidad de los zombies
            while self.ventana.tiempo != 0:
                time.sleep(self.ventana.tiempo)
            self.position = (self.numero, self.numero2)
            if self.zombie.vida is False:
                a = False
                time.sleep(2)
                self.zombie.vida2 = False
                self.position = (self.numero, self.numero2)
            if self.ventana.vida <= 0:
                a = False
                self.zombie.vida2 = False
                self.position = (self.numero, self.numero2)
