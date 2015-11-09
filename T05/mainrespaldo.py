__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, QtCore
from Mainwindow import MainWindow
from Zombies import Character


if __name__ == '__main__':
    app = QtGui.QApplication([])
    app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
    ventana = MainWindow()
    ventana.show()
    for i in range(10):
        personaje = Character(
            parent=ventana,
            path="zombie/z_arriba_q.png"
        )
        personaje.start()
    app.exec_()
