__author__ = 'JuanFrancisco'
from PyQt4 import QtGui,QtCore
from Mainwindow import MainWindow
from random import randint
from math import atan, degrees, radians, cos, sin
import time


class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

class Zombie:
    def __init__(self,x,y,label):
        self.jugador = [0, 0]
        self.angulo = 0
        self.posicion = [x, y]
        self.imagen_l=label

    def mover(self,parent):
        self.posicion=parent.posicion
        x = self.jugador[0]
        y = self.jugador[1]
        dif_x = self.posicion[0] - x
        dif_y = self.posicion[1] - y
        tg = abs(dif_y) / abs(dif_x)
        angulo = degrees(atan(tg))
        self.angulo=angulo
        if dif_x >= 0 and dif_y >= 0:
            self.puntero = [1, 1]
            if angulo > 60:
                self.revisar_pie('z_arriba_q')
                x = self.posicion[0]
                y = self.posicion[1] - 6
            elif 30 <= angulo <= 60:
                self.revisar_pie('z_dizq_q')
                x = self.posicion[0] - 6 * cos(radians(self.angulo))
                y = self.posicion[1] - 6 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('z_izq_q')
                x = self.posicion[0] - 6
                y = self.posicion[1]
        elif dif_y < 0 <= dif_x:
            self.puntero = [1, -1]
            if angulo > 60:
                self.revisar_pie('z_abajo_q')
                x = self.posicion[0]
                y = self.posicion[1] + 6
            elif 30 <= angulo <= 60:
                self.revisar_pie('z_dabajo_q')
                x = self.posicion[0] - 6 * cos(radians(self.angulo))
                y = self.posicion[1] + 6 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('z_izq_q')
                x = self.posicion[0] - 6
                y = self.posicion[1]
        elif dif_x < 0 and dif_y < 0:
            self.puntero = [-1, -1]
            if angulo > 60:
                self.revisar_pie('z_abajo_q')
                x = self.posicion[0]
                y = self.posicion[1] + 6
            elif 30 <= angulo <= 60:
                self.revisar_pie('z_ddere_q')
                x = self.posicion[0] + 6 * cos(radians(self.angulo))
                y = self.posicion[1] + 6 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('z_dere_q')
                x = self.posicion[0] + 6
                y = self.posicion[1]
        elif dif_x < 0 < dif_y:
            self.puntero = [-1, 1]
            if angulo > 60:
                self.revisar_pie('z_arriba_q')
                x = self.posicion[0]
                y = self.posicion[1] - 6
            elif 30 <= angulo <= 60:
                self.revisar_pie('z_darriba_q')
                x = self.posicion[0] + 6 * cos(radians(self.angulo))
                y = self.posicion[1] - 6 * sin(radians(self.angulo))
            elif 0 <= angulo <= 30:
                self.revisar_pie('z_dere_q')
                x = self.posicion[0] + 6
                y = self.posicion[1]
        self.posicion=[x,y]

    def revisar_pie(self,imagen):
        if self.imagen==imagen:
            if self.imagen[-1] == 'q':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'd'))
                self.imagen = self.imagen[:-1] + 'd'
                self.imagen_l.setPixmap(foto2)
            elif self.imagen[-1] == 'd':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'i'))
                self.imagen = self.imagen[:-1] + 'i'
                self.imagen_l.setPixmap(foto2)
            elif self.imagen[-1] == 'i':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'q'))
                self.imagen = self.imagen[:-1] + 'q'
                self.imagen_l.setPixmap(foto2)
        else:
            foto = QtGui.QPixmap('{}.png'.format(imagen))
            self.imagen = imagen
            self.imagen_l.setPixmap(foto)


class Character(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv
    # TENDRIA MAS SENTIDO QUE ESTE ATRIBUTO NO FUESE ESTATICO?
    #   Intentenlo en casa...
    #   spoiler: PyQt4-KHEEE?

    def __init__(self, parent, path, x, y, wait):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.ventana=parent
        self.image = QtGui.QLabel(parent)
        self.image.setPixmap(QtGui.QPixmap(path))
        self.image.adjustSize()
        self.image.show()
        self.trigger.connect(parent.actualizarImagen)
        self.numero=randint(0,800)
        self.numero2=randint(0,600)
        self.zombie=Zombie(self.numero,self.numero2,self.image)
        self.__position = (self.numero, self.numero2)
        self.wait = wait

        # esta linea se ve inocente
        # pero va a mandar una senhal (evento) a la ventana
        self.position = (x, y)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1]
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def run(self):
        a=True
        while a is True:
            time.sleep(0.1)
            self.position = (self.numero+1, self.numero2+5)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = MainWindow()
    ventana.show()
    for i in range(10):
        personaje = Character(
            parent=ventana,
            path="zombie/z_arriba_q.png",
            x=0, y=0,
            wait=3*(9-i)
        )
        personaje.start()
    app.exec_()

