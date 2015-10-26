__author__ = 'JuanFrancisco'
from random import uniform,expovariate,randrange


class Vehiculo:
    cantidad_autos = []

    def __init__(self, tipo, tiempo_llegada, cordenadas):
        self.tipo = tipo
        self.tiempo_llegada = tiempo_llegada
        self.velocidad_inicial = uniform(0.5, 1)
        self.velocidad = self.velocidad_inicial
        self.cordenadas_vehiculo = cordenadas
        self.stop = False
        self.libre = True
        self.tiempo_libre = tiempo_llegada + expovariate(1 / 40)
        self.destino = None

    def destino_taxi(self, mapa, lista_calles, esquinas):
        posibilidades = len(lista_calles)
        b = False
        calle = ''
        while b is False:
            rand = randrange(posibilidades)
            calle = lista_calles[rand]
            if calle in esquinas or calle == mapa[self.cordenadas_vehiculo[0] - 1][self.cordenadas_vehiculo[1] - 1]:
                b = False
            else:
                b = True
        self.destino = calle

    def __repr__(self):
        return 'Tipo vehiculo: {0}'.format(self.tipo)
