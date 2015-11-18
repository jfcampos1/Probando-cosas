__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore

form = uic.loadUiType("pausa.ui")


class Pausa(form[0], form[1]):
    def __init__(self, ventana, inicio, cronometro):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.botonjugar)
        self.pushButton_2.clicked.connect(self.botonreiniciar)
        self.pushButton_3.clicked.connect(self.botonmenu)
        self.pushButton_4.clicked.connect(self.botonsalir)
        self.respuesta = 0
        self.ventana = ventana
        self.inicio = inicio
        self.cronometro = cronometro
        self.setWindowTitle("Pausa")

    def botonjugar(self):
        self.ventana.pausa()
        self.hide()
        self.cronometro.Start()

    def botonmenu(self):
        self.ventana.hide()
        self.hide()
        self.cronometro.hide()
        self.cronometro.Reset()
        self.inicio.show()
        self.ventana.media.stop()
        self.inicio.mediaObject.play()

    def botonreiniciar(self):
        self.hide()
        self.ventana.hide()
        self.cronometro.hide()
        self.cronometro.Reset()
        self.ventana.vida = 0
        self.inicio.mapa.reinicio(self.ventana.fondo)

    def botonsalir(self):
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            self.ventana.media.stop()
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.botonjugar()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.botonsalir()

    def closeEvent(self, QCloseEvent):
        QCloseEvent.accept()
        self.ventana.pausa()
        self.cronometro.Start()
