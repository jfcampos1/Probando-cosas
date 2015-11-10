__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore

from Intrucciones import Instrucciones
from mapas import Mapa

form = uic.loadUiType("Inicio.ui")


class Inicio(form[0], form[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('fondoinicio.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonjugar)
        self.pushButton_3.clicked.connect(self.botoninstrucciones)
        self.pushButton_2.clicked.connect(self.botonsalir)
        self.instrucciones = Instrucciones(self)
        self.mapa = Mapa(self)

    def botonjugar(self):
        self.hide()
        self.mapa.show()

    def botoninstrucciones(self):
        self.hide()
        self.instrucciones.show()

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


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = Inicio()
    form.show()
    app.exec_()
