__author__ = 'JuanFrancisco'
from math import atan, degrees, radians, cos, sin
from random import uniform
from PyQt4.phonon import Phonon
from PyQt4 import QtGui, uic, QtCore

from Pausa import Pausa
from Ctiempo import main
from Cdisparos import DisparoTread

form = uic.loadUiType("juego.ui")


class MainWindow(form[0], form[1]):
    def __init__(self, fondo, inicio):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Survival Game")
        self.fondo = fondo
        foto = QtGui.QPixmap(fondo)
        self.label.setPixmap(foto)
        self.label_2.resize(50, 50)
        foto2 = QtGui.QPixmap('personaje/p_arriba_q.png')
        self.imagen = 'personaje/p_arriba_q'
        self.label_2.setPixmap(foto2)
        puntero = QtGui.QPixmap('puntero.png')
        mapa = []
        for i in range(600):
            mapa.append([''] * 800)
        self.mapa = mapa
        # self.label_3.setPixmap(puntero)
        # self.label_3.move(100, 200)
        self.posicion = [300, 200]
        self.puntero = [0, 0]
        self.angulo = 0
        self.label_2.move(300, 200)
        self.tipo = 'jugador'
        self.actualizar_mapa(300, 200, self)
        self.vida = 100
        self.balas = 20
        self.label_4.setText(str(self.balas))
        self.label_5.setText(str(self.vida))
        self.barra2 = self.progressBar_2
        self.tiempo = 0
        self.cronometro = main(self)
        self.cronometro.show()
        self.cronometro.Start()
        self.barra = self.progressBar
        self.setGeometry(300, 100, 800, 600)
        self.inicio = inicio
        self.paus = Pausa(self, self.inicio, self.cronometro)
        self.prox_supply = 0
        self.prox_supply_ocupado = False
        self.score=0
        self.zombies_muertos=0
        self.pushButton.clicked.connect(self.esc)
        self.playsong()


    def actualizar_mapa(self, x, y, objeto):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                if i > len(self.mapa) - 1 or n > len(self.mapa[0]) - 1 or 0 > i or 0 > n:
                    pass
                else:
                    self.mapa[i][n] = objeto

    def actualizar_mapa_disparo(self, x, y, objeto, borrar):
        for i in range(y, y + 20):
            for n in range(x, x + 20):
                if borrar is True:
                    self.mapa[i][n] = ''
                else:
                    self.mapa[i][n] = objeto

    def borrar_del_mapa(self, objeto, x, y):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                if i > len(self.mapa) - 1 or n > len(self.mapa[0]) - 1 or 0 > i or 0 > n:
                    pass
                elif self.mapa[i][n] == objeto:
                    self.mapa[i][n] = ''

    def revisar_mapa(self, x, y):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                if i > len(self.mapa) - 1 or n > len(self.mapa[0]) - 1 or 0 > i or 0 > n:
                    a = 'fuera'
                    return a
                elif self.mapa[i][n] != '':
                    return self.mapa[i][n]
        return True

    def revisar_mapa_disparo(self, x, y):
        for i in range(y, y + 20):
            for n in range(x, x + 20):
                if i > len(self.mapa) - 1 or n > len(self.mapa[0]) - 1 or 0 > i or 0 > n:
                    a = 'fuera'
                    return a
                if self.mapa[i][n] != '':
                    return self.mapa[i][n]
        return True
    def playsong(self):
        self.media = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media, self.audioOutput)
        self.media.setCurrentSource(Phonon.MediaSource('musicajuegos.mp3'))
        self.media.play()

    def playdisparo(self):
        self.media2 = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media2, self.audioOutput)
        self.media2.setCurrentSource(Phonon.MediaSource('disparo.mp3'))
        self.media2.play()

    def actualizarImagen(self, myImageEvent):
        label = myImageEvent.image
        self.barra.setValue(self.vida)
        self.label_5.setText(str(self.vida))
        self.barra2.setValue(self.balas)
        self.label_4.setText(str(self.balas))
        self.label_7.setText(str(self.score))
        if myImageEvent.vida is True:
            foto2 = QtGui.QPixmap('{}.png'.format(myImageEvent.imagen))
            label.resize(50, 50)
            label.setPixmap(foto2)
            label.adjustSize()
            label.move(myImageEvent.x, myImageEvent.y)
        else:
            self.zombies_muertos+=1
            tiempo = self.cronometro.time.split(':')
            minutos = int(tiempo[1]) + 1
            self.score=minutos*self.zombies_muertos+int(tiempo[2])*self.zombies_muertos
            label.close()
            label.destroy()

    def actualizarImagendisparo(self, myImageEvent):
        label = myImageEvent.image
        if myImageEvent.vida is True:
            foto2 = QtGui.QPixmap('{}.png'.format(myImageEvent.imagen))
            label.resize(50, 50)
            label.setPixmap(foto2)
            label.adjustSize()
            label.move(myImageEvent.x, myImageEvent.y)
        else:
            label.close()
            label.destroy()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            pass
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape or QKeyEvent.key() == QtCore.Qt.Key_P or \
                        QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.esc()
        elif QKeyEvent.key() == QtCore.Qt.Key_A or QKeyEvent.key() == QtCore.Qt.Key_Left or \
                        QKeyEvent.key() == QtCore.Qt.Key_1:
            if self.tiempo == 0:
                self.mover(1, 4 / 5)
        elif QKeyEvent.key() == QtCore.Qt.Key_S or QKeyEvent.key() == QtCore.Qt.Key_Down or \
                        QKeyEvent.key() == QtCore.Qt.Key_5:
            if self.tiempo == 0:
                self.mover(-1, -1 / 2)
        elif QKeyEvent.key() == QtCore.Qt.Key_D or QKeyEvent.key() == QtCore.Qt.Key_Right or \
                        QKeyEvent.key() == QtCore.Qt.Key_3:
            if self.tiempo == 0:
                self.mover(1, -4 / 5)
        elif QKeyEvent.key() == QtCore.Qt.Key_W or QKeyEvent.key() == QtCore.Qt.Key_Up or \
                        QKeyEvent.key() == QtCore.Qt.Key_2:
            if self.tiempo == 0:
                self.mover(-1, 1)

    def pausa(self):
        if self.tiempo != 0:
            self.tiempo = 0
        else:
            self.tiempo = 1

    def mover(self, sentido, numero):
        if sentido == 1:
            x = 0
            y = 0
            if self.puntero[0] == -1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + 6 * numero * cos(radians(self.angulo))
                    y = self.posicion[1] - 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] + numero * 6
                        y = self.posicion[1]
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] - 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] - numero * 6
                        y = self.posicion[1]
                if self.angulo < 30:
                    x = self.posicion[0]
                    y = self.posicion[1] - numero * 6
            elif self.puntero[0] == 1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] + 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] + 6 * numero
                        y = self.posicion[1]
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] + numero * 6 * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] - numero * 6
                        y = self.posicion[1]
                if self.angulo < 30:
                    x = self.posicion[0]
                    y = self.posicion[1] + numero * 6
            self.borrar_del_mapa(self, int(self.posicion[0]), int(self.posicion[1]))
            vacio = self.revisar_mapa(int(x), int(y))
            if vacio is True:
                self.posicion = [x, y]
                self.actualizar_mapa(int(x), int(y), self)
                self.label_2.move(x, y)
            elif vacio == 'fuera':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
            elif vacio.tipo == 'supply':
                self.posicion = [x, y]
                self.actualizar_mapa(int(x), int(y), self)
                self.label_2.move(x, y)
            elif vacio.tipo == 'zombie':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
        elif sentido == -1:
            x = 0
            y = 0
            if self.puntero[0] == -1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + 6 * numero * cos(radians(self.angulo))
                    y = self.posicion[1] + 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] + numero * 6
                elif self.puntero[1] == 1:
                    x = self.posicion[0] + numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] - 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] - numero * 6
                if self.angulo < 30:
                    x = self.posicion[0] + numero * 6
                    y = self.posicion[1]
            elif self.puntero[0] == 1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] - numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] + 6 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] + 6 * numero
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 6 * cos(radians(self.angulo))
                    y = self.posicion[1] - numero * 6 * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] - numero * 6
                if self.angulo < 30:
                    x = self.posicion[0] - numero * 6
                    y = self.posicion[1]
            if self.imagen[-1] == 'q':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'd'))
                self.imagen = self.imagen[:-1] + 'd'
                self.label_2.setPixmap(foto2)
            elif self.imagen[-1] == 'd':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'i'))
                self.imagen = self.imagen[:-1] + 'i'
                self.label_2.setPixmap(foto2)
            elif self.imagen[-1] == 'i':
                foto2 = QtGui.QPixmap('{}{}.png'.format(self.imagen[:-1], 'q'))
                self.imagen = self.imagen[:-1] + 'q'
                self.label_2.setPixmap(foto2)
            self.borrar_del_mapa(self, int(self.posicion[0]), int(self.posicion[1]))
            vacio = self.revisar_mapa(int(x), int(y))
            if vacio is True:
                self.posicion = [x, y]
                self.actualizar_mapa(int(x), int(y), self)
                self.label_2.move(x, y)
            elif vacio == 'fuera':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
            elif vacio.tipo == 'supply':
                self.posicion = [x, y]
                self.actualizar_mapa(int(x), int(y), self)
                self.label_2.move(x, y)
            elif vacio.tipo == 'zombie':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            if self.tiempo == 0:
                if self.balas != 0:
                    self.playdisparo()
                    self.bala = DisparoTread(self)
                    self.bala.start()
                    self.balas -= 1

    def tiempo_aparicion_zombies(self):
        tiempo = self.cronometro.time.split(':')
        minutos = int(tiempo[1]) + 1
        self.score=minutos*self.zombies_muertos+int(tiempo[2])*self.zombies_muertos
        if int(tiempo[2]) % 3 == 0:
            return minutos
        return False

    def aparicion_suplementos(self):
        if self.prox_supply_ocupado is False:
            siguiente_tiempo = int(uniform(5, 20))
            self.prox_supply += siguiente_tiempo
            self.prox_supply_ocupado = True

    def mouseMoveEvent(self, QMouseEvent):
        if self.tiempo == 0:
            boton = QMouseEvent.buttons()
            x = QMouseEvent.x()
            y = QMouseEvent.y()
            # self.label_3.move(x, y)
            dif_x = self.posicion[0] - x
            dif_y = self.posicion[1] - y
            tg = 0
            try:
                tg = abs(dif_y) / abs(dif_x)
            except ZeroDivisionError:
                tg = 0
            angulo = degrees(atan(tg))
            self.angulo = angulo
            if dif_x >= 0 and dif_y >= 0:
                self.puntero = [1, 1]
                if angulo > 60:
                    foto = QtGui.QPixmap('personaje/p_arriba_q.png')
                    self.imagen = 'personaje/p_arriba_q'
                    self.label_2.setPixmap(foto)
                elif 30 <= angulo <= 60:
                    foto = QtGui.QPixmap('personaje/p_dizq_q.png')
                    self.imagen = 'personaje/p_dizq_q'
                    self.label_2.setPixmap(foto)
                elif 0 <= angulo <= 30:
                    foto = QtGui.QPixmap('personaje/p_izq_q.png')
                    self.imagen = 'personaje/p_izq_q'
                    self.label_2.setPixmap(foto)
            elif dif_y < 0 <= dif_x:
                self.puntero = [1, -1]
                if angulo > 60:
                    foto = QtGui.QPixmap('personaje/p_abajo_q.png')
                    self.imagen = 'personaje/p_abajo_q'
                    self.label_2.setPixmap(foto)
                elif 30 <= angulo <= 60:
                    foto = QtGui.QPixmap('personaje/p_dabajo_q.png')
                    self.imagen = 'personaje/p_dabajo_q'
                    self.label_2.setPixmap(foto)
                elif 0 <= angulo <= 30:
                    foto = QtGui.QPixmap('personaje/p_izq_q.png')
                    self.imagen = 'personaje/p_izq_q'
                    self.label_2.setPixmap(foto)
            elif dif_x < 0 and dif_y < 0:
                self.puntero = [-1, -1]
                if angulo > 60:
                    foto = QtGui.QPixmap('personaje/p_abajo_q.png')
                    self.imagen = 'personaje/p_abajo_q'
                    self.label_2.setPixmap(foto)
                elif 30 <= angulo <= 60:
                    foto = QtGui.QPixmap('personaje/p_ddere_q.png')
                    self.imagen = 'personaje/p_ddere_q'
                    self.label_2.setPixmap(foto)
                elif 0 <= angulo <= 30:
                    foto = QtGui.QPixmap('personaje/p_dere_q.png')
                    self.imagen = 'personaje/p_dere_q'
                    self.label_2.setPixmap(foto)
            elif dif_x < 0 < dif_y:
                self.puntero = [-1, 1]
                if angulo > 60:
                    foto = QtGui.QPixmap('personaje/p_arriba_q.png')
                    self.imagen = 'personaje/p_arriba_q'
                    self.label_2.setPixmap(foto)
                elif 30 <= angulo <= 60:
                    foto = QtGui.QPixmap('personaje/p_darriba_q.png')
                    self.imagen = 'personaje/p_darriba_q'
                    self.label_2.setPixmap(foto)
                elif 0 <= angulo <= 30:
                    foto = QtGui.QPixmap('personaje/p_dere_q.png')
                    self.imagen = 'personaje/p_dere_q'
                    self.label_2.setPixmap(foto)

    def closeEvent(self, QCloseEvent):
        if self.tiempo == 0:
            self.cronometro.timer.stop()
        self.pausa()
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()
        else:
            self.cronometro.Start()
            self.pausa()
            QCloseEvent.ignore()

    def esc(self):
        if self.tiempo == 0:
            self.cronometro.timer.stop()
            self.paus.show()
        self.pausa()
