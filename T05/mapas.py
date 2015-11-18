__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore

from Mainwindow import MainWindow
from Zombies import Character

form = uic.loadUiType("mapas.ui")


class Mapa(form[0], form[1]):
    def __init__(self, ventana):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('instrucciones.png')
        self.label.setPixmap(foto)
        foto = QtGui.QPixmap('pasto.png')
        self.label_3.setPixmap(foto)
        foto = QtGui.QPixmap('fondo.png')
        self.label_4.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonatras)
        self.pushButton_2.setStyleSheet("background-color: transparent")
        self.pushButton_2.clicked.connect(self.botonmapa1)
        self.pushButton_3.setStyleSheet("background-color: transparent")
        self.pushButton_3.clicked.connect(self.botonmapa2)
        self.inicio = ventana

    def botonatras(self):
        self.hide()
        self.inicio.show()
        self.inicio.mediaObject.play()

    def botonmapa1(self):
        mapa = 'pasto.png'
        self.hide()
        self.juego = MainWindow(mapa, self.inicio)
        self.crear_zombies_iniciales(self.juego)
        self.juego.show()
        self.inicio.mediaObject.stop()
        self.juego.playsong()

    def botonmapa2(self):
        mapa = 'fondo.png'
        self.hide()
        self.juego = MainWindow(mapa, self.inicio)
        self.crear_zombies_iniciales(self.juego)
        self.juego.show()
        self.inicio.mediaObject.stop()
        self.juego.playsong()

    def reinicio(self, mapa):
        self.juego = MainWindow(mapa, self.inicio)
        self.crear_zombies_iniciales(self.juego)
        self.juego.show()

    def crear_zombies_iniciales(self, ventana):
        for i in range(10):
            self.personaje = Character(
                parent=ventana,
                path="zombie/z_arriba_q.png"
            )
            self.personaje.start()

    def botonsalir(self):
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.botonsalir()

    def closeEvent(self, QCloseEvent):
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
