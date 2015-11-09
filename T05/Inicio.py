__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic,QtCore

form = uic.loadUiType("Inicio.ui")


class Inicio(form[0], form[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        foto=QtGui.QPixmap('fondoinicio.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonjugar)
        self.pushButton_3.clicked.connect(self.botoninstrucciones)
        self.pushButton_2.clicked.connect(self.botonsalir)

    def botonjugar(self):
        print('apretaron jugar')

    def botoninstrucciones(self):
        print('apretaron instrucciones')

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

    def closeEvent(self, QCloseEvent):
            ans = QtGui.QMessageBox.question(self, "Zombie", "Salir del juego?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if ans == QtGui.QMessageBox.Yes:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()

if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = Inicio()
    form.show()
    app.exec_()