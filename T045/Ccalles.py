__author__ = 'JuanFrancisco'
from random import randrange

from Cvehiculo import Vehiculo


class Calle:
    def __init__(self, direccion, cordenadas):
        self.direccion = direccion
        self.cordenadas = cordenadas  # cordenadas con +1
        self.ocupado = False
        self.evento = False

    def mostrar_tablero(self, mapa):
        mapa = mapa
        r = ' '
        for i in range(len(mapa[0])):
            r += ' ' + str(i + 1)
        print(r)
        for i in range(len(mapa)):
            r = str(i + 1) + ' '
            for j in mapa[i]:
                if j == '':
                    j = '0'
                else:
                    j = '1'
                r += j + ' '
            print(r)

    def __repr__(self):
        return 'Cordenadas calle: {0}'.format(self.cordenadas)

    def siguiente_calle(self, mapa, lista_salida, grilla, auto, esquinas, especial, tiempo_actual):
        if self.direccion == 'izquierda':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = False
                    del auto
            else:
                b = 0
                espejo = False
                corde = []
                se_cambio = False
                intento_cambiarse = 0
                cordenadas = []
                if self.cordenadas[0] - 2 <= 0:
                    for i in range(len(mapa[0])):
                        if mapa[0][i] == '':
                            cordenadas = [2, i + 1]
                else:
                    cordenadas = self.cordenadas
                if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] in esquinas:
                    semaforo = Semaforo.semaforo[0]
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    if semaforo.horizontal is True and calle_elegida.ocupado is False:
                        corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                        if calle_elegida.direccion == 'abajo':
                            b = 90
                        elif calle_elegida.direccion == 'arriba':
                            b = -90
                        elif calle_elegida.direccion == 'izquierda':
                            b = 0
                            espejo = True
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        auto.stop = False
                    else:
                        auto.stop = True
                    se_cambio = True
                elif mapa[cordenadas[0] - 2][cordenadas[1] - 1] != '':
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado is False:
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                        espejo = True
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                        se_cambio = True
                    else:
                        intento_cambiarse = 1
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] == '':
                    espejo = True
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] - 1]
                    auto.tiempo_llegada += 0.5
                    auto.stop = False
                    se_cambio = True
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado is not False:
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado.stop is False:
                        espejo = True
                        corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                        auto.stop = False
                        auto.velocidad = mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado.velocidad
                        auto.tiempo_llegada += auto.velocidad
                    elif mapa[self.cordenadas[0]][self.cordenadas[1] - 2].ocupado is False and mapa[self.cordenadas[0]][
                                self.cordenadas[1] - 1].ocupado is False:
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] - 1]
                        auto.stop = False
                        auto.tiempo_llegada += 0.5
                    else:
                        auto.stop = True
                    se_cambio = True
                if intento_cambiarse == 0 and se_cambio is False:
                    espejo = True
                    corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                    auto.stop = False
                    auto.velocidad = auto.velocidad_inicial
                    auto.tiempo_llegada += auto.velocidad
                elif se_cambio is True:
                    pass
                else:
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] == '':
                        espejo = True
                        if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                            corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                        elif mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                            corde = [self.cordenadas[0] + 1, self.cordenadas[1] - 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                    elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado is not False:
                        if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado.stop is False:
                            espejo = True
                            corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                            auto.stop = False
                            auto.velocidad = mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado.velocidad
                            auto.tiempo_llegada += auto.velocidad
                        else:
                            auto.stop = True
                    else:
                        espejo = True
                        corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                        auto.stop = False
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                elif auto.stop is True:
                    espejo = True
                    corde = [auto.cordenadas_vehiculo[0], auto.cordenadas_vehiculo[1]]
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = False
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
        elif self.direccion == 'derecha':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = None
                    del auto
            else:
                b = 0
                espejo = False
                corde = []
                se_cambio = False
                intento_cambiarse = 0
                cordenadas = []
                if self.cordenadas[0] >= len(mapa):
                    for i in range(len(mapa[0])):
                        if mapa[0][i] == '':
                            cordenadas = [0, i + 1]
                else:
                    cordenadas = self.cordenadas
                if mapa[self.cordenadas[0] - 1][self.cordenadas[1]] in esquinas:
                    semaforo = Semaforo.semaforo[0]
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    if semaforo.horizontal is True and calle_elegida.ocupado is False:
                        corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                        if calle_elegida.direccion == 'abajo':
                            b = 90
                        elif calle_elegida.direccion == 'derecha':
                            b = 0
                        elif calle_elegida.direccion == 'arriba':
                            b = -90
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        auto.stop = False
                    else:
                        auto.stop = True
                    se_cambio = True
                elif mapa[cordenadas[0]][cordenadas[1] - 1] != '':
                    if mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado is False:
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                        se_cambio = True
                    else:
                        intento_cambiarse = 1
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]] == '':
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] + 1]
                    auto.tiempo_llegada += 0.5
                    auto.stop = False
                    se_cambio = True
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado is not False:
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado.stop is False:
                        corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                        auto.stop = False
                        auto.velocidad = mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado.velocidad
                        auto.tiempo_llegada += auto.velocidad
                    elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado is False and \
                                    mapa[self.cordenadas[0] - 2][self.cordenadas[1]].ocupado is False:
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                        auto.stop = False
                        auto.tiempo_llegada += 0.5
                    else:
                        auto.stop = True
                    se_cambio = True
                if intento_cambiarse == 0 and se_cambio is False:
                    corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                    auto.stop = False
                    auto.velocidad = auto.velocidad_inicial
                    auto.tiempo_llegada += auto.velocidad
                elif se_cambio is True:
                    pass
                else:
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1]] == '':
                        if mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                            corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                        elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                            corde = [self.cordenadas[0] + 1, self.cordenadas[1] + 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                    elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado is not False:
                        if mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado.stop is False:
                            corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                            auto.stop = False
                            auto.velocidad = mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado.velocidad
                            auto.tiempo_llegada += auto.velocidad
                        else:
                            auto.stop = True
                    else:
                        corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                        auto.stop = False
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                elif auto.stop is True:
                    corde = [auto.cordenadas_vehiculo[0], auto.cordenadas_vehiculo[1]]
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = False
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
        elif self.direccion == 'arriba':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = False
                    del auto
            else:
                b = -90
                espejo = False
                corde = []
                se_cambio = False
                intento_cambiarse = 0
                cordenadas = []
                if self.cordenadas[1] >= len(mapa[0]):
                    for i in range(len(mapa[0])):
                        if mapa[0][i] == '':
                            cordenadas = [1, i]
                else:
                    cordenadas = self.cordenadas
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    semaforo = Semaforo.semaforo[0]
                    if semaforo.vertical is True and calle_elegida.ocupado is False:
                        corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                        if calle_elegida.direccion == 'arriba':
                            b = -90
                            espejo = False
                        elif calle_elegida.direccion == 'derecha':
                            b = 0
                            espejo = False
                        elif calle_elegida.direccion == 'izquierda':
                            b = 0
                            espejo = True
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        auto.stop = False
                    else:
                        auto.stop = True
                    se_cambio = True
                elif mapa[cordenadas[0] - 1][cordenadas[1]] != '':
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado is False:
                        corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                        se_cambio = True
                    else:
                        intento_cambiarse = 1
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] == '':
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                    auto.tiempo_llegada += 0.5
                    auto.stop = False
                    se_cambio = True
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado is not False:
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado.stop is False:
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                        auto.stop = False
                        auto.velocidad = mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado.velocidad
                        auto.tiempo_llegada += auto.velocidad
                    elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado is False and \
                                    mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado is False:
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                        auto.stop = False
                        auto.tiempo_llegada += 0.5
                    else:
                        auto.stop = True
                    se_cambio = True
                if intento_cambiarse == 0 and se_cambio is False:
                    corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                    auto.stop = False
                    auto.velocidad = auto.velocidad_inicial
                    auto.tiempo_llegada += auto.velocidad
                elif se_cambio is True:
                    pass
                else:
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] == '':
                        if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                            corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                        elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                            corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                    elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado is not False:
                        if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado.stop is False:
                            corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                            auto.stop = False
                            auto.velocidad = mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1].ocupado.velocidad
                            auto.tiempo_llegada += auto.velocidad
                        else:
                            auto.stop = True
                    else:
                        auto.stop = False
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                elif auto.stop is True:
                    corde = [auto.cordenadas_vehiculo[0], auto.cordenadas_vehiculo[1]]
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = False
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
        elif self.direccion == 'abajo':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = False
                    del auto
            else:
                b = 90
                espejo = False
                corde = []
                se_cambio = False
                intento_cambiarse = 0
                cordenadas = []
                if self.cordenadas[1] - 2 < 0:
                    for i in range(len(mapa[0])):
                        if mapa[0][i] == '':
                            cordenadas = [1, i + 2]
                else:
                    cordenadas = self.cordenadas
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 1] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    semaforo = Semaforo.semaforo[0]
                    if semaforo.vertical is True and calle_elegida.ocupado is False:
                        corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                        if calle_elegida.direccion == 'abajo':
                            b = 90
                        elif calle_elegida.direccion == 'derecha':
                            b = 0
                            espejo = False
                        elif calle_elegida.direccion == 'izquierda':
                            b = 0
                            espejo = True
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        auto.stop = False
                    else:
                        auto.stop = True
                    se_cambio = True
                elif mapa[cordenadas[0] - 1][cordenadas[1] - 2] != '':
                    if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2].ocupado is False:
                        corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                        se_cambio = True
                    else:
                        intento_cambiarse = 1
                elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1] == '':
                    if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                    auto.tiempo_llegada += 0.5
                    auto.stop = False
                    se_cambio = True
                elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado is not False:
                    if mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado.stop is False:
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                        auto.stop = False
                        auto.velocidad = mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado.velocidad
                        auto.tiempo_llegada += auto.velocidad
                    elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]].ocupado is False and mapa[self.cordenadas[0]][
                        self.cordenadas[1]].ocupado is False:
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] + 1]
                        auto.stop = False
                        auto.tiempo_llegada += 0.5
                    else:
                        auto.stop = True
                    se_cambio = True
                if intento_cambiarse == 0 and se_cambio is False:
                    corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                    auto.stop = False
                    auto.velocidad = auto.velocidad_inicial
                    auto.tiempo_llegada += auto.velocidad
                elif se_cambio is True:
                    pass
                else:
                    if mapa[self.cordenadas[0]][self.cordenadas[1] - 1] == '':
                        if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                            corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                        elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                            corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                        auto.tiempo_llegada += 0.5
                        auto.stop = False
                    elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado is not False:
                        if mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado.stop is False:
                            corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                            auto.stop = False
                            auto.velocidad = mapa[self.cordenadas[0]][self.cordenadas[1] - 1].ocupado.velocidad
                            auto.tiempo_llegada += auto.velocidad
                        else:
                            auto.stop = True
                    else:
                        auto.stop = False
                        auto.velocidad = auto.velocidad_inicial
                        auto.tiempo_llegada += auto.velocidad
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                elif auto.stop is True:
                    corde = [auto.cordenadas_vehiculo[0], auto.cordenadas_vehiculo[1]]
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = False
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'taxi':
                        grilla.agregar_taxi(corde[0], corde[1], b, espejo)

    def doblar_esquinas(self, inverso, mapa, esquinas):
        lugares_cambio = []
        direc = ''
        if inverso == 1:
            direc = self.direccion
        elif inverso == 2:
            if self.direccion == 'arriba':
                direc = 'abajo'
            elif self.direccion == 'abajo':
                direc = 'arriba'
            elif self.direccion == 'izquierda':
                direc = 'derecha'
            elif self.direccion == 'derecha':
                direc = 'izquierda'
        if direc == 'abajo':
            posibles_lugares = []
            if self.cordenadas[1] - 2 < 0:
                if mapa[self.cordenadas[0]][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0], self.cordenadas[1] - 2),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 2),
                                        (self.cordenadas[0], self.cordenadas[1] + 1),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 1),
                                        (self.cordenadas[0] + 2, self.cordenadas[1])]
            elif self.cordenadas[1] >= len(mapa[0]):
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0], self.cordenadas[1] - 3),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 3),
                                        (self.cordenadas[0], self.cordenadas[1]),
                                        (self.cordenadas[0] + 1, self.cordenadas[1]),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 1)]
            else:
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0], self.cordenadas[1] - 3),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 3),
                                        (self.cordenadas[0], self.cordenadas[1]),
                                        (self.cordenadas[0] + 1, self.cordenadas[1]),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 1)]
                elif mapa[self.cordenadas[0]][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0], self.cordenadas[1] - 2),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 2),
                                        (self.cordenadas[0], self.cordenadas[1] + 1),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] + 2, self.cordenadas[1] - 1),
                                        (self.cordenadas[0] + 2, self.cordenadas[1])]
            if inverso == 1:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
            elif inverso == 2:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
        elif direc == 'arriba':
            posibles_lugares = []
            if self.cordenadas[1] - 2 < 0:
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 1),
                                        (self.cordenadas[0] - 4, self.cordenadas[1])]
            elif self.cordenadas[1] >= len(mapa[0]):
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 2, self.cordenadas[1]),
                                        (self.cordenadas[0] - 3, self.cordenadas[1]),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 1)]
            else:
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 2, self.cordenadas[1]),
                                        (self.cordenadas[0] - 3, self.cordenadas[1]),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 1)]
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 4, self.cordenadas[1] - 1),
                                        (self.cordenadas[0] - 4, self.cordenadas[1])]
            if inverso == 1:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
            elif inverso == 2:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
        elif direc == 'izquierda':
            posibles_lugares = []
            if self.cordenadas[0] >= len(mapa):
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 3, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] - 4),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] - 4),
                                        (self.cordenadas[0], self.cordenadas[1] - 3),
                                        (self.cordenadas[0], self.cordenadas[1] - 2)]
            elif self.cordenadas[0] - 2 < 0:
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] - 4),
                                        (self.cordenadas[0], self.cordenadas[1] - 4),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 2)]
            else:
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] - 4),
                                        (self.cordenadas[0], self.cordenadas[1] - 4),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] + 1, self.cordenadas[1] - 2)]
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 3, self.cordenadas[1] - 3),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] - 2),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] - 4),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] - 4),
                                        (self.cordenadas[0], self.cordenadas[1] - 3),
                                        (self.cordenadas[0], self.cordenadas[1] - 2)]
            if inverso == 1:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
            elif inverso == 2:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
        elif direc == 'derecha':
            posibles_lugares = []
            if self.cordenadas[0] >= len(mapa):
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 3, self.cordenadas[1]),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 2),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] + 2),
                                        (self.cordenadas[0], self.cordenadas[1]),
                                        (self.cordenadas[0], self.cordenadas[1] + 1)]
            elif self.cordenadas[0] - 2 < 0:
                if mapa[self.cordenadas[0]][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1]),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] + 2),
                                        (self.cordenadas[0], self.cordenadas[1] + 2),
                                        (self.cordenadas[0] + 1, self.cordenadas[1]),
                                        (self.cordenadas[0] + 1, self.cordenadas[1])]
            else:
                if mapa[self.cordenadas[0]][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 2, self.cordenadas[1]),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] + 2),
                                        (self.cordenadas[0], self.cordenadas[1] + 2),
                                        (self.cordenadas[0] + 1, self.cordenadas[1]),
                                        (self.cordenadas[0] + 1, self.cordenadas[1])]
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] in esquinas:
                    posibles_lugares = [(self.cordenadas[0] - 3, self.cordenadas[1]),
                                        (self.cordenadas[0] - 3, self.cordenadas[1] + 1),
                                        (self.cordenadas[0] - 2, self.cordenadas[1] + 2),
                                        (self.cordenadas[0] - 1, self.cordenadas[1] + 2),
                                        (self.cordenadas[0], self.cordenadas[1]),
                                        (self.cordenadas[0], self.cordenadas[1] + 1)]
            if inverso == 1:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'derecha':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
            elif inverso == 2:
                for i in range(len(posibles_lugares)):
                    j, n = posibles_lugares[i]
                    if 0 <= n < len(mapa[0]) and 0 <= j < len(mapa):
                        if mapa[j][n] != '':
                            if i < 2:
                                if mapa[j][n].direccion == 'abajo':
                                    lugares_cambio.append(mapa[j][n])
                            elif 2 <= i <= 3:
                                if mapa[j][n].direccion == 'izquierda':
                                    lugares_cambio.append(mapa[j][n])
                            elif 3 < i <= 5:
                                if mapa[j][n].direccion == 'arriba':
                                    lugares_cambio.append(mapa[j][n])
        return lugares_cambio

    def ir_destino(self, mapa, auto, esquinas, camino=[]):
        if self == mapa[auto.cordenadas_vehiculo[0] - 1][auto.cordenadas_vehiculo[1] - 1]:
            return None
        else:
            if self.direccion == 'arriba':
                calle = mapa[self.cordenadas[0]][self.cordenadas[1] - 1]
                if calle in esquinas:
                    posibles_lugares = calle.doblar_esquinas(2, mapa, esquinas)

                camino.append(calle)
                calle.ir_destino(mapa, auto, esquinas, camino=camino)


class Semaforo:
    semaforo = []

    def __init__(self, tiempo_simulacion):
        self.vertical = True
        self.horizontal = False
        self.tiempo_simulacion = tiempo_simulacion
        Semaforo.semaforo.append(self)

    def cambiar_semaforo(self, tiempo_actual):
        if tiempo_actual >= self.tiempo_simulacion + 20:
            if self.vertical is True:
                self.vertical = False
                self.horizontal = True
                print('cambioo verticales rojos')
            elif self.horizontal is True:
                self.horizontal = False
                self.vertical = True
                print('cambio horizontales rojos')
            self.tiempo_simulacion = tiempo_actual
