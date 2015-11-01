__author__ = 'JuanFrancisco'
from math import atan, degrees,radians,cos,sin

from PyQt4 import QtGui, uic, QtCore

form = uic.loadUiType("juego.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('pasto.png')
        self.label.setPixmap(foto)
        foto2 = QtGui.QPixmap('p_arriba_q.png')
        self.label_2.setPixmap(foto2)
        puntero = QtGui.QPixmap('puntero.png')
        self.label_3.setPixmap(puntero)
        self.label_3.move(100, 200)
        self.posicion = [300, 200]
        self.puntero=[0,0]
        self.angulo=0
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
            x=self.posicion[0]+10*self.puntero[0]*cos(radians(self.angulo))
            self.label_2.move(x, 200)
            self.posicion=[x,200]
            print('Presione A o izq')
        elif QKeyEvent.key() == QtCore.Qt.Key_S or QKeyEvent.key() == QtCore.Qt.Key_Down:
            print('Presione S o abajo')
        elif QKeyEvent.key() == QtCore.Qt.Key_D or QKeyEvent.key() == QtCore.Qt.Key_Right:
            print('Presione D o derecha')
        elif QKeyEvent.key() == QtCore.Qt.Key_W or QKeyEvent.key() == QtCore.Qt.Key_Up:
            print('Presione W o arriba')


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
        if dif_x >= 0 and dif_y >= 0:
            self.puntero=[1,1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_arriba_q.png')
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_dizq_q.png')
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_izq_q.png')
                self.label_2.setPixmap(foto)
        elif dif_y < 0 <= dif_x:
            self.puntero=[1,-1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_abajo_q.png')
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_dabajo_q.png')
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_izq_q.png')
                self.label_2.setPixmap(foto)
        elif dif_x < 0 and dif_y < 0:
            self.puntero=[-1,-1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_abajo_q.png')
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_ddere_q.png')
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_dere_q.png')
                self.label_2.setPixmap(foto)
        elif dif_x < 0 < dif_y:
            self.puntero=[-1,1]
            if angulo > 60:
                foto = QtGui.QPixmap('p_arriba_q.png')
                self.label_2.setPixmap(foto)
            elif 30 <= angulo <= 60:
                foto = QtGui.QPixmap('p_darriba_q.png')
                self.label_2.setPixmap(foto)
            elif 0 <= angulo <= 30:
                foto = QtGui.QPixmap('p_dere_q.png')
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
