__author__ = 'JuanFrancisco'
from math import atan,degrees,tan ,radians
print(degrees(atan(9/8)))
print(tan(radians(45)))
letra='holacomoestas'
print(letra[:-1])
import sys
from PyQt4 import QtGui, QtCore

s = 0
m = 0
h = 0

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        centralwidget = QtGui.QWidget(self)

        self.lcd = QtGui.QLCDNumber(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)

        # self.start = QtGui.QPushButton("Start",self)
        # self.start.clicked.connect(self.Start)
        #
        # self.stop = QtGui.QPushButton("Stop",self)
        # self.stop.clicked.connect(lambda: self.timer.stop())
        #
        # self.reset = QtGui.QPushButton("Reset",self)
        # self.reset.clicked.connect(self.Reset)

        grid = QtGui.QGridLayout()

        # grid.addWidget(self.start,1,0)
        # grid.addWidget(self.stop,1,1)
        # grid.addWidget(self.reset,1,2)
        grid.addWidget(self.lcd,2,0,1,3)

        centralwidget.setLayout(grid)

        self.setCentralWidget(centralwidget)
        self.time=''

#---------Window settings --------------------------------

        self.setWindowTitle("Tiempo")
        self.setGeometry(10,200,280,170)

    def Reset(self):
        global s,m,h

        self.timer.stop()

        s = 0
        m = 0
        h = 0

        self.time = "{0}:{1}:{2}".format(h,m,s)

        self.lcd.setDigitCount(len(self.time))
        self.lcd.display(self.time)

    def Start(self):
        global s,m,h

        self.timer.start(1000)

    def Time(self):
        global s,m,h

        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()

        self.time = "{0}:{1}:{2}".format(h,m,s)

        self.lcd.setDigitCount(len(self.time))
        self.lcd.display(self.time)

def main():
    main= Main()
    return main

