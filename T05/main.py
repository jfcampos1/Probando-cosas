__author__ = 'JuanFrancisco'
from PyQt4 import QtGui

from Inicio import Inicio

if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = Inicio()
    ventana.show()
    app.exec_()
