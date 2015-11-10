__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore

form = uic.loadUiType("instrucciones.ui")


class Instrucciones(form[0], form[1]):
    def __init__(self, ventana):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('Instrucciones-Juego2.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonatras)
        self.inicio = ventana

    def botonatras(self):
        self.hide()
        self.inicio.show()

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
