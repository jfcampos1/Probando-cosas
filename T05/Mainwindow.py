__author__ = 'JuanFrancisco'
from math import atan, degrees, radians, cos, sin
from Cdisparos import DisparoTread
from PyQt4 import QtGui, uic, QtCore



form = uic.loadUiType("juego.ui")


class MainWindow(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Survival Game")
        foto = QtGui.QPixmap('pasto.png')
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
        self.label_3.setPixmap(puntero)
        self.label_3.move(100, 200)
        self.posicion = [300, 200]
        self.puntero = [0, 0]
        self.angulo = 0
        self.label_2.move(300, 200)
        self.tipo = 'jugador'
        self.actualizar_mapa(300, 200, self)
        self.vida = 100
        self.label_5.setText(str(self.vida))

    def actualizar_mapa(self, x, y, objeto):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                self.mapa[i][n] = objeto

    def actualizar_mapa_disparo(self, x, y, objeto,borrar):
        for i in range(y, y + 20):
            for n in range(x, x + 20):
                if borrar is True:
                    self.mapa[i][n] = ''
                else:
                    self.mapa[i][n] = objeto

    def borrar_del_mapa(self, objeto, x, y):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                if i>len(self.mapa)-1 or n>len(self.mapa[0])-1 or 0>i or 0>n:
                    pass
                elif self.mapa[i][n] == objeto:
                    self.mapa[i][n] = ''

    def revisar_mapa(self, x, y):
        for i in range(y, y + 50):
            for n in range(x, x + 50):
                if i>len(self.mapa)-1 or n>len(self.mapa[0])-1 or 0>i or 0>n:
                    a='fuera'
                    return a
                elif self.mapa[i][n] != '':
                    return self.mapa[i][n]
        return True

    def revisar_mapa_disparo(self, x, y):
        for i in range(y, y + 20):
            for n in range(x, x + 20):
                if i>len(self.mapa)-1 or n>len(self.mapa[0])-1 or 0>i or 0>n:
                    a='fuera'
                    return a
                if self.mapa[i][n] != '':
                    return self.mapa[i][n]
        return True

    def actualizarImagen(self, myImageEvent):
        foto2 = QtGui.QPixmap('{}.png'.format(myImageEvent.imagen))
        label = myImageEvent.image
        label.resize(50, 50)
        label.setPixmap(foto2)
        label.adjustSize()
        label.move(myImageEvent.x, myImageEvent.y)

    def actualizarImagendisparo(self, myImageEvent):
        foto2 = QtGui.QPixmap('{}.png'.format(myImageEvent.imagen))
        label = myImageEvent.image
        label.resize(50, 50)
        label.setPixmap(foto2)
        label.adjustSize()
        label.move(myImageEvent.x, myImageEvent.y)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            print("Presionarion ENTER!")
        elif QKeyEvent.key() == QtCore.Qt.Key_Space:
            print('Presione espacio')
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            QtCore.QCoreApplication.instance().quit()
            print('Presione esc')
        elif QKeyEvent.key() == QtCore.Qt.Key_A or QKeyEvent.key() == QtCore.Qt.Key_Left or QKeyEvent.key() == QtCore.Qt.Key_1:
            self.mover(1, 4 / 5)
            print('Presione A o izq')
        elif QKeyEvent.key() == QtCore.Qt.Key_S or QKeyEvent.key() == QtCore.Qt.Key_Down or QKeyEvent.key() == QtCore.Qt.Key_5:
            self.mover(-1, -1 / 2)
            print('Presione S o abajo')
        elif QKeyEvent.key() == QtCore.Qt.Key_D or QKeyEvent.key() == QtCore.Qt.Key_Right or QKeyEvent.key() == QtCore.Qt.Key_3:
            self.mover(1, -4 / 5)
            print('Presione D o derecha')
        elif QKeyEvent.key() == QtCore.Qt.Key_W or QKeyEvent.key() == QtCore.Qt.Key_Up or QKeyEvent.key() == QtCore.Qt.Key_2:
            self.mover(-1, 1)
            print('Presione W o arriba')

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
            elif vacio=='fuera':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
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
            elif vacio=='fuera':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)
            elif vacio.tipo == 'zombie':
                self.actualizar_mapa(int(self.posicion[0]), int(self.posicion[1]), self)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            self.bala=DisparoTread(self)
            print('aquiiiiiiiiiiiiiiiiiii')
            self.bala.start()
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
        print(self.puntero)

        print(int(dif_x), int(dif_y))

        # def closeEvent(self, QCloseEvent):
        #     ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        #     if ans == QtGui.QMessageBox.Yes:
        #         QCloseEvent.accept()
        #     else:
        #         QCloseEvent.ignore()

# if __name__ == '__main__':
#     app = QtGui.QApplication([])
#     app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
#     form = MainWindow()
#     form.show()
#     app.exec_()
