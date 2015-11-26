__author__ = 'JuanFrancisco'
# import sys
# from PyQt4 import QtCore, QtGui
#
#
# class Window(QtGui.QWidget):
#
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#         self.treeWidget = QtGui.QTreeWidget()
#         self.treeWidget.setHeaderHidden(True)
#         self.addItems(self.treeWidget.invisibleRootItem())
#         self.treeWidget.itemChanged.connect(self.handleChanged)
#         layout = QtGui.QVBoxLayout()
#         layout.addWidget(self.treeWidget)
#         self.setLayout(layout)
#
#     def addItems(self, parent):
#         column = 0
#         clients_item = self.addParent(parent, column, 'Clients', 'data Clients')
#         vendors_item = self.addParent(parent, column, 'Vendors', 'data Vendors')
#         time_period_item = self.addParent(parent, column, 'Time Period', 'data Time Period')
#
#         self.addChild(clients_item, column, 'Type A', 'data Type A')
#         self.addChild(clients_item, column, 'Type B', 'data Type B')
#
#         self.addChild(vendors_item, column, 'Mary', 'data Mary')
#         self.addChild(vendors_item, column, 'Arnold', 'data Arnold')
#
#         self.addChild(time_period_item, column, 'Init', 'data Init')
#         self.addChild(time_period_item, column, 'End', 'data End')
#
#     def addParent(self, parent, column, title, data):
#         item = QtGui.QTreeWidgetItem(parent, [title])
#         item.setData(column, QtCore.Qt.UserRole, data)
#         item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
#         item.setExpanded (True)
#         return item
#
#     def addChild(self, parent, column, title, data):
#         item = QtGui.QTreeWidgetItem(parent, [title])
#         item.setData(column, QtCore.Qt.UserRole, data)
#         item.setCheckState (column, QtCore.Qt.Unchecked)
#         return item
#
#     def handleChanged(self, item, column):
#         if item.checkState(column) == QtCore.Qt.Checked:
#             print ("checked", item, item.text(column))
#         if item.checkState(column) == QtCore.Qt.Unchecked:
#             print ("unchecked", item, item.text(column))
#
# if __name__ == "__main__":
#
#     app = QtGui.QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


# data = [
#     ("Alice", [
#         ("Keys", [("Cellphone", [])]),
#         ("Purse", [
#             ("Cellphone", [])
#             ])
#         ]),
#     ("Bob", [
#         ("Wallet", [
#             ("Credit card", []),
#             ("Money", [])
#             ])
#         ])
#     ]
data = {'hola':{},"Alice": {"Keys": {"Cellphone": {}}, "Purse": {"Credit card": {"Cellphone": {}}, "Money": {}}},
         "Bob": {"Wallet": {"Credit card": {}, "Money": {}}}}


class Window(QWidget):
    def __init__(self):

        QWidget.__init__(self)

        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)
        self.model = QStandardItemModel()
        self.addItems(self.model, data)
        self.treeView.setModel(self.model)

        self.model.setHorizontalHeaderLabels([self.tr("Dropbox")])

        layout = QVBoxLayout()
        layout.addWidget(self.treeView)
        self.setLayout(layout)

    def addItems(self, parent, elements):
        for text in elements.keys():
            item = QStandardItem(text)
            parent.appendRow(item)
            if elements[text]:
                self.addItems(item, elements[text])
    def hola(self):
        print('hola')

    def openMenu(self, position):

        indexes = self.treeView.selectedIndexes()
        level = 0
        if len(indexes) > 0:
            index = indexes[0]
            while index.parent().isValid():
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
            menu.addAction(ver_status)
            menu.addAction(ver_status2)
        elif level == 1:
            menu.addAction(self.tr("Edit object/container"))
        elif level == 2:
            menu.addAction(self.tr("Edit object"))

        menu.exec_(self.treeView.viewport().mapToGlobal(position))

    def botonsalir(self):
        ans = QMessageBox.question(self, "Salir", "Salir de dropbox?",
                                         QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            # self.cliente.enviar('quit')
            QCoreApplication.instance().quit()

    # def keyPressEvent(self, QKeyEvent):
    #     if QKeyEvent.key() == Qt.Key_Return:
    #         self.botonaceptar()
    #     elif QKeyEvent.key() == Qt.Key_Escape:
    #         self.botonsalir()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
