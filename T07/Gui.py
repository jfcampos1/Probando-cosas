__author__ = 'JuanFrancisco'
# coding=utf-8
import os
import time

import dropbox
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dropbox.files import FolderMetadata

from Arbol import Arbol


class MainForm(QMainWindow):
    def __init__(self, client):
        super().__init__()

        # Configura geometría de la ventana
        self.setWindowTitle('Drobpox')
        self.setGeometry(500, 200, 400, 500)
        self.client = client
        self.padre = ''
        self.form = Window(self.client, self)
        self.setCentralWidget(self.form)
        # Definición de acciones

        salir = QAction(QIcon(None), '&Salir', self)
        salir.setShortcut('Ctrl+Q')
        salir.setStatusTip('Terminar la aplicación')
        salir.triggered.connect(self.botonsalir)

        agregar_a = QAction(QIcon(None), '&Agregar Archivo', self)
        agregar_a.setShortcut('Ctrl+N')
        agregar_a.setStatusTip('Agregar Archivo')
        agregar_a.triggered.connect(self.encontrar_padre_archivo)

        agregar_c = QAction(QIcon(None), '&Agregar Carpeta', self)
        agregar_c.setShortcut('Ctrl+O')
        agregar_c.setStatusTip('Agregar Carpeta')
        agregar_c.triggered.connect(self.encontrar_padre_carpeta)
        agregar_d = QAction(QIcon(None), '&Crear Carpeta', self)
        agregar_d.setStatusTip('Crear Carpeta')
        agregar_d.triggered.connect(self.encontrar_padre_crearcarpeta)
        # Creación de la barra de menús y de los menús
        menubar = self.menuBar()

        # primero menú
        archivo_menu = menubar.addMenu('&Menu')
        archivo_menu.addAction(salir)

        # segundo menú
        otro_menu = menubar.addMenu('&Agregar')
        otro_menu.addAction(agregar_a)
        otro_menu.addAction(agregar_c)
        otro_menu.addAction(agregar_d)

        # Incluye la barra de estado'''
        self.statusBar().showMessage('Listo')

    def botonsalir(self):
        ans = QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            self.form.salir()
            QCoreApplication.instance().quit()

    def encontrar_padre_archivo(self):
        self.padre = '/'
        self.botonnuevo_archivo()

    def encontrar_padre_carpeta(self):
        self.padre = '/'
        self.botonnueva_carpeta()

    def encontrar_padre_crearcarpeta(self):
        self.padre = '/'
        self.crear_carpeta()

    def botonnuevo_archivo(self):
        fileName = QFileDialog.getOpenFileNames(self, 'Escoger Archivos', QDir.rootPath())
        if fileName:
            for i in range(len(fileName)):
                time.sleep(3)
                self.enviar_archivo(fileName[i], self.padre)
                print(self.padre)
            print(fileName)

    def botonnueva_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoger Carpeta', QDir.rootPath())
        if fileName:
            self.enviar_carpeta(fileName, self.padre)
            print('Esta es la carpeta:', fileName)
            nombrecarpeta = fileName.split('\\')
            if self.padre == '/' or self.padre is None:
                padre = self.padre + nombrecarpeta[-1]
                padre2 = ''
                print('acaa')
            else:
                padre = self.padre + '/' + nombrecarpeta[-1]
                padre2 = self.padre
            self.form.arbol.agregar_nodo(padre, nombre=nombrecarpeta[-1], valor='013', id_padre=padre2)
            self.mandar_todo_carpeta(fileName, nombrecarpeta[-1], padre)
            self.form.init_GUI()
            self.statusBar().showMessage('Listo')
            print(fileName)

    def enviar_archivo(self, path, padre):
        nombre = path.split('\\')
        with open("{}".format(path), 'rb') as file:
            archivo = file.read()
        print(padre, nombre[-1])
        dest_path = padre + '/' + nombre[-1]
        print(dest_path)
        try:
            self.client.files_upload(archivo, dest_path, mute=True)
            self.form.arbol.agregar_nodo(id_nodo=dest_path, nombre=nombre[-1], valor='012', id_padre=padre)
            self.form.init_GUI()
        except dropbox.exceptions.InternalServerError:
            print('Problema en el servidor')
            # client_modified=datetime.datetime(*time.gmtime(mtime)[:6]) mtime = os.path.getmtime(path)

    def enviar_carpeta(self, path, padre):
        archivo = path.split('\\')
        nombre = padre + '/' + archivo[-1]
        print(nombre)
        try:
            self.client.files_create_folder(nombre)
            self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=archivo[-1], valor='013', id_padre=padre)
            self.form.init_GUI()
        except dropbox.exceptions.ApiError:
            print('Carpeta ya existente')

    def crear_carpeta(self):
        texto, ok = QInputDialog.getText(self, "Titulo", "Ingresa tu texto:")
        if ok:
            if texto == '':
                pass
            else:
                nombre = os.path.join('/', texto)
                self.client.files_create_folder(nombre)
                self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=texto, valor='013', id_padre='')
                self.form.init_GUI()

    def juntar_string(self, string):
        nuevo = ''
        for i in range(len(string)):
            if i == 0:
                nuevo = string[i]
            if i < len(string) - 1:
                nuevo += '\\' + string[i]
        return nuevo

    def mandar_todo_carpeta(self, path, carpeta, path2):
        lista = os.listdir(str(path))
        for i in range(len(lista)):
            completo = path + '\\' + lista[i]
            archivo = self.es_carpeta_o_archivo(completo)
            nombre = path.split('\\')
            self.statusBar().showMessage('Subiendo carpeta: {}..elemento: {}'.format(carpeta, nombre[-1]))
            print(nombre)
            if archivo == '012':
                self.enviar_archivo(completo, path2)
            else:
                self.enviar_carpeta(completo, path2)
                path3 = path2 + '/' + lista[i]
                print(completo, path3)
                self.mandar_todo_carpeta(completo, carpeta, path3)

    def agregar_carpeta(self, path):
        lista2 = []
        lista = os.listdir(path)
        for i in range(len(lista)):
            completo = path + '\\' + lista[i]
            archivo = self.es_carpeta_o_archivo(path + '\\' + lista[i])
            if archivo == '012':
                lista2.append([completo, '012', path])
            else:
                lista3 = self.agregar_carpeta(completo)
                lista2.append([completo, '013', path])
                lista2 += lista3
        return lista2

    def es_carpeta_o_archivo(self, path):
        if os.path.isfile(path):
            return '012'
        else:
            return '013'

    def closeEvent(self, QCloseEvent):
        self.botonsalir()
        QCloseEvent.ignore()


