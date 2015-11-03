__author__ = 'JuanFrancisco'
from math import atan, degrees, radians, cos, sin

from PyQt4 import QtGui, uic, QtCore

form = uic.loadUiType("juego.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('pasto.png')
        self.label.setPixmap(foto)
        foto2 = QtGui.QPixmap('p_arriba_q.png')
        self.imagen = 'p_arriba_q'
        self.label_2.setPixmap(foto2)
        puntero = QtGui.QPixmap('puntero.png')
        self.label_3.setPixmap(puntero)
        self.label_3.move(100, 200)
        self.posicion = [300, 200]
        self.puntero = [0, 0]
        self.angulo = 0
        self.label_2.move(300, 200)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            print("Presionarion ENTER!")
        elif QKeyEvent.key() == QtCore.Qt.Key_Space:
            print('Presione espacio')
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            QtCore.QCoreApplication.instance().quit()
            print('Presione esc')
        elif QKeyEvent.key() == QtCore.Qt.Key_A or QKeyEvent.key() == QtCore.Qt.Key_Left:
            self.mover(1, 4 / 5)
            print('Presione A o izq')
        elif QKeyEvent.key() == QtCore.Qt.Key_S or QKeyEvent.key() == QtCore.Qt.Key_Down:
            self.mover(-1, -1 / 2)
            print('Presione S o abajo')
        elif QKeyEvent.key() == QtCore.Qt.Key_D or QKeyEvent.key() == QtCore.Qt.Key_Right:
            self.mover(1, -4 / 5)
            print('Presione D o derecha')
        elif QKeyEvent.key() == QtCore.Qt.Key_W or QKeyEvent.key() == QtCore.Qt.Key_Up:
            self.mover(-1, 1)
            print('Presione W o arriba')

    def mover(self, sentido, numero):
        if sentido == 1:
            x = 0
            y = 0
            if self.puntero[0] == -1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + 10 * numero * cos(radians(self.angulo))
                    y = self.posicion[1] - 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] + numero * 10
                        y = self.posicion[1]
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] - 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] - numero * 10
                        y = self.posicion[1]
                if self.angulo < 30:
                    x = self.posicion[0]
                    y = self.posicion[1] - numero * 10
            elif self.puntero[0] == 1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] + 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] + 10 * numero
                        y = self.posicion[1]
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] + numero * 10 * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0] - numero * 10
                        y = self.posicion[1]
                if self.angulo < 30:
                    x = self.posicion[0]
                    y = self.posicion[1] + numero * 10
            self.label_2.move(x, y)
            self.posicion = [x, y]
        elif sentido == -1:
            x = 0
            y = 0
            if self.puntero[0] == -1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] + 10 * numero * cos(radians(self.angulo))
                    y = self.posicion[1] + 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] + numero * 10
                elif self.puntero[1] == 1:
                    x = self.posicion[0] + numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] - 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] - numero * 10
                if self.angulo < 30:
                    x = self.posicion[0] + numero * 10
                    y = self.posicion[1]
            elif self.puntero[0] == 1:
                if self.puntero[1] == -1:
                    x = self.posicion[0] - numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] + 10 * numero * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] + 10 * numero
                elif self.puntero[1] == 1:
                    x = self.posicion[0] - numero * 10 * cos(radians(self.angulo))
                    y = self.posicion[1] - numero * 10 * sin(radians(self.angulo))
                    if self.angulo >= 60:
                        x = self.posicion[0]
                        y = self.posicion[1] - numero * 10
                if self.angulo < 30:
                    x = self.posicion[0] - numero * 10
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
            self.label_2.move(x, y)
            self.posicion = [x, y]

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            print("Hizo click izquierdo!")
        elif QMouseEvent.buttons() == QtCore.Qt.RightButton:
            print("Hizo click derecho!")

    def mouseMoveEvent(self, QMouseEvent):
        boton = QMouseEvent.buttons()
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        self.label_3.move(x, y)
        dif_x = self.posicion[0] - x
        dif_y = self.posicion[1] - y
        tg = abs(dif_y) / abs(dif_x)
        angulo = degrees(atan(tg))
        self.angulo = angulo
        if dif_x >= 0 and dif_y >= 0:
            self.puntero = [1, 1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_arriba_q.png')
                self.imagen = 'p_arriba_q'
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_dizq_q.png')
                self.imagen = 'p_dizq_q'
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_izq_q.png')
                self.imagen = 'p_izq_q'
                self.label_2.setPixmap(foto)
        elif dif_y < 0 <= dif_x:
            self.puntero = [1, -1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_abajo_q.png')
                self.imagen = 'p_abajo_q'
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_dabajo_q.png')
                self.imagen = 'p_dabajo_q'
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_izq_q.png')
                self.imagen = 'p_izq_q'
                self.label_2.setPixmap(foto)
        elif dif_x < 0 and dif_y < 0:
            self.puntero = [-1, -1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_abajo_q.png')
                self.imagen = 'p_abajo_q'
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_ddere_q.png')
                self.imagen = 'p_ddere_q'
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_dere_q.png')
                self.imagen = 'p_dere_q'
                self.label_2.setPixmap(foto)
        elif dif_x < 0 < dif_y:
            self.puntero = [-1, 1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_arriba_q.png')
                self.imagen = 'p_arriba_q'
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_darriba_q.png')
                self.imagen = 'p_darriba_q'
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_dere_q.png')
                self.imagen = 'p_dere_q'
                self.label_2.setPixmap(foto)
        print(self.puntero)

        print(dif_x, dif_y)

        # def closeEvent(self, QCloseEvent):
        #     ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        #     if ans == QtGui.QMessageBox.Yes:
        #         QCloseEvent.accept()
        #     else:
        #         QCloseEvent.ignore()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
    form = MainWindow()
    form.show()
    app.exec_()
