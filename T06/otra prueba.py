__author__ = 'JuanFrancisco'
# coding=utf-8
# import sys
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
#
# def clickable(widget):
#
#     class Filter(QObject):
#
#         clicked = pyqtSignal()
#
#         def eventFilter(self, obj, event):
#
#             if obj == widget:
#                 if event.type() == QEvent.MouseButtonRelease:
#                     if obj.rect().contains(event.pos()):
#                         self.clicked.emit()
#                         # The developer can opt for .emit(obj) to get the object within the slot.
#                         return True
#
#             return False
#
#     filter = Filter(widget)
#     widget.installEventFilter(filter)
#     return filter.clicked
#
# class Window(QWidget):
#
#     def __init__(self, parent = None):
#
#         QWidget.__init__(self, parent)
#
#         label1 = QLabel(self.tr("Hello world!"))
#         label2 = QLabel(self.tr("ABC DEF GHI"))
#         label3 = QLabel(self.tr("Hello PyQt!"))
#
#         clickable(label1).connect(self.showText1)
#         clickable(label2).connect(self.showText2)
#         clickable(label3).connect(self.showText3)
#
#         layout = QHBoxLayout(self)
#         layout.addWidget(label1)
#         layout.addWidget(label2)
#         layout.addWidget(label3)
#
#     def showText1(self):
#         print ("Label 1 clicked")
#
#     def showText2(self):
#         print( "Label 2 clicked")
#
#     def showText3(self):
#         print ("Label 3 clicked")
#
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt4.QtGui import *
#
# class Window(QWidget):
#
#     def __init__(self, parent = None):
#
#         QWidget.__init__(self, parent)
#
#         label1 = QLabel(self.tr("Hello world!"))
#         label2 = QLabel(self.tr("ABC DEF GHI"))
#         label3 = QLabel(self.tr("Hello PyQt!"))
#
#         label1.mouseReleaseEvent = self.showText1
#         label2.mouseReleaseEvent = self.showText2
#         label3.mouseReleaseEvent = self.showText3
#
#         layout = QHBoxLayout(self)
#         layout.addWidget(label1)
#         layout.addWidget(label2)
#         layout.addWidget(label3)
#
#     def showText1(self, event):
#         print("Label 1 clicked")
#
#     def showText2(self, event):
#         print("Label 2 clicked")
#
#     def showText3(self, event):
#         print("Label 3 clicked")
#
#
# if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
from PyQt4 import QtGui, QtCore
from maspruebas import Window


class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        # Configura geometría de la ventana
        self.setWindowTitle('Ventana con Boton')
        self.setGeometry(200, 100, 300, 250)

        # Definición de acciones
        ver_status = QtGui.QAction(QtGui.QIcon(None), '&Cambiar Status', self)
        ver_status.setStatusTip('Este es un ítem de prueba')
        ver_status.triggered.connect(self.cambiar_status_bar)

        salir = QtGui.QAction(QtGui.QIcon(None), '&Salir', self)
        salir.setShortcut('Ctrl+Q') # permite usar combinación de teclas para ejecutar comandos
        salir.setStatusTip('Terminar la aplicación') # muestra en la barra de estados la descripción del comando
        salir.triggered.connect(QtGui.qApp.quit) # conecta la señal con el slot que manejará este evento


        # Creación de la barra de menús y de los menús
        menubar = self.menuBar()

        # primero menú
        archivo_menu = menubar.addMenu('&Archivo')
        archivo_menu.addAction(ver_status)
        archivo_menu.addAction(salir)

        # segundo menú
        otro_menu = menubar.addMenu('&Otro Menú')

        # Incluye la barra de estado'''
        self.statusBar().showMessage('Listo')

        # Configura como Widget Central el formulario creado anteriormente.
        self.form = Window()
        self.setCentralWidget(self.form)

    def cambiar_status_bar(self):
        self.statusBar().showMessage('Cambié el Status')


class MiFormulario(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        # Este método inicializa la interfaz y sus elementos

        self.label1 = QtGui.QLabel('Texto:', self)
        self.label1.move(10, 15)

        self.label2 = QtGui.QLabel('Aqui se escribe la respuesta', self)
        self.label2.move(10, 50)

        self.label3 = QtGui.QLabel('Origen de la señal: ', self)
        self.label3.move(10, 180)

        self.edit1 = QtGui.QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        self.boton1 = QtGui.QPushButton('&Procesar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)
        self.boton1.clicked.connect(self.boton1_callback)
        self.boton1.clicked.connect(self.boton_presionado)

    def boton_presionado(self):
        sender = self.sender()
        self.label3.setText('Origen de la señal: {0}'.format(sender.text()))
        self.label3.resize(self.label3.sizeHint())

    def boton1_callback(self):
        self.label2.setText('{}'.format(self.edit1.text()))
        self.label2.resize(self.label2.sizeHint())

if __name__ == '__main__':
    app = QtGui.QApplication([])

    # Se crea una ventana descendiente de QMainWindows
    form = MainForm()
    form.show()
    app.exec_()