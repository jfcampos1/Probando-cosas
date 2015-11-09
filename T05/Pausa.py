__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic,QtCore

form = uic.loadUiType("pausa.ui")


class Pausa(form[0], form[1]):

    def __init__(self,ventana):
        super().__init__()
        self.setupUi(self)
        # foto=QtGui.QPixmap('fondo2.png')
        # self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonjugar)
        self.pushButton_2.clicked.connect(self.botonreiniciar)
        self.pushButton_3.clicked.connect(self.botonmenu)
        self.pushButton_4.clicked.connect(self.botonsalir)
        self.respuesta=0
        self.ventana=ventana

    def botonjugar(self):
        self.ventana.pausa()
        self.hide()
        print('apretaron jugar')

    def botonmenu(self):
        print('apretaron instrucciones')

    def botonreiniciar(self):
        print('apretaron reiniciar')

    def botonsalir(self):
        print('apretaron salir')
        ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Space:
            print('Presione espacio')
        # elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
        #     self.botonsalir()
        #     print('Presione esc')





if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = Pausa()
    form.show()
    app.exec_()
