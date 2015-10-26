__author__ = 'JuanFrancisco'

from Ccalles import Calle
from gui.gui import GrillaSimulacion
from Ccasa import Casa


def nuevo_mapa(app):
    with open('mapa fix.txt', 'r', encoding='utf8') as arch:
        dimension = arch.readline().strip()
        dimension = dimension.split('x')
        grilla_simulacion = GrillaSimulacion(app, rows=int(dimension[0]), cols=(int(dimension[1]) + 1))
        linea1 = arch.readline().strip()
        lista_vacios = []
        lista_casas = []
        lista_calle_entrada = []
        lista_calle_salida = []
        principio = True
        mapa_calles = []
        for i in range(int(dimension[0])):
            mapa_calles.append([''] * (int(dimension[1]) + 1))
        while principio is True:
            lista = linea1.split(' ')
            cordenadas = lista[0].split(',')
            cordenadas_bien = [int(cordenadas[0]) + 1, int(cordenadas[1]) + 1]
            if lista[1] == 'calle':
                grilla_simulacion.agregar_calle(cordenadas_bien[0], cordenadas_bien[1])
                calle = Calle(lista[2], cordenadas_bien)
                mapa_calles[int(cordenadas[0])][int(cordenadas[1])] = calle
                if int(cordenadas[0]) == 0:
                    if lista[2] == 'arriba':
                        lista_calle_salida.append(calle)
                    elif lista[2] == 'abajo':
                        lista_calle_entrada.append(calle)
                elif int(cordenadas[1]) == 0:
                    if lista[2] == 'izquierda':
                        lista_calle_salida.append(calle)
                    elif lista[2] == 'derecha':
                        lista_calle_entrada.append(calle)
                elif int(cordenadas[0]) == int(dimension[0]):
                    if lista[2] == 'abajo':
                        lista_calle_salida.append(calle)
                    elif lista[2] == 'arriba':
                        lista_calle_entrada.append(calle)
                elif int(cordenadas[1]) == int(dimension[1]):
                    if lista[2] == 'derecha':
                        lista_calle_salida.append(calle)
                    elif lista[2] == 'izquierda':
                        lista_calle_entrada.append(calle)
            elif lista[1] == 'casa':
                grilla_simulacion.agregar_casa(cordenadas_bien[0], cordenadas_bien[1])
                ladrones = [int(lista[4][1:3]), int(lista[5][0:2])]
                casa = Casa(lista[3], ladrones, cordenadas_bien)
                lista_casas.append(casa)
            elif lista[1] == 'vacio':
                lista_vacios.append(cordenadas_bien)
            linea1 = arch.readline().strip()
            if linea1 == '':
                principio = False
    esquinas = encontrar_esquinas(mapa_calles, lista_calle_salida)
    return lista_casas, mapa_calles, lista_vacios, lista_calle_entrada, lista_calle_salida, grilla_simulacion, esquinas


def cantidad_calles_lista(mapa):
    contador = 0
    lista_calles = []
    for i in mapa:
        for j in i:
            if j != '':
                contador += 1
                lista_calles.append(j)
    return contador, lista_calles


def encontrar_esquinas(mapa, listas_salidas):
    esquinas = []
    for i in range(len(mapa)):
        for n in range(len(mapa[0])):
            if mapa[i][n] != '':
                if mapa[i][n].direccion == 'abajo':
                    if mapa[i][n] in listas_salidas:
                        pass
                    elif mapa[i + 1][n] != '':
                        if mapa[i + 1][n].direccion != 'abajo':
                            esquinas.append(mapa[i + 1][n])
                            if mapa[i + 1][n] in listas_salidas:
                                pass
                            elif mapa[i + 2][n] != '':
                                if mapa[i + 2][n] != 'abajo':
                                    esquinas.append(mapa[i + 2][n])
                    if i - 1 < 0:
                        pass
                    elif mapa[i - 1][n] != '':
                        if mapa[i - 1][n].direccion != 'abajo':
                            esquinas.append(mapa[i - 1][n])
                            if i - 2 < 0:
                                pass
                            elif mapa[i - 2][n] != '':
                                if mapa[i - 2][n].direccion != 'abajo':
                                    esquinas.append(mapa[i - 2][n])
                elif mapa[i][n].direccion == 'arriba':
                    if mapa[i][n] in listas_salidas:
                        pass
                    elif mapa[i - 1][n] != '':
                        if mapa[i - 1][n].direccion != 'arriba':
                            esquinas.append(mapa[i - 1][n])
                            if mapa[i - 1][n] in listas_salidas:
                                pass
                            elif mapa[i - 2][n] != '':
                                if mapa[i - 2][n].direccion != 'arriba':
                                    esquinas.append(mapa[i - 2][n])
                    if i + 1 > len(mapa):
                        pass
                    elif mapa[i + 1][n] != '':
                        if mapa[i + 1][n].direccion != 'arriba':
                            esquinas.append(mapa[i + 1][n])
                            if i + 2 > len(mapa):
                                pass
                            elif mapa[i + 2][n] != '':
                                if mapa[i + 2][n] != 'arriba':
                                    esquinas.append(mapa[i + 2][n])
                elif mapa[i][n].direccion == 'derecha':
                    if mapa[i][n] in listas_salidas:
                        pass
                    elif mapa[i][n + 1] != '':
                        if mapa[i][n + 1].direccion != 'derecha':
                            esquinas.append(mapa[i][n + 1])
                            if mapa[i][n + 1] in listas_salidas:
                                pass
                            elif mapa[i][n + 2] != '':
                                if mapa[i][n + 2].direccion != 'derecha':
                                    esquinas.append(mapa[i][n + 2])
                    if n - 1 < 0:
                        pass
                    elif mapa[i][n - 1] != '':
                        if mapa[i][n - 1].direccion != 'derecha':
                            esquinas.append(mapa[i][n - 1])
                            if n - 2 < 0:
                                pass
                            elif mapa[i][n - 2] != '':
                                if mapa[i][n - 2].direccion != 'derecha':
                                    esquinas.append(mapa[i][n - 2])
                elif mapa[i][n].direccion == 'izquierda':
                    if mapa[i][n] in listas_salidas:
                        pass
                    elif mapa[i][n - 1] != '':
                        if mapa[i][n - 1].direccion != 'izquierda':
                            esquinas.append(mapa[i][n - 1])
                            if mapa[i][n - 1] in listas_salidas:
                                pass
                            elif mapa[i][n - 2] != '':
                                if mapa[i][n - 2].direccion != 'izquierda':
                                    esquinas.append(mapa[i][n - 2])
                    if n + 1 > len(mapa[0]):
                        pass
                    elif mapa[i][n + 1] != '':
                        if mapa[i][n + 1].direccion != 'izquierda':
                            esquinas.append(mapa[i][n + 1])
                            if n + 2 > len(mapa[0]):
                                pass
                            elif mapa[i][n + 2] != '':
                                if mapa[i][n + 2].direccion != 'izquierda':
                                    esquinas.append(mapa[i][n + 2])
    return esquinas
