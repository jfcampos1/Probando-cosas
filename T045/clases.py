__author__ = 'JuanFrancisco'
from random import uniform, randrange, expovariate, randint


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


class Casa:
    materiales_peso = {'madera': 10, 'ladrillos': 7, 'hormigon': 4, 'metal': 2}
    materiales_tiempo_apagar = {'madera': [1800, 7200], 'ladrillos': [2400, 6000], 'hormigon': [3600, 4800],
                                'metal': [1800, 2400]}
    todas_casas = []

    def __init__(self, material, tiempo_robo, cordenadas):
        self.material = material
        self.peso = Casa.materiales_peso[material]
        self.tiempo_apagar = Casa.materiales_tiempo_apagar[material]
        self.tiempo_robo = tiempo_robo
        self.cordenadas = cordenadas
        self.calles_casa=[]
        Casa.todas_casas.append(self)

    def encontrar_calle(self, mapa):
        orden = Casa.todas_casas
        for i in range(len(orden)):
            fijar = orden[i].cordenadas
            opciones = []
            if fijar[0] - 2 >= 0:
                if mapa[fijar[0] - 2][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0] - 2][fijar[1] - 1])
            if fijar[0] < len(mapa):
                if mapa[fijar[0]][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0]][fijar[1] - 1])
            if fijar[1] - 2 >= 0:
                if mapa[fijar[0] - 1][fijar[1] - 2] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1] - 2])
            if fijar[1] < len(mapa[0]):
                if mapa[fijar[0] - 1][fijar[1]] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1]])
            orden[i].calles_casa=opciones



    def proximo_robo(self, comisaria):
        cantidad_casas = len(Casa.todas_casas)
        todos_pesos = []
        for i in range(cantidad_casas):
            peso = 10 + abs(Casa.todas_casas[i].cordenadas[0] - comisaria[0]) + abs(
                Casa.todas_casas[i].cordenadas[1] - comisaria[1])
            todos_pesos.append(peso)
        suma_pesos = 0
        for i in todos_pesos:
            suma_pesos += i
        numero = randint(11, suma_pesos)
        casa = ''
        cont = 0
        for i in range(cantidad_casas):
            if numero - todos_pesos[i] < 0 and cont == 0:
                cont = 1
                casa = i
            else:
                numero -= todos_pesos[i]
        casa_robada = Casa.todas_casas[casa]
        return casa_robada

    def proximo_incendio(self):
        cantidad_casas = len(Casa.todas_casas)
        todos_pesos = 0
        for i in Casa.todas_casas:
            todos_pesos += i.peso
        probabilidad_todas = []
        for i in Casa.todas_casas:
            prob = i.peso / todos_pesos
            probabilidad_todas.append(prob)
        base = 2 / todos_pesos
        numero = uniform(base, 1)
        cont = 0
        casa = ''
        for i in range(cantidad_casas):
            if numero - probabilidad_todas[i] < 0 and cont == 0:
                cont = 1
                casa = i
            else:
                numero -= probabilidad_todas[i]
        casa_quemada = Casa.todas_casas[casa]
        return casa_quemada

    def proximo_enfermo(self):
        numero = randrange(len(Casa.todas_casas))
        casa_enfermo = Casa.todas_casas[numero]
        return casa_enfermo

    def tiempo_inicio_eventos(self):
        incendio = expovariate(1 / 10) * 3600
        robo = expovariate(1 / 4) * 3600
        enfermo = expovariate(1 / 2) * 3600
        casa_incendio = self.proximo_incendio()
        patrulla = Edificios.edificio['comisaria']
        casa_robo = self.proximo_robo(patrulla[0])
        casa_enfermo = self.proximo_enfermo()
        nuevo = Eventos('incendio', incendio, casa_incendio, 0)
        nuevo2 = Eventos('robo', robo, casa_robo, 0)
        nuevo3 = Eventos('enfermo', enfermo, casa_enfermo, 0)

    def cambiar_estado(self, grilla, evento):
        if evento.evento == 'enfermo':
            grilla.agregar_enfermo(self.cordenadas[0], self.cordenadas[1])
        elif evento.evento == 'robo':
            grilla.agregar_robo(self.cordenadas[0], self.cordenadas[1])
        elif evento.evento == 'incendio':
            grilla.agregar_incendio(self.cordenadas[0], self.cordenadas[1])


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
        self.stop=False
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

    def mover(self,mapa,grilla):
        calle=self.casa.calles_casa[0]
        if mapa[calle.cordenadas[0]-1][calle.cordenadas[1]-1].ocupado is False:
            direccion = calle.direccion
            b = 0
            espejo = False
            if direccion == 'izquierda':
                espejo = True
            elif direccion == 'arriba':
                b = -90
            elif direccion == 'abajo':
                b = 90
            if self.vehiculo=='clinica':
                self.stop=True
                mapa[calle.cordenadas[0]-1][calle.cordenadas[1]-1].ocupado=self
                grilla.agregar_ambulancia(calle.cordenadas[0], calle.cordenadas[1], b, espejo)
            elif self.vehiculo=='comisaria':
                self.stop=True
                mapa[calle.cordenadas[0]-1][calle.cordenadas[1]-1].ocupado=self
                grilla.agregar_patrulla(calle.cordenadas[0], calle.cordenadas[1], b, espejo)
            elif self.vehiculo=='bomba':
                self.stop=True
                mapa[calle.cordenadas[0]-1][calle.cordenadas[1]-1].ocupado=self
                grilla.agregar_carro_bomba(calle.cordenadas[0], calle.cordenadas[1], b, espejo)



class Edificios:
    edificio = {}

    def __init__(self, ubi_clinica, ubi_comisaria, ubi_bomba):
        self.clinica = ubi_clinica
        self.calle_clinica = ''
        self.comisaria = ubi_comisaria
        self.calle_comisaria = ''
        self.bomba = ubi_bomba
        self.calle_bomba = ''
        Edificios.edificio = {'comisaria': [self.comisaria, self.calle_comisaria],
                              'clinica': [self.clinica, self.calle_clinica], 'bomba': [self.bomba, self.calle_bomba]}

    def encontrar_calle(self, mapa):
        orden = [self.clinica, self.comisaria, self.bomba]
        calles = [self.calle_clinica, self.calle_comisaria, self.calle_bomba]
        for i in range(3):
            fijar = orden[i]
            opciones = []
            if fijar[0] - 2 >= 0:
                if mapa[fijar[0] - 2][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0] - 2][fijar[1] - 1])
            if fijar[0] < len(mapa):
                if mapa[fijar[0]][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0]][fijar[1] - 1])
            if fijar[1] - 2 >= 0:
                if mapa[fijar[0] - 1][fijar[1] - 2] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1] - 2])
            if fijar[1] < len(mapa[0]):
                if mapa[fijar[0] - 1][fijar[1]] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1]])
            if i == 0:
                self.calle_clinica = opciones
                Edificios.edificio['clinica'] = [self.clinica, self.calle_clinica]
            elif i == 1:
                self.calle_comisaria = opciones
                Edificios.edificio['comisaria'] = [self.comisaria, self.calle_comisaria]
            else:
                self.calle_bomba = opciones
                Edificios.edificio['bomba'] = [self.bomba, self.calle_bomba]
