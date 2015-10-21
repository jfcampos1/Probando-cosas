__author__ = 'JuanFrancisco'
from random import uniform, randrange


class Calle:
    def __init__(self, direccion, cordenadas):
        self.direccion = direccion
        self.cordenadas = cordenadas  # cordenadas con +1
        self.ocupado = None

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

    # def simplifica_siguiente_calle(self, mapa, grilla, numero, x, y, auto):
    #     if numero == 1:
    #         if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)] != '':
    #             if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'arriba':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1]]
    #             elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'abajo' or \
    #                             mapa[self.cordenadas[1] + 1][self.cordenadas[0] + (1 * y)].direccion == 'abajo':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] + 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] + 1, self.cordenadas[1]]
    #             else:
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1]]
    #         elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)] != '':
    #             if mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'arriba':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1]]
    #             elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'abajo':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] + 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] + 1, self.cordenadas[1]]
    #             else:
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0] + 1, self.cordenadas[1], 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0] + 1, self.cordenadas[1]]
    #     elif numero == 2:
    #         if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)] != '':
    #             if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'derecha':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] + 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] + 1]
    #             elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'izquierda':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] - 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] - 1]
    #             else:
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] - 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] - 1]
    #         elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]] != '':
    #             if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]].direccion == 'derecha':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] + 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] + 1]
    #             elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]].direccion == 'izquierda':
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] - 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] - 1]
    #             else:
    #                 grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
    #                 grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] + 1, 0, False)
    #                 auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] + 1]

    def siguiente_calle(self, mapa, lista_salida, grilla, auto, esquinas):
        if self.direccion == 'izquierda':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] in esquinas:
                lugares_doblar = self.doblar_esquinas(mapa, esquinas)
                calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                b = 0
                espejo = False
                if calle_elegida.direccion == 'abajo':
                    b = 90
                elif calle_elegida.direccion == 'arriba':
                    b = -90
                    espejo = False
                elif calle_elegida.direccion == 'izquierda':
                    b = 0
                    espejo = True
                grilla.agregar_convertible(calle_elegida.cordenadas[0], calle_elegida.cordenadas[1], b, espejo)
                auto.cordenadas_vehiculo = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] - 1, 0, True)
                auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] - 1]
        elif self.direccion == 'derecha':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0] - 1][self.cordenadas[1]] in esquinas:
                lugares_doblar = self.doblar_esquinas(mapa, esquinas)
                calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                b = 0
                espejo = False
                if calle_elegida.direccion == 'abajo':
                    b = 90
                elif calle_elegida.direccion == 'derecha':
                    b = 0
                    espejo = False
                elif calle_elegida.direccion == 'arriba':
                    b = -90
                    espejo = False
                grilla.agregar_convertible(calle_elegida.cordenadas[0], calle_elegida.cordenadas[1], b, espejo)
                auto.cordenadas_vehiculo = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_convertible(self.cordenadas[0], self.cordenadas[1] + 1, 0, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1] + 1]
        elif self.direccion == 'arriba':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] in esquinas:
                lugares_doblar = self.doblar_esquinas(mapa, esquinas)
                calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                b = 0
                espejo = False
                if calle_elegida.direccion == 'arriba':
                    b = -90
                    espejo = False
                elif calle_elegida.direccion == 'derecha':
                    b = 0
                    espejo = False
                elif calle_elegida.direccion == 'izquierda':
                    b = 0
                    espejo = True
                grilla.agregar_convertible(calle_elegida.cordenadas[0], calle_elegida.cordenadas[1], b, espejo)
                auto.cordenadas_vehiculo = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
            elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] == '':
                if mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 2] != '':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1] - 1, -90, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1] - 1]
                elif mapa[self.cordenadas[0] - 2][self.cordenadas[1]] != '':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1] + 1, -90, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1] + 1]
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_convertible(self.cordenadas[0] - 1, self.cordenadas[1], -90, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0] - 1, self.cordenadas[1]]
        elif self.direccion == 'abajo':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1] in esquinas:
                lugares_doblar = self.doblar_esquinas(mapa, esquinas)
                calle_elegida = lugares_doblar[randrange(len(lugares_doblar))]
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                b = 0
                espejo = False
                if calle_elegida.direccion == 'abajo':
                    b = 90
                elif calle_elegida.direccion == 'derecha':
                    b = 0
                    espejo = False
                elif calle_elegida.direccion == 'izquierda':
                    b = 0
                    espejo = True
                grilla.agregar_convertible(calle_elegida.cordenadas[0], calle_elegida.cordenadas[1], b, espejo)
                auto.cordenadas_vehiculo = [calle_elegida.cordenadas[0], calle_elegida.cordenadas[1]]
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_convertible(self.cordenadas[0] + 1, self.cordenadas[1], 90, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0] + 1, self.cordenadas[1]]

    def doblar_esquinas(self, mapa, esquinas):
        lugares_cambio = []
        if self.direccion == 'abajo':
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
        elif self.direccion == 'arriba':
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
        elif self.direccion == 'izquierda':
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
        elif self.direccion == 'derecha':
            posibles_lugares = []
            print(self.cordenadas[0], self.cordenadas[1])
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
        return lugares_cambio


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
    tipo_auto = {'auto': 0, 'taxi': 0}
    cantidad_autos = []

    def __init__(self, tipo, tiempo_llegada, cordenadas):
        self.tipo = tipo
        self.tipo_vehiculo = Vehiculo.tipo_auto[tipo]
        self.tiempo_llegada = tiempo_llegada
        self.velocidad = uniform(0.5, 1)
        self.cordenadas_vehiculo = cordenadas

    def __repr__(self):
        return 'Tipo vehiculo: {0}'.format(self.tipo_vehiculo)
