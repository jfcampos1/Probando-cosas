__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic,QtCore

form = uic.loadUiType("pausa.ui")


class Perdiste(form[0], form[1]):

    def __init__(self,ventana,inicio,cronometro):
        super().__init__()
        self.setupUi(self)
        # foto=QtGui.QPixmap('fondo2.png')
        # self.label.setPixmap(foto)
        self.pushButton.setText('GAME OVER')
        self.pushButton.setStyleSheet("background-color: transparent")
        self.pushButton_2.clicked.connect(self.botonreiniciar)
        self.pushButton_3.clicked.connect(self.botonmenu)
        self.pushButton_4.clicked.connect(self.botonsalir)
        self.respuesta=0
        self.ventana=ventana
        self.inicio=inicio
        self.cronometro=cronometro
        self.setWindowTitle("GAME OVER")

    def botonjugar(self):
        self.ventana.pausa()
        self.hide()
        self.cronometro.Start()
        print('apretaron jugar')

    def botonmenu(self):
        self.ventana.hide()
        self.hide()
        self.cronometro.hide()
        self.cronometro.Reset()
        self.inicio.show()
        print('apretaron instrucciones')

    def botonreiniciar(self):
        self.hide()
        self.ventana.hide()
        self.cronometro.hide()
        self.cronometro.Reset()
        self.inicio.mapa.reinicio(self.ventana.fondo)

    def botonsalir(self):
        print('apretaron salir')
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            self.botonreiniciar()
            print('Presione espacio')
        # elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
        #     self.botonsalir()
        #     print('Presione esc')

    def closeEvent(self, QCloseEvent):
            QCloseEvent.accept()
            self.ventana.pausa()
            self.cronometro.Start()
