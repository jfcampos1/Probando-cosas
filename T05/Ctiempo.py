__author__ = 'JuanFrancisco'
from PyQt4 import QtGui, QtCore

from Zombies import Character
from Perdiste import Perdiste
from Supply import SuplementoTread

s = 0
m = 0
h = 0


class Main(QtGui.QMainWindow):
    def __init__(self, ventana):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
        self.ventana = ventana

    def initUI(self):

        centralwidget = QtGui.QWidget(self)

        self.lcd = QtGui.QLCDNumber(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        grid = QtGui.QGridLayout()
        grid.addWidget(self.lcd, 2, 0, 1, 3)
        centralwidget.setLayout(grid)
        self.setCentralWidget(centralwidget)
        self.time = '0:0:0'

        # ---------Window settings --------------------------------

        self.setWindowTitle("Tiempo")
        self.setGeometry(10, 200, 280, 170)

    def Reset(self):
        global s, m, h

        self.timer.stop()

        s = 0
        m = 0
        h = 0

        self.time = "{0}:{1}:{2}".format(h, m, s)

        self.lcd.setDigitCount(len(self.time))
        self.lcd.display(self.time)

    def Start(self):
        global s, m, h

        self.timer.start(1000)

    def Time(self):
        global s, m, h

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

        self.time = "{0}:{1}:{2}".format(h, m, s)
        valor = self.ventana.tiempo_aparicion_zombies()
        self.ventana.aparicion_suplementos()
        if valor is not False:
            for i in range(valor):
                self.personaje = Character(parent=self.ventana, path="zombie/z_arriba_q.png")
                self.personaje.start()
        if self.ventana.prox_supply_ocupado is True:
            segundos = self.ventana.prox_supply
            minutos = 0
            while segundos > 59:
                if segundos > 59:
                    minutos += 1
                    segundos -= 59
            if m == minutos and segundos == s:
                self.sup = SuplementoTread(parent=self.ventana)
                self.sup.start()
                self.ventana.prox_supply_ocupado = False
        if self.ventana.vida <= 0:
            self.perdiste = Perdiste(self.ventana, self.ventana.inicio, self)
            self.perdiste.show()
            self.ventana.pausa()
            self.timer.stop()

        self.lcd.setDigitCount(len(self.time))
        self.lcd.display(self.time)


def main(ventana):
    main = Main(ventana)
    return main
