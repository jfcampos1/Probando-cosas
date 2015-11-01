__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, QtCore


class Ventana(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            print("Presionarion ENTER!")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            print("Hizo click izquierdo!")

    def mouseMoveEvent(self, QMouseEvent):
        boton = QMouseEvent.buttons()
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        print(x, y)

    def closeEvent(self, QCloseEvent):
        ans = QtGui.QMessageBox.question(self, "Titulo", "Salir?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    ventana = Ventana()
    ventana.show()
    app.exec_()