class Window(QWidget):
    def __init__(self, client, mainwindow):

        QWidget.__init__(self)
        self.mainwindow = mainwindow
        self.que = ''
        self.client = client
        self.arbol = Arbol('')
        self.crear_arbol('')
        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.model = QStandardItemModel()
        self.additems(self.model, self.arbol)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def init_GUI(self):
        self.model = QStandardItemModel()
        self.additems(self.model, self.arbol)
        self.treeView.setModel(self.model)
        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

    def additems(self, parent, elements):
        for text in elements.hijos.keys():
            nombre = elements.hijos[text].nombre
            item = QStandardItem(nombre)
            parent.appendRow(item)
            if elements.hijos[text]:
                self.additems(item, elements.hijos[text])

    def crear_arbol(self, path):
        for text in self.client.files_list_folder(path).entries:
            nombre = text.name
            path_nuevo = text.path_lower
            if type(text) == FolderMetadata:
                self.arbol.agregar_nodo(path_nuevo, nombre, '013', path)
                self.crear_arbol(text.path_lower)
            else:
                self.arbol.agregar_nodo(path_nuevo, nombre, '012', path)

    def agregar_archivo(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        if nodo.valor == '013':
            self.mainwindow.padre = nodo.id_nodo
            self.mainwindow.botonnuevo_archivo()
        else:
            self.mainwindow.padre = nodo.id_padre
            self.mainwindow.botonnuevo_archivo()

    def agregar_carpeta(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        if nodo.valor == '013':
            self.mainwindow.padre = nodo.id_nodo
            self.mainwindow.botonnueva_carpeta()
        else:
            self.mainwindow.padre = nodo.id_padre
            self.mainwindow.botonnueva_carpeta()

    def descargar_archivo(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            nodo = self.arbol.obtener_nodo_nombre(self.que)
            nombre = nodo.id_nodo.split('/')
            self.client.files_download_to_file(fileName + '\\' + nombre[-1], nodo.id_nodo)

    def descargar_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            os.makedirs("{}".format(str(fileName + '\\' + self.que)))
            nodo = self.arbol.obtener_nodo_nombre(self.que)
            self.mandar_descarga_carpeta(fileName + '\\' + self.que, nodo)

    def borrar(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        self.client.files_delete(nodo.id_nodo)
        self.arbol.borrar_nodo(id_padre=nodo.id_padre, id_nodo=nodo.id_nodo)
        self.init_GUI()

    def mandar_descarga_carpeta(self, path, nodo):
        for i in nodo.hijos.keys():
            archivo = nodo.hijos[i].valor
            print('Tipo de archivo')
            if archivo == '012':
                self.client.files_download_to_file(path + '\\' + nodo.hijos[i].nombre, nodo.hijos[i].id_nodo)
            else:
                os.makedirs("{}".format(str(path + '\\' + nodo.hijos[i].nombre)))
                self.mandar_descarga_carpeta(str(path + '\\' + nodo.hijos[i].nombre), nodo.hijos[i])

    def historial(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        data = self.client.files_get_metadata(nodo.id_nodo)
        print(data)

    def openMenu(self, position):

        indexes = self.treeView.selectedIndexes()
        ver_status = QAction(QIcon(None), '&Agregar Archivo', self)
        ver_status.setStatusTip('Agregar Archivo')
        ver_status.triggered.connect(self.agregar_archivo)
        ver_status2 = QAction(QIcon(None), '&Agregar Carpeta', self)
        ver_status2.setStatusTip('Agregar Carpeta')
        ver_status2.triggered.connect(self.agregar_carpeta)
        ver_status3 = QAction(QIcon(None), '&Descargar Archivo', self)
        ver_status3.setStatusTip('Descargando Archivo')
        ver_status3.triggered.connect(self.descargar_archivo)
        ver_status4 = QAction(QIcon(None), '&Descargar Carpeta', self)
        ver_status4.setStatusTip('Descargando Carpeta')
        ver_status4.triggered.connect(self.descargar_carpeta)
        ver_status5 = QAction(QIcon(None), '&Borrar Archivo', self)
        ver_status5.setStatusTip('Borrando Archivo')
        ver_status5.triggered.connect(self.borrar)
        ver_status6 = QAction(QIcon(None), '&Borrar Carpeta', self)
        ver_status6.setStatusTip('Borrando Carpeta')
        ver_status6.triggered.connect(self.borrar)
        ver_status7 = QAction(QIcon(None), '&Ver Historial', self)
        ver_status7.setStatusTip('Ver Historial')
        ver_status7.triggered.connect(self.historial)
        menu = QMenu()
        if len(indexes) > 0:
            self.que = indexes[0].data()
            menu.addAction(ver_status)
            menu.addAction(ver_status2)
            nodo = self.arbol.obtener_nodo_nombre(self.que)
            if nodo.valor == '013':
                menu.addAction(ver_status4)
                menu.addAction(ver_status6)
            else:
                menu.addAction(ver_status3)
                menu.addAction(ver_status5)
            menu.addAction(ver_status7)

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def salir(self):
        QCoreApplication.instance().quit()


class Historial(QWidget):
    def __init__(self, data):

        QWidget.__init__(self)
        # self.cliente = cliente
        self.setWindowTitle('Historial Modificaciones')
        self.que = ''
        self.data = data
        self.arbol = Arbol('')
        self.crear_arbol('')
        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.additems(self.model, self.arbol)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def additems(self, parent, elements):
        for text in elements.hijos.keys():
            nombre = elements.hijos[text].nombre
            item = QStandardItem(nombre)
            parent.appendRow(item)
            if elements.hijos[text]:
                self.additems(item, elements.hijos[text])
