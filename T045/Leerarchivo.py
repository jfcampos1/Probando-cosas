__author__ = 'JuanFrancisco'

from clases import Calle, Casa
from gui.gui import GrillaSimulacion

def nuevo_mapa(app):
    with open('mapa fix.txt', 'r', encoding='utf8') as arch:
        dimension=arch.readline().strip()
        dimension=dimension.split('x')
        grilla_simulacion = GrillaSimulacion(app,rows=int(dimension[0]),cols=(int(dimension[1])+1))
        linea1 = arch.readline().strip()
        lista_vacios = []
        lista_casas = []
        lista_calle_entrada = []
        lista_calle_salida = []
        principio = True
        mapa_calles = []
        for i in range(int(dimension[0])):
            mapa_calles.append([''] * (int(dimension[1])+1))
        while principio is True:
            lista = linea1.split(' ')
            cordenadas = lista[0].split(',')
            cordenadas_bien = [int(cordenadas[0])+1, int(cordenadas[1])+1]
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
                elif int(cordenadas[0]) == 19:
                    if lista[2] == 'abajo':
                        lista_calle_salida.append(calle)
                    elif lista[2] == 'arriba':
                        lista_calle_entrada.append(calle)
                elif int(cordenadas[1]) == 19:
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
        grilla_simulacion.show()
        grilla_simulacion.actualizar()
        return lista_casas, mapa_calles, lista_vacios, lista_calle_entrada, lista_calle_salida,grilla_simulacion
