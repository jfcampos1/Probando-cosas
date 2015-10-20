__author__ = 'JuanFrancisco'

from collections import deque
from random import expovariate, randint, randrange

from PyQt4 import QtGui

from clases import Vehiculo
from Leerarchivo import nuevo_mapa


class Taller:
    def __init__(self, tipos):
        self.tarea_actual = None
        self.tiempo_revision = 0
        self.tipos = tipos

    def pasar_vehiculo(self, vehiculo):
        self.tarea_actual = vehiculo
        self.tiempo_revision = round(expovariate(self.tipos[vehiculo.tipo]) + 0.5)

    @property
    def ocupado(self):
        return self.tarea_actual != None


class Simulacion:
    def __init__(self, tiempo_maximo, tasa_llegada, tipos):
        self.tiempo_maximo_sim = tiempo_maximo
        self.tasa_llegada = tasa_llegada
        self.tiempo_simulacion = 0
        self.tiempo_proximo_auto = 0
        self.tiempo_atencion = 0
        self.tiempo_espera = 0
        self.planta = Taller(tipos)
        self.cola_espera = deque()
        self.vehiculos_atendidos = 0

    def proximo_auto(self, tasa_llegada):
        # un auto llega cada 5 minutos
        self.tiempo_proximo_auto = self.tiempo_simulacion + round(expovariate(tasa_llegada) + 0.5)

    def run(self):
        app = QtGui.QApplication([])
        lista_casas, mapa_calles, lista_vacios, lista_calle_entrada, lista_calle_salida, grilla = nuevo_mapa(app)
        grilla.show()
        entradas = len(lista_calle_entrada)
        print(entradas)
        rand = randrange(entradas)
        print(rand)
        cordenadas = lista_calle_entrada[3].cordenadas
        auto = Vehiculo('auto', self.tiempo_simulacion, cordenadas)
        grilla.agregar_convertible(cordenadas[0], cordenadas[1], 90, False)  # al momento del random
        #  hacer posibilidades y que ocupe solo ese
        rand = randrange(entradas)
        cordenadas = lista_calle_entrada[0].cordenadas
        auto2 = Vehiculo('auto', self.tiempo_simulacion, cordenadas)
        grilla.agregar_convertible(cordenadas[0], cordenadas[1], 90, False)
        grilla.actualizar()
        lista_calle_entrada[rand].mostrar_tablero(mapa_calles)
        self.proximo_auto(self.tasa_llegada)
        while self.tiempo_simulacion < self.tiempo_maximo_sim:
            grilla.tiempo_intervalo = 1
            print(auto.cordenadas_vehiculo[0] - 1,auto.cordenadas_vehiculo[1] - 1)
            calle = mapa_calles[auto.cordenadas_vehiculo[0] - 1][auto.cordenadas_vehiculo[1] - 1]
            calle.siguiente_calle(mapa_calles, lista_calle_salida, grilla, auto)
            calle2 = mapa_calles[auto2.cordenadas_vehiculo[0] - 1][auto2.cordenadas_vehiculo[1] - 1]
            calle2.siguiente_calle(mapa_calles, lista_calle_salida, grilla, auto2)
            grilla.actualizar()
            self.tiempo_simulacion+=1
        app.exec_()
        print()
        print('Estadisticas:')


if __name__ == '__main__':
    vehiculos = {'taxi': 1.0 / 8, 'auto': 1.0 / 15, 'camioneta': 1.0 / 20}
    tasa_llegada_vehiculos = 1 / 5
    s = Simulacion(30, tasa_llegada_vehiculos, vehiculos)
    s.run()
