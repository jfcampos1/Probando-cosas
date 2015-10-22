__author__ = 'JuanFrancisco'
from random import uniform, randrange, expovariate


class Calle:
    def __init__(self, direccion, cordenadas):
        self.direccion = direccion
        self.cordenadas = cordenadas  # cordenadas con +1
        self.ocupado = None
        self.evento = False

    def mostrar_tablero(self, mapa):
        mapa = mapa
        r = ' '
        for i in range(len(mapa[0])):
            r += ' ' + str(i + 1)
        print(r)
        for i in range(len(mapa)):
            r = chr(65 + i) + ' '
            for j in mapa[i]:
                if j == '':
                    j = '0'
                else:
                    j = '1'
                r += j + ' '
            print(r)

    def siguiente_calle(self, mapa, lista_salida, grilla, auto, esquinas, especial):
        if self.direccion == 'izquierda':
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
                if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                    if calle_elegida.direccion == 'abajo':
                        b = 90
                    elif calle_elegida.direccion == 'arriba':
                        b = -90
                    elif calle_elegida.direccion == 'izquierda':
                        b = 0
                        espejo = True
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] == '':
                    espejo = True
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] - 1]
                else:
                    espejo = True
                    corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = None
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
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
                if mapa[self.cordenadas[0] - 1][self.cordenadas[1]] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                    if calle_elegida.direccion == 'abajo':
                        b = 90
                    elif calle_elegida.direccion == 'derecha':
                        b = 0
                        espejo = False
                    elif calle_elegida.direccion == 'arriba':
                        b = -90
                        espejo = False
                elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]] == '':
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] + 1, self.cordenadas[1] + 1]
                else:
                    corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = None
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
        elif self.direccion == 'arriba':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = None
                    del auto
            else:
                b = -90
                espejo = False
                corde = []
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
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
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] == '':
                    if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
                else:
                    corde = [self.cordenadas[0] - 1, self.cordenadas[1]]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = None
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)
        elif self.direccion == 'abajo':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                if especial == 1:
                    return False
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    Vehiculo.cantidad_autos.remove(auto)
                    self.ocupado = None
                    del auto
            else:
                b = 90
                espejo = False
                corde = []
                if mapa[self.cordenadas[0]][self.cordenadas[1] - 1] in esquinas:
                    lugares_doblar = self.doblar_esquinas(1, mapa, esquinas)
                    calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                    corde = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
                    if calle_elegida.direccion == 'abajo':
                        b = 90
                    elif calle_elegida.direccion == 'derecha':
                        b = 0
                        espejo = False
                    elif calle_elegida.direccion == 'izquierda':
                        b = 0
                        espejo = True
                elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1] == '':
                    if mapa[self.cordenadas[0]][self.cordenadas[1] - 2] != '':
                        corde = [self.cordenadas[0], self.cordenadas[1] - 1]
                    elif mapa[self.cordenadas[0]][self.cordenadas[1]] != '':
                        corde = [self.cordenadas[0], self.cordenadas[1] + 1]
                else:
                    corde = [self.cordenadas[0] + 1, self.cordenadas[1]]
                if especial == 1:
                    return mapa[corde[0] - 1][corde[1] - 1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    self.ocupado = None
                    auto.cordenadas_vehiculo = [corde[0], corde[1]]
                    mapa[corde[0] - 1][corde[1] - 1].ocupado = auto
                    if auto.tipo == 'sedan':
                        grilla.agregar_sedan(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'camioneta':
                        grilla.agregar_pickup(corde[0], corde[1], b, espejo)
                    elif auto.tipo == 'convertible':
                        grilla.agregar_convertible(corde[0], corde[1], b, espejo)

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
                    posibles_lugares=calle.doblar_esquinas(2, mapa, esquinas)

                camino.append(calle)
                calle.ir_destino(mapa, auto, esquinas, camino=camino)


class Casa:
    materiales_peso = {'madera': 10, 'ladrillos': 7, 'hormigon': 4, 'metal': 2}
    materiales_tiempo_apagar = {'madera': [30, 120], 'ladrillos': [40, 100], 'hormigon': [60, 80], 'metal': [30, 40]}

    def __init__(self, material, tiempo_robo, cordenadas):
        self.material = material
        self.peso = Casa.materiales_peso[material]
        self.tiempo_apagar = Casa.materiales_tiempo_apagar[material]
        self.tiempo_robo = tiempo_robo
        self.cordenadas = cordenadas


class Vehiculo:
    cantidad_autos = []

    def __init__(self, tipo, tiempo_llegada, cordenadas):
        self.tipo = tipo
        self.tiempo_llegada = tiempo_llegada
        self.velocidad = uniform(0.5, 1)
        self.cordenadas_vehiculo = cordenadas
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
