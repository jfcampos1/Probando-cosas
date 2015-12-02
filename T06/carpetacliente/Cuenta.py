__author__ = 'JuanFrancisco'
# coding=utf-8
import pickle
import os
import time
from serializar import get_persona,write_persona
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Chat import Onlines


class Archivo:
    def __init__(self, archivo, nombre):
        self.archivo = archivo
        self.nombre = nombre
        self.compartido = []


class MainForm(QMainWindow):
    def __init__(self, cliente):
        super().__init__()

        # Configura geometría de la ventana
        self.setWindowTitle('Drobpox')
        self.setGeometry(500, 200, 300, 400)
        self.cliente = cliente
        self.padre = 0
        self.form = Window(self.cliente, self)
        self.elchat=Onlines(self.cliente)
        self.setCentralWidget(self.form)
        # Definición de acciones
        ver_status = QAction(QIcon(None), '&Abrir Chat', self)
        ver_status.setStatusTip('Abrir Chat')
        ver_status.triggered.connect(self.cambiar_status_bar)

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
        archivo_menu.addAction(ver_status)
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
            self.cliente.enviar('quit')
            self.form.salir()
            QCoreApplication.instance().quit()

    def encontrar_padre_archivo(self):
        nodo = self.cliente.hijos
        self.padre = nodo.id_nodo
        self.botonnuevo_archivo()

    def encontrar_padre_carpeta(self):
        nodo = self.cliente.hijos
        self.padre = nodo.id_nodo
        self.botonnueva_carpeta()

    def encontrar_padre_crearcarpeta(self):
        nodo = self.cliente.hijos
        self.padre = nodo.id_nodo
        self.crear_carpeta()

    def botonnuevo_archivo(self):
        fileName = QFileDialog.getOpenFileNames(self, 'Escoger Archivos', QDir.rootPath())
        if fileName:
            for i in range(len(fileName)):
                time.sleep(3)
                self.enviar_archivo(fileName[i])
                print(self.padre)
            print(fileName)

    def botonnueva_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoger Carpeta', QDir.rootPath())
        if fileName:
            self.enviar_carpeta(fileName)
            persona=get_persona(self.cliente.usuario,'Cliente')
            print('Esta es la carpeta:',fileName)
            nombrecarpeta=fileName.split('\\')
            persona.archivos.agregar_nodo(fileName,fileName,valor='013',id_padre=None)
            self.mandar_todo_carpeta(fileName,persona.archivos,nombrecarpeta[-1])
            print(persona.archivos)
            lista=self.agregar_carpeta(fileName)
            for i in range(len(lista)):
                persona.archivos.agregar_nodo(lista[i][0],lista[i][0],lista[i][1],lista[i][2])
            print(lista)
            write_persona(persona,'Cliente')
            self.statusBar().showMessage('Listo')
            print(fileName)

    def enviar_archivo(self, path):
        nombre = path.split('\\')
        with open("{}".format(path), 'rb') as file:
            archivo = file.read()
            nuevo_archivo = Archivo(archivo, nombre[-1])
        codigo = '009'
        msj_final = [self.cliente.usuario, self.padre, codigo, nuevo_archivo]
        pick = pickle.dumps(msj_final)
        self.cliente.s_cliente.sendall('{}: 009:{}'.format(self.cliente.usuario, len(pick)).encode('utf-8'))
        self.cliente.s_cliente.sendall(pick)

    def enviar_carpeta(self, path):
        nombre = path.split('\\')
        nuevo_archivo = Archivo(None, nombre[-1])
        codigo = '011'
        msj_final = [self.cliente.usuario, self.padre, codigo, nuevo_archivo]
        pick = pickle.dumps(msj_final)
        print(len(pick), nuevo_archivo, nuevo_archivo.archivo)
        self.cliente.s_cliente.sendall('{}: 011:{}'.format(self.cliente.usuario, len(pick)).encode('utf-8'))
        self.cliente.s_cliente.sendall(pick)

    def crear_carpeta(self):
        texto, ok = QInputDialog.getText(self, "Titulo", "Ingresa tu texto:")
        if ok:
            if texto == '':
                pass
            else:
                nombre = 'agregar\\' + texto
                self.enviar_carpeta(nombre)

    def juntar_string(self,string):
        nuevo=''
        for i in range(len(string)):
            if i==0:
                nuevo=string[i]
            if i<len(string)-1:
                nuevo+='\\'+string[i]
        return nuevo

    def mandar_todo_carpeta(self, path,persona,carpeta):
        # lista2=[]
        lista = os.listdir(str(path))
        for i in range(len(lista)):
            time.sleep(2)
            completo = path + '\\' + lista[i]
            archivo = self.es_carpeta_o_archivo(path + '\\' + lista[i])
            nombre = path.split('\\')
            self.padre = str(nombre[-1])
            self.statusBar().showMessage('Subiendo carpeta: {}..elemento: {}'.format(carpeta,nombre[-1]))
            if archivo == '012':
                self.enviar_archivo(completo)
            else:
                self.enviar_carpeta(completo)
                self.mandar_todo_carpeta(completo,persona,carpeta)

    def agregar_carpeta(self,path):
        lista2=[]
        lista=os.listdir(path)
        for i in range(len(lista)):
            completo = path + '\\' + lista[i]
            archivo = self.es_carpeta_o_archivo(path + '\\' + lista[i])
            if archivo == '012':
                lista2.append([completo,'012',path])
            else:
                lista3=self.agregar_carpeta(completo)
                lista2.append([completo,'013',path])
                lista2+=lista3
        return lista2

    def es_carpeta_o_archivo(self, path):
        if os.path.isfile(path):
            return '012'
        else:
            return '013'

    def closeEvent(self, QCloseEvent):
        self.botonsalir()
        QCloseEvent.ignore()

    def cambiar_status_bar(self):
        self.statusBar().showMessage('Abrir Chat')
        self.elchat.show()


