__author__ = 'JuanFrancisco'

from collections import deque
from random import expovariate, randint, randrange
from time import sleep

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
        entradas = len(lista_calle_entrada)
        print(entradas)
        rand = randrange(entradas)
        print(rand)
        cordenadas = lista_calle_entrada[rand].cordenadas
        auto = Vehiculo('auto', self.tiempo_simulacion, cordenadas)
        grilla.agregar_auto(cordenadas[0], cordenadas[1], 0, False)
        sleep(50)
        self.proximo_auto(self.tasa_llegada)

        while self.tiempo_simulacion < self.tiempo_maximo_sim:
            # lista_calle_entrada[rand].mostrar_tablero(mapa_calles)
            # calle=mapa_calles[auto.cordenadas_vehiculo[1]-1][auto.cordenadas_vehiculo[0]-1]
            # calle.siguiente_calle(mapa_calles,lista_calle_salida,grilla,auto)
            if (self.planta.ocupado and
                        self.tiempo_proximo_auto < self.tiempo_atencion) or (not self.planta.ocupado):

                self.tiempo_simulacion = self.tiempo_proximo_auto

            else:

                self.tiempo_simulacion = self.tiempo_atencion

            print('[SIMULACION] tiempo: {0} min'.format(self.tiempo_simulacion))

            if self.tiempo_simulacion == self.tiempo_proximo_auto:
                tipo = randint(1, 10)
                if tipo <= 2:
                    self.cola_espera.append(Vehiculo('taxi', self.tiempo_simulacion, [0, 1]))
                else:
                    self.cola_espera.append(Vehiculo('auto', self.tiempo_simulacion, [0, 1]))
                self.proximo_auto(self.tasa_llegada)

                print('[COLA] Llega {0} en tiempo simulacion: {1} min.'.format(
                    self.cola_espera[-1].tipo, self.tiempo_simulacion))

                if (not self.planta.ocupado) and (len(self.cola_espera) > 0):
                    proximo_vehiculo = self.cola_espera.popleft()  # sacamos un auto en la cola de atencion
                    self.planta.pasar_vehiculo(proximo_vehiculo)  # y lo pasamos a la planta

                    self.tiempo_atencion = self.tiempo_simulacion + self.planta.tiempo_revision

                    print('[PLANTA] Entra {0} con un tiempo de atencion esperado de {1} min.'. \
                          format(self.planta.tarea_actual.tipo, self.planta.tiempo_revision))

            else:

                #
                print('[PLANTA] Sale: {0} a los {1} min.'.format(
                    self.planta.tarea_actual.tipo, self.tiempo_simulacion))

                self.tiempo_espera += self.tiempo_simulacion - self.planta.tarea_actual.tiempo_llegada
                self.planta.tarea_actual = None
                self.vehiculos_atendidos += 1
            sleep(5)

        print()
        print('Estadisticas:')
        print('Tiempo total atencion {0} min.'.format(self.tiempo_atencion))
        print('Total de vehiculos atendidos: {0}'.format(self.vehiculos_atendidos))
        print('Tiempo promedio de espera {0} min.'.format(round(self.tiempo_espera / self.vehiculos_atendidos)))
        app.exec_()


if __name__ == '__main__':
    vehiculos = {'taxi': 1.0 / 8, 'auto': 1.0 / 15, 'camioneta': 1.0 / 20}
    tasa_llegada_vehiculos = 1 / 5
    s = Simulacion(50, tasa_llegada_vehiculos, vehiculos)
    s.run()
