__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, QtCore
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # self.socket()

        roomLabel = QtGui.QLabel('room')

        # self.browser = QtGui.QTextBrowser()
        # self.browser.backwardAvailable()

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setMaximumSize(QtCore.QSize(400,60))
        #4 edit line
        # self.connect(self.browser, QtCore.SIGNAL("returnPressed()"),self.callback)

        SendButton = QtGui.QPushButton('Send')
        SendButton.setMaximumSize(QtCore.QSize(400,60))
        # SendButton.clicked.connect(self.callback)




        layoutINlayout = QtGui.QHBoxLayout()
        layoutINlayout.addWidget(self.textEdit)
        layoutINlayout.addWidget(SendButton)


        widget = QtGui.QWidget()
        self.setCentralWidget(widget)

        self.layout = QtGui.QVBoxLayout()
        # self.layout.addWidget(self.browser)

        mainwindow = QtGui.QVBoxLayout()
        mainwindow.addLayout (self.layout )
        mainwindow.addLayout (layoutINlayout )

        widget.setLayout(mainwindow)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint )

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
