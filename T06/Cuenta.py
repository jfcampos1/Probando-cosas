__author__ = 'JuanFrancisco'
# coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pickle


class Archivo:
    def __init__(self, archivo, nombre):
        self.archivo = archivo
        self.nombre = nombre


class MainForm(QMainWindow):
    def __init__(self,cliente):
        super().__init__()

        # Configura geometría de la ventana
        self.setWindowTitle('Ventana con Boton')
        self.setGeometry(500, 200, 300, 400)
        self.cliente=cliente
        self.form = Window(self.cliente)
        self.setCentralWidget(self.form)
        # Definición de acciones
        ver_status =QAction(QIcon(None), '&Cambiar Status', self)
        ver_status.setStatusTip('Este es un ítem de prueba')
        ver_status.triggered.connect(self.cambiar_status_bar)

        salir = QAction(QIcon(None), '&Salir', self)
        salir.setShortcut('Ctrl+Q') # permite usar combinación de teclas para ejecutar comandos
        salir.setStatusTip('Terminar la aplicación') # muestra en la barra de estados la descripción del comando
        salir.triggered.connect(self.botonsalir) # conecta la señal con el slot que manejará este evento

        agregar_a =QAction(QIcon(None), '&Agregar Archivo', self)
        agregar_a.setShortcut('Ctrl+N')
        agregar_a.setStatusTip('Agregar Archivo')
        agregar_a.triggered.connect(self.botonnuevo_archivo)

        agregar_c =QAction(QIcon(None), '&Agregar Carpeta', self)
        agregar_c.setStatusTip('Agregar Carpeta')
        agregar_c.triggered.connect(self.botonnueva_carpeta)
        # Creación de la barra de menús y de los menús
        menubar = self.menuBar()

        # primero menú
        archivo_menu = menubar.addMenu('&Menu')
        archivo_menu.addAction(ver_status)
        archivo_menu.addAction(salir)

        # segundo menú
        otro_menu = menubar.addMenu('&Agregar')
        otro_menu.addAction(agregar_a)
        otro_menu.addAction(agregar_c)

        # Incluye la barra de estado'''
        self.statusBar().showMessage('Listo')

    def botonsalir(self):
        ans = QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                         QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            self.cliente.enviar('quit')
            self.form.salir()
            QCoreApplication.instance().quit()

    def botonnuevo_archivo(self):
        fileName = QFileDialog.getOpenFileNames(self, 'Escoger Archivos',
                                                      QDir.rootPath())  # getExistingDirectory
        if fileName:
            for i in range(len(fileName)):
                nombre = fileName[i].split('\\')
                with open("{}".format(fileName[i]), 'rb') as file:
                    archivo = file.read()
                    nuevo_archivo = Archivo(archivo, nombre[-1])
                codigo = '009'
                msj_final = [self.cliente.usuario, codigo, nuevo_archivo]
                print(nuevo_archivo.archivo)
                pick = pickle.dumps(msj_final)
                print(len(pick),nuevo_archivo, nuevo_archivo.archivo)
                self.cliente.s_cliente.sendall('{}: 009:{}'.format(self.cliente.usuario, len(pick)).encode('utf-8'))
                self.cliente.s_cliente.sendall(pick)
            print(fileName)

    def botonnueva_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoger Carpeta',
                                                      QDir.rootPath())
        if fileName:
            nombre = fileName.split('\\')
            with open("{}".format(fileName), 'rb') as file:
                archivo = file.read()
                nuevo_archivo = Archivo(archivo, nombre[-1])
            codigo = '009'
            msj_final = [self.cliente.usuario, codigo, nuevo_archivo]
            print(nuevo_archivo.archivo)
            pick = pickle.dumps(msj_final)
            print(len(pick),nuevo_archivo, nuevo_archivo.archivo)
            self.cliente.s_cliente.sendall('{}: 009:{}'.format(self.cliente.usuario, len(pick)).encode('utf-8'))
            self.cliente.s_cliente.sendall(pick)
            print(fileName)

    def closeEvent(self, QCloseEvent):
        self.botonsalir()
        QCloseEvent.ignore()

    def cambiar_status_bar(self):
        self.statusBar().showMessage('Cambié el Status')


data = {'hola':{},"Alice": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
         "Bob": {"Wallet": {"Credit card": {}, "Money": {}}},'hola1':{},"Alice1": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}}
        ,'hol2a':{},"Alice3": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola2':{},"Alice2": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola3':{},"Alice4": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola4':{},"Alice5": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola5':{},"Alice6": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola6':{},"Alice7": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola7':{},"Alice8": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola8':{},"Alice9": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
        'hola9':{},"Alice0": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}}}


class Window(QWidget):
    def __init__(self,cliente):

        QWidget.__init__(self)

        self.cliente=cliente
        self.que=''
        # self.init_GUI()

    def init_GUI(self):
        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.model = QStandardItemModel()
        self.additems(self.model, self.cliente.hijos)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def additems(self, parent, elements):
        for text in elements.hijos.keys():
            nombre=elements.hijos[text].nombre
            item = QStandardItem(nombre)
            parent.appendRow(item)
            if elements.hijos[text]:
                self.additems(item, elements.hijos[text])

    # def actualizar_layaut(self):
    #     self.model = QStandardItemModel()
    #     self.additems(self.model, self.cliente.hijos)
    #     self.treeView.setModel(self.model)
    #     self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])
    #     layout = QVBoxLayout()
    #     layout.addWidget(self.treeView)
    #     try:
    #         self.setLayout(layout)
    #     except QWidget:
    #         pass

    def hola(self,que):
        print('hola')
        print(self.que)

    def openMenu(self, position):

        indexes = self.treeView.selectedIndexes()
        level = 0
        if len(indexes) > 0:
            index = indexes[0]
            while index.parent().isValid():
                # print(index.data(),index.parent().data())
                index = index.parent()
                level += 1
        ver_status = QAction(QIcon(None), '&Cambiar Status', self)
        ver_status.setStatusTip('Este es un item de prueba')
        ver_status.triggered.connect(self.hola)
        ver_status2 = QAction(QIcon(None), '&Cambiar Status2', self)
        ver_status2.setStatusTip('Este es un item de prueba2')
        ver_status2.triggered.connect(self.hola)
        menu = QMenu()
        if level == 0:
            self.que=indexes[0].data()
            menu.addAction(ver_status)

        elif level == 1:
            print(indexes[0].data())
            menu.addAction(self.tr("Edit object/container"))
            menu.addAction(ver_status2)
        elif level == 2:
            print(indexes[0].data())
            menu.addAction(self.tr("Edit object"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def botonsalir(self):
        ans = QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                         QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            # self.cliente.enviar('quit')
            QCoreApplication.instance().quit()

    def salir(self):
        QCoreApplication.instance().quit()

    # def keyPressEvent(self, QKeyEvent):
    #     if QKeyEvent.key() == Qt.Key_Return:
    #         self.botonaceptar()
    #     elif QKeyEvent.key() == Qt.Key_Escape:
    #         self.botonsalir()


