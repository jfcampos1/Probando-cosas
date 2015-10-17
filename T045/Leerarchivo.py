__author__ = 'JuanFrancisco'
from PyQt4 import QtGui

from clases import Calle, Casa

from gui.gui import GrillaSimulacion

def nuevo_mapa(grilla_simulacion):
    with open('mapa.txt', 'r', encoding='utf8') as arch:
        arch.readline()
        linea1 = arch.readline().strip()
        lista_vacios = []
        principio = True
        while principio is True:
            lista = linea1.split(' ')
            cordenadas = lista[0].split(',')
            cordenadas_bien = [int(cordenadas[1]) + 1, int(cordenadas[0]) + 1]
            if lista[1] == 'calle':
                grilla_simulacion.agregar_calle(cordenadas_bien[0], cordenadas_bien[1])
                calle = Calle(lista[2], cordenadas_bien)
            elif lista[1] == 'casa':
                grilla_simulacion.agregar_casa(cordenadas_bien[0], cordenadas_bien[1])
                ladrones = [int(lista[4][1:3]), int(lista[5][0:2])]
                casa = Casa(lista[3], lista[4], cordenadas_bien)
            elif lista[1] == 'vacio':
                lista_vacios.append(cordenadas_bien)
            linea1 = arch.readline().strip()
            if linea1 == '':
                principio = False
        grilla_simulacion.show()

app = QtGui.QApplication([])
grilla = GrillaSimulacion(app)
nuevo_mapa(grilla)
app.exec_()
