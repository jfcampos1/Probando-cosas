__author__ = 'JuanFrancisco'
from Cedificio import Edificios
from Cvehiculo import Vehiculo


class Eventos:
    vehiculos = {'enfermo': 'clinica', 'incendio': 'bomba', 'robo': 'comisaria'}
    evento = []
    autos = []

    def __init__(self, tipo, tiempo, casa, tiempo_sim):
        self.evento = tipo
        self.tiempo = tiempo
        self.tiempo_simulacion = tiempo_sim
        self.vehiculo = Eventos.vehiculos[tipo]
        self.casa = casa
        self.en_proceso = False
        self.stop = False
        Eventos.evento.append(self)

    def crear_vehiculo(self, tiempo_llegada, grilla):
        if self.vehiculo == 'clinica':
            lugar, calle = Edificios.edificio['clinica']
            nuevo = Vehiculo('ambulancia', tiempo_llegada, calle[0].cordenadas)
            Eventos.autos.append(nuevo)
            direccion = calle[0].direccion
            b = 0
            espejo = False
            if direccion == 'izquierda':
                espejo = True
            elif direccion == 'arriba':
                b = -90
            elif direccion == 'abajo':
                b = 90
            grilla.agregar_ambulancia(calle[0].cordenadas[0], calle[0].cordenadas[1], b, espejo)
        elif self.vehiculo == 'bomba':
            print(Edificios.edificio['bomba'])
            calle = Edificios.edificio['bomba']
            nuevo = Vehiculo('carro_bombero', tiempo_llegada, calle[1][0].cordenadas)
            Eventos.autos.append(nuevo)
            direccion = calle[1][0].direccion
            b = 0
            espejo = False
            if direccion == 'izquierda':
                espejo = True
            elif direccion == 'arriba':
                b = -90
            elif direccion == 'abajo':
                b = 90
            grilla.agregar_carro_bomba(calle[1][0].cordenadas[0], calle[1][0].cordenadas[1], b, espejo)
        elif self.vehiculo == 'comisaria':
            lugar, calle = Edificios.edificio['comisaria']
            nuevo = Vehiculo('patrulla', tiempo_llegada, calle[0].cordenadas)
            Eventos.autos.append(nuevo)
            direccion = calle[0].direccion
            b = 0
            espejo = False
            if direccion == 'izquierda':
                espejo = True
            elif direccion == 'arriba':
                b = -90
            elif direccion == 'abajo':
                b = 90
            grilla.agregar_patrulla(calle[0].cordenadas[0], calle[0].cordenadas[1], b, espejo)

    def mover(self, mapa, grilla):
        calle = self.casa.calles_casa[0]
        if mapa[calle.cordenadas[0] - 1][calle.cordenadas[1] - 1].ocupado is False:
            direccion = calle.direccion
            b = 0
            espejo = False
            if direccion == 'izquierda':
                espejo = True
            elif direccion == 'arriba':
                b = -90
            elif direccion == 'abajo':
                b = 90
            if self.vehiculo == 'clinica':
                self.stop = True
                mapa[calle.cordenadas[0] - 1][calle.cordenadas[1] - 1].ocupado = self
                grilla.agregar_ambulancia(calle.cordenadas[0], calle.cordenadas[1], b, espejo)
            elif self.vehiculo == 'comisaria':
                self.stop = True
                mapa[calle.cordenadas[0] - 1][calle.cordenadas[1] - 1].ocupado = self
                grilla.agregar_patrulla(calle.cordenadas[0], calle.cordenadas[1], b, espejo)
            elif self.vehiculo == 'bomba':
                self.stop = True
                mapa[calle.cordenadas[0] - 1][calle.cordenadas[1] - 1].ocupado = self
                grilla.agregar_carro_bomba(calle.cordenadas[0], calle.cordenadas[1], b, espejo)

