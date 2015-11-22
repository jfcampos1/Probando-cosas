__author__ = 'JuanFrancisco'
from PyQt4 import QtGui
from Gui_cliente import Cuenta
lista=[1]
print(lista[int('-1')])
strin='hola'
print(strin.find('u'))
print(type(strin.find('u')))
app = QtGui.QApplication([])
client = Cuenta('hola')
client.show()
app.exec_()