__author__ = 'JuanFrancisco'
# coding=utf-8
import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtGui.QVBoxLayout(self)
        chat=QtGui.QHBoxLayout(self)
        self.button = QtGui.QPushButton('Send')
        self.boton2=QtGui.QPushButton('Test2')
        self.texto = QtGui.QLineEdit(self)
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.edit)
        layout.addLayout(chat)
        chat.addWidget(self.texto)
        chat.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.handleTest)
        self.boton2.clicked.connect(self.cambiar_status_bar)

    def cambiar_status_bar(self):
        self.edit.append('hola')
    def handleTest(self):
        self.edit.append('spam: spam spam spam spam\na')


class Chat(QtGui.QMainWindow):
    def __init__(self, cliente,el_otro):
        super().__init__()

        # Configura geometría de la ventana
        self.setWindowTitle(el_otro)
        self.setGeometry(100, 200, 300, 400)
        self.cliente = cliente
        self.padre = 0
        self.form = Window()
        self.setCentralWidget(self.form)
        # Definición de acciones

        salir = QtGui.QAction(QtGui.QIcon(None), '&Salir', self)
        salir.setShortcut('Ctrl+Q')
        salir.setStatusTip('Terminar la aplicación')
        salir.triggered.connect(self.botonsalir)


        # Creación de la barra de menús y de los menús
        menubar = self.menuBar()

        # primero menú
        archivo_menu = menubar.addMenu('&Menu')
        archivo_menu.addAction(salir)

        # segundo menú

        # Incluye la barra de estado'''
        self.statusBar().showMessage('Listo')

    def cambiar_status_bar(self):
        self.edit.append('hola')

    def agregar_texto(self):
        self.form.edit.append(self.form.texto.text())
        self.form.texto.setText('')

    def botonsalir(self):
        ans = QtGui.QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                   QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            self.hide()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            self.agregar_texto()
        elif QKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.botonsalir()

    def closeEvent(self, QCloseEvent):
        self.botonsalir()
        QCloseEvent.ignore()


class Onlines(QtGui.QWidget):
    def __init__(self, cliente):

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Drobpox')
        self.cliente = cliente
        self.que = ''
        self.treeView = QtGui.QTreeView()
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.model = QtGui.QStandardItemModel()
        self.additems(self.model, self.cliente.conectados)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Online")])

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def init_GUI(self):
        self.model = QtGui.QStandardItemModel()
        self.additems(self.model, self.cliente.conectados)
        self.treeView.setModel(self.model)
        self.model.setHorizontalHeaderLabels([self.tr("Online")])

    def additems(self, parent, elements):
        for text in elements:
            if self.cliente.usuario!=text:
                item = QtGui.QStandardItem(text)
                parent.appendRow(item)

    def abrir_chat(self):
        self.nuevochat=Chat(self.cliente,self.que)
        self.nuevochat.show()

    def openMenu(self, position):

        indexes = self.treeView.selectedIndexes()
        ver_status = QtGui.QAction(QtGui.QIcon(None), '&Abrir Chat', self)
        ver_status.triggered.connect(self.abrir_chat)
        menu = QtGui.QMenu()
        if len(indexes) > 0:
            self.que = indexes[0].data()
            menu.addAction(ver_status)

        menu.exec_(self.treeView.viewport().mapToGlobal(position))