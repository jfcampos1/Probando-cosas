__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, uic, QtCore

form = uic.loadUiType("log-in.ui")


class Cuenta(form[0], form[1]):
    def __init__(self, cliente):
        super().__init__()
        self.setupUi(self)
        foto = QtGui.QPixmap('water-drop.png')
        self.label.setPixmap(foto)
        self.pushButton.clicked.connect(self.botonsalir)
        self.pushButton_2.clicked.connect(self.botonaceptar)
        self.pushButton_3.clicked.connect(self.botonnueva)
        self.pushButton_3.setStyleSheet("background-color: transparent")
        self.pushButton_2.setText('Enviar')
        self.pushButton_3.setText('Nuevo archivo')
        self.label_2.setText('Padre')
        self.label_3.setText('archivo:')
        self.cliente = cliente
        self.setWindowTitle("DrobPox")

    def botonaceptar(self):
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
            usuario = self.lineEdit.text()
            clave = self.lineEdit_2.text()
            self.cliente.enviar('009:' + usuario + ':' + clave)

    def botonnueva(self):
        fileName = QtGui.QFileDialog.getOpenFileNames(self, 'Dialog Title', '/path/to/default/directory') #getExistingDirectory
        if fileName:
            print(fileName)

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