class Window(QWidget):
    def __init__(self, cliente, mainwindow):

        QWidget.__init__(self)
        self.mainwindow = mainwindow
        self.cliente = cliente
        self.que = ''
        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.model = QStandardItemModel()
        self.additems(self.model, self.cliente)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def init_GUI(self):
        self.model = QStandardItemModel()
        self.additems(self.model, self.cliente.hijos)
        self.treeView.setModel(self.model)
        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

    def additems(self, parent, elements):
        for text in elements.hijos.keys():
            nombre = elements.hijos[text].nombre
            item = QStandardItem(nombre)
            parent.appendRow(item)
            if elements.hijos[text]:
                self.additems(item, elements.hijos[text])

    def agregar_archivo(self):
        nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
        if nodo.valor == '013':
            self.mainwindow.padre = nodo.id_nodo
            self.mainwindow.botonnuevo_archivo()
        else:
            self.mainwindow.padre = nodo.id_padre
            self.mainwindow.botonnuevo_archivo()

    def agregar_carpeta(self):
        nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
        if nodo.valor == '013':
            self.mainwindow.padre = nodo.id_nodo
            self.mainwindow.botonnueva_carpeta()
        else:
            self.mainwindow.padre = nodo.id_padre
            self.mainwindow.botonnueva_carpeta()

    def descargar_archivo(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
            no_file = str(nodo.id_nodo) + ',' + fileName
            self.cliente.s_cliente.sendall('{}: 015:{}'.format(self.cliente.usuario, len(no_file)).encode('utf-8'))
            self.cliente.s_cliente.sendall('{}'.format(no_file).encode('utf-8'))

    def descargar_carpeta(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Escoge Carpeta de descarga', QDir.rootPath())
        if fileName:
            os.makedirs("{}".format(str(fileName + '\\' + self.que)))
            nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
            self.mandar_descarga_carpeta(fileName + '\\' + self.que, nodo)
            no_file = str(nodo.id_nodo) + ',' + fileName
            self.cliente.s_cliente.sendall('{}: 015:{}'.format(self.cliente.usuario, len(no_file)).encode('utf-8'))
            self.cliente.s_cliente.sendall('{}'.format(no_file).encode('utf-8'))

    def borrar(self):
        nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
        self.cliente.s_cliente.sendall('{}: 016:{}'.format(self.cliente.usuario,nodo.id_nodo).encode('utf-8'))

    def mandar_descarga_carpeta(self, path, nodo):
        for i in nodo.hijos.keys():
            time.sleep(3)
            archivo = nodo.hijos[i].valor
            print('Tipo de archivo')
            if archivo == '012':
                no_file = str(nodo.hijos[i].id_nodo) + ',' + path
                self.cliente.s_cliente.sendall('{}: 015:{}'.format(self.cliente.usuario, len(no_file)).encode('utf-8'))
                self.cliente.s_cliente.sendall('{}'.format(no_file).encode('utf-8'))
            else:
                os.makedirs("{}".format(str(path + '\\' + nodo.hijos[i].nombre)))
                self.mandar_descarga_carpeta(str(path + '\\' + nodo.hijos[i].nombre), nodo.hijos[i])

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
        menu = QMenu()
        if len(indexes) > 0:
            self.que = indexes[0].data()
            menu.addAction(ver_status)
            menu.addAction(ver_status2)
            nodo = self.cliente.hijos.obtener_nodo_nombre(self.que)
            if nodo.valor == '013':
                menu.addAction(ver_status4)
                menu.addAction(ver_status6)
            else:
                menu.addAction(ver_status3)
                menu.addAction(ver_status5)

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def salir(self):
        QCoreApplication.instance().quit()

