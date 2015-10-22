__author__ = 'JuanFrancisco'

from collections import deque
from random import expovariate, randrange, choice
from _datetime import datetime

from PyQt4 import QtGui

from clases import Vehiculo
from Leerarchivo import nuevo_mapa, cantidad_calles_lista


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
        t = datetime.now()
        app = QtGui.QApplication([])
        lista_casas, mapa_calles, lista_vacios, lista_calle_entrada, lista_calle_salida, grilla, esquinas = nuevo_mapa(
            app)
        grilla.show()
        cantidad_calles,lista_calles=cantidad_calles_lista(mapa_calles)
        cantidad_vehiculos_max = cantidad_calles // 2
        entradas = len(lista_calle_entrada)
        grilla.actualizar()
        self.proximo_auto(self.tasa_llegada)
        while self.tiempo_simulacion < self.tiempo_maximo_sim:
            grilla.tiempo_intervalo = 1
            if cantidad_vehiculos_max > len(Vehiculo.cantidad_autos):
                p_taxi=randrange(10)
                rand = randrange(entradas)
                cordenadas = lista_calle_entrada[rand].cordenadas
                if p_taxi<2:
                    grilla.agregar_taxi(cordenadas[0], cordenadas[1], 90, False)
                    taxi = Vehiculo('taxi', self.tiempo_simulacion, cordenadas)
                    Vehiculo.cantidad_autos.append(taxi)
                else:
                    tipo_auto = choice(['sedan', 'camioneta', 'convertible'])
                    if tipo_auto == 'sedan':
                        grilla.agregar_sedan(cordenadas[0], cordenadas[1], 90, False)
                    elif tipo_auto == 'camioneta':
                        grilla.agregar_pickup(cordenadas[0], cordenadas[1], 90, False)
                    elif tipo_auto == 'convertible':
                        grilla.agregar_convertible(cordenadas[0], cordenadas[1], 90, False)
                    auto2 = Vehiculo(tipo_auto, self.tiempo_simulacion, cordenadas)
                    Vehiculo.cantidad_autos.append(auto2)
            for i in Vehiculo.cantidad_autos:
                if i.tiempo_llegada + i.velocidad < self.tiempo_simulacion:
                    i.tiempo_llegada += i.velocidad
                elif i.tiempo_llegada + i.velocidad >= self.tiempo_simulacion:
                    if i.tipo=='taxi' and i.libre is True:
                        if i.tiempo_libre>=self.tiempo_simulacion:
                            i.destino_taxi(mapa_calles,lista_calles, esquinas)
                        calle = mapa_calles[i.cordenadas_vehiculo[0] - 1][i.cordenadas_vehiculo[1] - 1]
                        calle.siguiente_calle(mapa_calles, lista_calle_salida, grilla, i, esquinas)
                    elif i.tipo=='taxi' and i.libre is False:
                        pass
                    i.tiempo_llegada += i.velocidad
                    calle = mapa_calles[i.cordenadas_vehiculo[0] - 1][i.cordenadas_vehiculo[1] - 1]
                    calle.siguiente_calle(mapa_calles, lista_calle_salida, grilla, i, esquinas)
            grilla.actualizar()
            self.tiempo_simulacion += 0.5
        print(datetime.now() - t)
        print(len(Vehiculo.cantidad_autos), cantidad_vehiculos_max)
        app.exec_()
        print()
        print('Estadisticas:')


if __name__ == '__main__':
    vehiculos = {'taxi': 1.0 / 8, 'auto': 1.0 / 15, 'camioneta': 1.0 / 20}
    tasa_llegada_vehiculos = 1 / 5
    s = Simulacion(10000, tasa_llegada_vehiculos, vehiculos)
    s.run()
