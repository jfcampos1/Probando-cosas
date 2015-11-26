__author__ = 'JuanFrancisco'
import Cuenta
lista = [1,2,3,5]
print(lista[int('-1')])
print(lista.index(5))
strin = 'hola'
print(strin.find('u'))
print(type(strin.find('u')))
print(type(Cuenta.Archivo(lista,strin)))
# app = QtGui.QApplication([])
# client = Cuenta('hola')
# client.show()
# app.exec_()
# import sys
#
# from PyQt4.QtGui import (QApplication, QColumnView, QFileSystemModel,
#                          QSplitter, QTreeView)
# from PyQt4.QtCore import QDir, Qt
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # Splitter to show 2 views in same widget easily.
#     splitter = QSplitter()
#     # The model.
#     model = QFileSystemModel()
#     # You can setRootPath to any path.
#     model.setRootPath(QDir.rootPath())
#     # List of views.
#     views = []
#     for ViewType in (QColumnView, QTreeView):
#         # Create the view in the splitter.
#         view = ViewType(splitter)
#         # Set the model of the view.
#         view.setModel(model)
#         # Set the root index of the view as the user's home directory.
#         view.setRootIndex(model.index('./'))
#     # Show the splitter.
#     splitter.show()
#     # Maximize the splitter.
#     splitter.setWindowState(Qt.WindowMaximized)
#     # Start the main loop.
#     sys.exit(app.exec_())
#
# class Main(QtGui.QTreeView):
#
#   def __init__(self):
#
#     QtGui.QTreeView.__init__(self)
#     model = QtGui.QFileSystemModel()
#     model.setRootPath( QtCore.QDir.currentPath() )
#     self.setModel(model)
#     QtCore.QObject.connect(self.selectionModel(), QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'), self.test)
#
#   @QtCore.pyqtSlot("QItemSelection, QItemSelection")
#   def test(self, selected, deselected):
#       print("hello!")
#       print(selected)
#       print(deselected)
#
# if __name__ == '__main__':
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     w = Main()
#     w.show()
#     sys.exit(app.exec_())
#
# class MainWindow(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.resize(600,400)
#         self.setWindowTitle("Treeview Example")
#
#         self.treeview = QtGui.QTreeView(self)
#
#         self.treeview.model = QtGui.QFileSystemModel()
#         self.treeview.model.setRootPath( QtCore.QDir.currentPath() )
#         self.treeview.setModel(self.treeview.model)
#         self.treeview.setColumnWidth(0, 200)
#
#         self.setCentralWidget(self.treeview)
#
#         self.treeview.clicked.connect(self.on_treeview_clicked)
#
# # ---------------------------------------------------------------------
#
#     @QtCore.pyqtSlot(QtCore.QModelIndex)
#     def on_treeview_clicked(self, index):
#         indexItem = self.treeview.model.index(index.row(), 0, index.parent())
#
#         # path or filename selected
#         fileName = self.treeview.model.fileName(indexItem)
#         # full path/filename selected
#         filePath = self.treeview.model.filePath(indexItem)
#
#         print(fileName)
#         print(filePath)
#
# # ---------------------------------------------------------------------
#
# if __name__ == '__main__':
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     w = MainWindow()
#     w.show()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt4 import QtCore, QtGui
#
# app = QtGui.QApplication(sys.argv)
#
# model = QtGui.QDirModel()
# tree = QtGui.QTreeView()
# tree.setModel(model)
#
# tree.setWindowTitle(tree.tr("Dir View"))
# tree.resize(640, 480)
# tree.show()
#
# sys.exit(app.exec_())
# from PyQt4 import QtCore, QtGui
#
#
# class TreeItem(object):
#     def __init__(self, data, parent=None):
#         self.parentItem = parent
#         self.itemData = data
#         self.childItems = []
#
#     def appendChild(self, item):
#         self.childItems.append(item)
#
#     def child(self, row):
#         return self.childItems[row]
#
#     def childCount(self):
#         return len(self.childItems)
#
#     def columnCount(self):
#         return len(self.itemData)
#
#     def data(self, column):
#         try:
#             return self.itemData[column]
#         except IndexError:
#             return None
#
#     def parent(self):
#         return self.parentItem
#
#     def row(self):
#         if self.parentItem:
#             return self.parentItem.childItems.index(self)
#         return 0
#
#
# class TreeModel(QtCore.QAbstractItemModel):
#     def __init__(self, data, parent=None):
#         super(TreeModel, self).__init__(parent)
#         self.rootItem = TreeItem(("Title", "Summary"))
#         self.setupModelData(data.split('\n'), self.rootItem)
#
#     def columnCount(self, parent):
#         if parent.isValid():
#             return parent.internalPointer().columnCount()
#         else:
#             return self.rootItem.columnCount()
#
#     def data(self, index, role):
#         if not index.isValid():
#             return None
#         if role != QtCore.Qt.DisplayRole:
#             return None
#         item = index.internalPointer()
#         return item.data(index.column())
#
#     def flags(self, index):
#         if not index.isValid():
#             return QtCore.Qt.NoItemFlags
#         return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
#
#     def headerData(self, section, orientation, role):
#         if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
#             return self.rootItem.data(section)
#         return None
#
#     def index(self, row, column, parent):
#         if not self.hasIndex(row, column, parent):
#             return QtCore.QModelIndex()
#         if not parent.isValid():
#             parentItem = self.rootItem
#         else:
#             parentItem = parent.internalPointer()
#         childItem = parentItem.child(row)
#         if childItem:
#             return self.createIndex(row, column, childItem)
#         else:
#             return QtCore.QModelIndex()
#
#     def parent(self, index):
#         if not index.isValid():
#             return QtCore.QModelIndex()
#         childItem = index.internalPointer()
#         parentItem = childItem.parent()
#         if parentItem == self.rootItem:
#             return QtCore.QModelIndex()
#         return self.createIndex(parentItem.row(), 0, parentItem)
#
#     def rowCount(self, parent):
#         if parent.column() > 0:
#             return 0
#         if not parent.isValid():
#             parentItem = self.rootItem
#         else:
#             parentItem = parent.internalPointer()
#         return parentItem.childCount()
#
#     def setupModelData(self, lines, parent):
#         parents = [parent]
#         indentations = [0]
#         number = 0
#         while number < len(lines):
#             position = 0
#             while position < len(lines[number]):
#                 if lines[number][position] != ' ':
#                     break
#                 position += 1
#             lineData = lines[number][position:].trimmed()
#             if lineData:
#                 # Read the column data from the rest of the line.
#                 columnData = [s for s in lineData.split('\t') if s]
#                 if position > indentations[-1]:
#                     # The last child of the current parent is now the new
#                     # parent unless the current parent has no children.
#                     if parents[-1].childCount() > 0:
#                         parents.append(parents[-1].child(parents[-1].childCount() - 1))
#                         indentations.append(position)
#                 else:
#                     while position < indentations[-1] and len(parents) > 0:
#                         parents.pop()
#                         indentations.pop()
#                 # Append a new item to the current parent's list of children.
#                 parents[-1].appendChild(TreeItem(columnData, parents[-1]))
#             number += 1
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QtGui.QApplication(sys.argv)
#
#     f = QtCore.QFile(':/default.txt')
#     f.open(QtCore.QIODevice.ReadOnly)
#     model = TreeModel(f.readAll())
#     f.close()
#
#     view = QtGui.QTreeView()
#     view.setModel(model)
#     view.setWindowTitle("Simple Tree Model")
#     view.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt4 import QtGui,QtCore
#
# class Myview(QtGui.QMainWindow):
#     def __init__(self,parent=None):
#         QtGui.QMainWindow.__init__(self)
#         model = QtGui.QFileSystemModel()
#         model.setRootPath('C:\Myfolder')
#         view = QtGui.QTreeView()
#         view.setModel(model)
#         self.setCentralWidget(view)
#
#
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     myview = Myview()
#     myview.show()
#     sys.exit(app.exec_())