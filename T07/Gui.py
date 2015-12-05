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
        self.setAttribute(Qt.WA_DeleteOnClose)
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
            # self.close()
            QCoreApplication.instance().quit()

    def encontrar_padre_archivo(self):
        self.padre = ''
        self.botonnuevo_archivo()

    def encontrar_padre_carpeta(self):
        self.padre = ''
        self.botonnueva_carpeta()

    def encontrar_padre_crearcarpeta(self):
        self.padre = '/'
        self.crear_carpeta()

    def botonnuevo_archivo(self):
        fileName = QFileDialog.getOpenFileNames(self, 'Escoger Archivos', QDir.rootPath())
        if fileName:
            for i in range(len(fileName)):
                time.sleep(3)
                nombre = fileName[i].split('\\')
                self.statusBar().showMessage('Cargando archivo: {}'.format(nombre[-1]))
                self.enviar_archivo(fileName[i], self.padre)

    def botonnueva_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoger Carpeta', QDir.rootPath())
        if fileName:
            self.enviar_carpeta(fileName, self.padre)
            nombrecarpeta = fileName.split('\\')
            if self.padre == '/' or self.padre is None:
                padre = self.padre + nombrecarpeta[-1]
                padre2 = ''
            else:
                padre = self.padre + '/' + nombrecarpeta[-1]
                padre2 = self.padre
            self.form.arbol.agregar_nodo(padre, nombre=nombrecarpeta[-1], valor='013', id_padre=padre2)
            self.mandar_todo_carpeta(fileName, nombrecarpeta[-1], padre)
            self.form.init_GUI()
            self.statusBar().showMessage('Listo')

    def enviar_archivo(self, path, padre):
        nombre = path.split('\\')
        with open("{}".format(path), 'rb') as file:
            archivo = file.read()
        dest_path = padre + '/' + nombre[-1]
        self.statusBar().showMessage('Subiendo archivo: {}'.format(nombre[-1]))
        try:
            self.client.files_upload(archivo, dest_path, mute=True)
            self.form.arbol.agregar_nodo(id_nodo=dest_path, nombre=nombre[-1], valor='012', id_padre=padre)
            self.form.init_GUI()
            self.statusBar().showMessage('Listo')
        except dropbox.exceptions.InternalServerError:
            self.statusBar().showMessage('Problema en el servidor')
            # client_modified=datetime.datetime(*time.gmtime(mtime)[:6]) mtime = os.path.getmtime(path)

    def enviar_carpeta(self, path, padre):
        archivo = path.split('\\')
        nombre = padre + '/' + archivo[-1]
        try:
            self.client.files_create_folder(nombre)
            self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=archivo[-1], valor='013', id_padre=padre)
            self.form.init_GUI()
        except dropbox.exceptions.ApiError:
            self.statusBar().showMessage('Carpeta ya existe')

    def crear_carpeta(self):
        texto, ok = QInputDialog.getText(self, "Titulo", "Nombre de la nueva carpeta:")
        if ok:
            if texto == '':
                pass
            else:
                nombre = os.path.join('/', texto)
                self.client.files_create_folder(nombre)
                self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=texto, valor='013', id_padre='')
                self.statusBar().showMessage('Carpeta agregada: {}'.format(nombre))
                self.form.init_GUI()

    def mandar_todo_carpeta(self, path, carpeta, path2):
        lista = os.listdir(str(path))
        for i in range(len(lista)):
            completo = path + '\\' + lista[i]
            archivo = self.es_carpeta_o_archivo(completo)
            nombre = path.split('\\')
            self.statusBar().showMessage('Subiendo carpeta: {}..elemento: {}'.format(carpeta, nombre[-1]))
            if archivo == '012':
                self.enviar_archivo(completo, path2)
            else:
                self.enviar_carpeta(completo, path2)
                path3 = path2 + '/' + lista[i]
                self.mandar_todo_carpeta(completo, carpeta, path3)

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
        self.treeView.customContextMenuRequested.connect(self.openmenu)
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
        lista = self.client.files_list_folder('').entries
        lista2 = self.client.files_list_folder('', recursive=True).entries
        for text in lista:
            nombre = text.name
            path_nuevo = text.path_lower
            if type(text) == FolderMetadata:
                self.arbol.agregar_nodo(path_nuevo, nombre, '013', '')
            else:
                self.arbol.agregar_nodo(path_nuevo, nombre, '012', '')
        for text in lista2:
            nombre = text.name
            path_nuevo = text.path_lower
            nombre2 = path_nuevo.split('/')
            padre = path_nuevo.replace('/{}'.format(nombre2[-1]), '')
            if type(text) == FolderMetadata:
                self.arbol.agregar_nodo(path_nuevo, nombre, '013', padre)
            else:
                self.arbol.agregar_nodo(path_nuevo, nombre, '012', padre)

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

    def crear_carpeta(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        texto, ok = QInputDialog.getText(self, "Titulo", "Nombre de la nueva carpeta:")
        if ok:
            if texto == '':
                pass
            else:
                if nodo.valor == '012':
                    nombre = nodo.id_padre + '/' + texto
                    try:
                        self.client.files_create_folder(nombre)
                        self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=texto, valor='013', id_padre=nodo.id_padre)
                        self.statusBar().showMessage('Carpeta agregada: {}'.format(nombre))
                        self.form.init_GUI()
                    except dropbox.exceptions.ApiError:
                        self.statusBar().showMessage('Nombre de carpeta ya existe: {}'.format(nombre))
                elif nodo.valor == '013':
                    nombre = nodo.id_nodo + '/' + texto
                    try:
                        self.client.files_create_folder(nombre)
                        self.form.arbol.agregar_nodo(id_nodo=nombre, nombre=texto, valor='013', id_padre=nodo.id_nodo)
                        self.statusBar().showMessage('Carpeta agregada: {}'.format(nombre))
                        self.form.init_GUI()
                    except dropbox.exceptions.ApiError:
                        self.statusBar().showMessage('Nombre de carpeta ya existe: {}'.format(nombre))

    def descargar_archivo(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            nodo = self.arbol.obtener_nodo_nombre(self.que)
            nombre = nodo.id_nodo.split('/')
            self.client.files_download_to_file(fileName + '\\' + nombre[-1], nodo.id_nodo)
            self.mainwindow.statusBar().showMessage('Descargado: {}'.format(nombre[-1]))

    def descargar_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            os.makedirs("{}".format(str(fileName + '\\' + self.que)))
            nodo = self.arbol.obtener_nodo_nombre(self.que)
            self.mainwindow.statusBar().showMessage('Descargando: {}'.format(self.que))
            self.mandar_descarga_carpeta(fileName + '\\' + self.que, nodo)
            self.mainwindow.statusBar().showMessage('Listo la descarga: {}'.format(self.que))

    def borrar(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        self.client.files_delete(nodo.id_nodo)
        self.mainwindow.statusBar().showMessage('Borrando: {}'.format(self.que))
        self.arbol.borrar_nodo(id_padre=nodo.id_padre, id_nodo=nodo.id_nodo)
        self.mainwindow.statusBar().showMessage('Listo: {}'.format(self.que))
        self.init_GUI()

    def mandar_descarga_carpeta(self, path, nodo):
        for i in nodo.hijos.keys():
            archivo = nodo.hijos[i].valor
            if archivo == '012':
                self.client.files_download_to_file(path + '\\' + nodo.hijos[i].nombre, nodo.hijos[i].id_nodo)
            else:
                os.makedirs("{}".format(str(path + '\\' + nodo.hijos[i].nombre)))
                self.mandar_descarga_carpeta(str(path + '\\' + nodo.hijos[i].nombre), nodo.hijos[i])

    def historial(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        if nodo.valor == '012':
            data = self.client.files_list_revisions(nodo.id_nodo, limit=10).entries
            self.historia = Historial(data)
            self.historia.table.show()
        elif nodo.valor == '013':
            data = []
            for i in nodo.hijos.values():
                if i.valor == '012':
                    data2 = self.client.files_list_revisions(i.id_nodo, limit=10).entries
                    data += data2
            self.historia2 = Historial(data)
            self.historia2.table.show()

    def mover(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        texto, ok = QInputDialog.getText(self, "Mover",
                                         "Ingresa nombre de la carpeta contenedora(dropbox para carpeta principal):")
        if ok:
            if texto == '':
                pass
            else:
                if texto == 'dropbox':
                    try:
                        self.client.files_move(nodo.id_nodo, '/' + nodo.nombre)
                        aux = self.arbol.sacar_nodo(nodo)
                        aux.agregando_a_arbol(self.arbol, '')
                    except dropbox.exceptions.ApiError:
                        self.mainwindow.statusBar().showMessage('Carpeta ya existe con el mismo nombre en el destino')
                else:
                    nodo_llegada = self.arbol.obtener_nodo_nombre(texto)
                    if nodo_llegada is not None and nodo_llegada.valor == '013':
                        try:
                            self.client.files_move(nodo.id_nodo, nodo_llegada.id_nodo + '/' + nodo.nombre)
                            aux = self.arbol.sacar_nodo(nodo)
                            aux.agregando_a_arbol(self.arbol, nodo_llegada.id_nodo)
                        except dropbox.exceptions.ApiError:
                            otra = self.mainwindow.statusBar()
                            otra.showMessage('Carpeta ya existe con el mismo nombre en el destino')
                    elif nodo_llegada is not None and nodo_llegada.valor == '012':
                        otra = self.mainwindow.statusBar()
                        otra.showMessage('Tienes que moverlo a una carpeta')
                    else:
                        otra = self.mainwindow.statusBar()
                        otra.showMessage('Tienes que moverlo a una carpeta')
                self.init_GUI()

    def renombrar(self):
        nodo = self.arbol.obtener_nodo_nombre(self.que)
        texto, ok = QInputDialog.getText(self, "Renombrar",
                                         "Nuevo nombre con la extencion si es archivo:")
        if ok:
            if texto == '':
                pass
            else:
                if self.arbol.obtener_nodo_nombre(texto) is None:
                    if nodo.valor == '012':
                        numero = texto.find('.')
                        if numero != -1:
                            if texto.split('.')[1] == nodo.nombre.split('.')[1]:
                                id_padre = nodo.id_padre
                                nuevo_id = id_padre + '/' + texto
                                self.client.files_move(nodo.id_nodo, nuevo_id)
                                aux = self.arbol.sacar_nodo(nodo)
                                self.arbol.agregar_nodo(id_nodo=nuevo_id, valor=nodo.valor, id_padre=id_padre,
                                                        nombre=texto)
                                for i in aux.hijos.values():
                                    i.agregando_a_arbol(self.arbol, nuevo_id)
                                self.init_GUI()
                            else:
                                self.mainwindow.statusBar().showMessage('Falta la extencion')
                        else:
                            self.mainwindow.statusBar().showMessage('Falta la extencion')
                    elif nodo.valor == '013':
                        id_padre = nodo.id_padre
                        nuevo_id = id_padre + '/' + texto
                        try:
                            self.client.files_move(nodo.id_nodo, nuevo_id)
                            aux = self.arbol.sacar_nodo(nodo)
                            self.arbol.agregar_nodo(id_nodo=nuevo_id, valor=nodo.valor, id_padre=id_padre, nombre=texto)
                            for i in aux.hijos.values():
                                i.agregando_a_arbol(self.arbol, nuevo_id)
                            self.init_GUI()
                        except dropbox.exceptions.ApiError:
                            self.mainwindow.statusBar().showMessage('Nombre ya existe, escoja uno diferente')
                else:
                    self.mainwindow.statusBar().showMessage('Nombre ya existe, escoja uno diferente')

    def openmenu(self, position):

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
        ver_status10 = QAction(QIcon(None), '&Crear Carpeta', self)
        ver_status10.setStatusTip('Crear Carpeta')
        ver_status10.triggered.connect(self.crear_carpeta)
        ver_status7 = QAction(QIcon(None), '&Ver Historial', self)
        ver_status7.setStatusTip('Ver Historial')
        ver_status7.triggered.connect(self.historial)
        ver_status8 = QAction(QIcon(None), '&Mover', self)
        ver_status8.setStatusTip('Mover')
        ver_status8.triggered.connect(self.mover)
        ver_status9 = QAction(QIcon(None), '&Renombrar', self)
        ver_status9.setStatusTip('Renombrar')
        ver_status9.triggered.connect(self.renombrar)
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
            menu.addAction(ver_status10)
            menu.addAction(ver_status7)
            menu.addAction(ver_status8)
            menu.addAction(ver_status9)

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def salir(self):
        QCoreApplication.instance().quit()


class Historial(QWidget):
    def __init__(self, history):
        super().__init__()
        lista = ['Name', 'Path', 'Client_modified', 'Server_modified', 'Size']
        self.history = history
        self.table = QTableWidget(len(lista), 5)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tableItem = QLabel()
        self.tableItem.setText("Testing")
        self.table.setCellWidget(0, 0, self.tableItem)
        for i in range(len(lista)):
            tableItem = QLabel()
            tableItem.setText(str(lista[i]))
            tableItem.setAlignment(Qt.AlignCenter)
            self.table.setCellWidget(0, i, tableItem)
        for i in range(len(self.history)):
            for n in range(len(lista)):
                tableItem = QLabel()
                if n == 0:
                    tableItem.setText(str(self.history[i].name))
                elif n == 1:
                    tableItem.setText(str(self.history[i].path_lower))
                elif n == 2:
                    tableItem.setText(str(self.history[i].client_modified))
                elif n == 3:
                    tableItem.setText(str(self.history[i].server_modified))
                elif n == 4:
                    tableItem.setText(str(self.history[i].size))
                tableItem.sizeHint()
                tableItem.setAlignment(Qt.AlignCenter)
                self.table.setCellWidget(i + 1, n, tableItem)
        self.table.setGeometry(500, 200, 600, 400)
