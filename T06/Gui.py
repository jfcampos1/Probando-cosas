__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore


form = uic.loadUiType("log-in.ui")


class Login(form[0], form[1]):
    def __init__(self, cliente,nueva):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('water-drop.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonsalir)
        self.pushButton_2.clicked.connect(self.botonaceptar)
        self.pushButton_3.clicked.connect(self.botonnueva)
        self.pushButton_3.setStyleSheet("background-color: transparent")
        self.cliente = cliente
        self.nueva=nueva
        self.setWindowTitle("DrobPox")

    def actualizarimagen(self,actualizar):
        mensaje = actualizar.texto
        accion=actualizar.accion
        if accion == '001':
            self.label_4.setText(mensaje)
        elif accion == '002':
            self.label_4.setText(mensaje)
            self.hide()
            self.cliente.gucliente.show()
        elif accion == '004':
            self.nueva.label_4.setText(mensaje)
        elif accion == '006':
            self.nueva.hide()
            self.show()
            self.label_4.setText(mensaje)

    def botonaceptar(self):
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
            usuario = self.lineEdit.text()
            clave = self.lineEdit_2.text()
            if usuario.find(':') != -1 or clave.find(':') != -1:
                self.label_4.setText('Usuario o clave no pueden contener dos puntos ":"')
            else:
                print('aca')
                self.cliente.enviar('005:' + usuario + ':' + clave)
        else:
            self.label_4.setText('Usuario o clave incorrectos')

    def botonnueva(self):
        self.label_4.setText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.hide()
        self.nueva.show()

    def hide_login(self):
        self.nueva.hide()
        self.show()

    def botonsalir(self):
        ans = QtGui.QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            self.cliente.enviar('quit')
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.botonaceptar()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.botonsalir()

    def closeEvent(self, QCloseEvent):
        self.botonsalir()


class NuevaCuenta(form[0], form[1]):
    def __init__(self, cliente):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('water-drop.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonsalir)
        self.pushButton_2.clicked.connect(self.botonaceptar)
        self.pushButton_3.clicked.connect(self.botonatras)
        self.pushButton_3.setText('Atras')
        self.cliente = cliente
        self.setWindowTitle("Nueva Cuenta")

    def botonaceptar(self):
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
            usuario = self.lineEdit.text()
            clave = self.lineEdit_2.text()
            if usuario.find(':') != -1 or clave.find(':') != -1:
                self.label_4.setText('Usuario o clave no pueden contener dos puntos ":"')
            else:
                self.cliente.enviar('003:' + usuario + ':' + clave)
                self.label_4.setText('')
        else:
            self.label_4.setText('Usuario o clave incorrectos')

    def botonatras(self):
        self.label_4.setText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.hide()
        self.login.show()

    def botonsalir(self):
        ans = QtGui.QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                         QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            self.login.cliente.enviar('quit')
            QtCore.QCoreApplication.instance().quit()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.botonaceptar()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.botonsalir()

    def closeEvent(self, QCloseEvent):
        self.botonsalir()
