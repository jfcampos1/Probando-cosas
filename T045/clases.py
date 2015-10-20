__author__ = 'JuanFrancisco'
from random import uniform


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

    def simplifica_siguiente_calle(self, mapa, grilla, numero, x, y,auto):
        if numero == 1:
            if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)] != '':
                if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'arriba':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]-1, self.cordenadas[1] , 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]-1, self.cordenadas[1]]
                elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'abajo' or \
                                mapa[self.cordenadas[1]+1][self.cordenadas[0] + (1 * y)].direccion == 'abajo':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]+1, self.cordenadas[1] , 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]+1, self.cordenadas[1]]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]-1, self.cordenadas[1], 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]-1, self.cordenadas[1]]
            elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)] != '':
                if mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'arriba':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]-1, self.cordenadas[1] , 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]-1, self.cordenadas[1]]
                elif mapa[self.cordenadas[1]][self.cordenadas[0] + (1 * y)].direccion == 'abajo':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]+1, self.cordenadas[1] , 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]+1, self.cordenadas[1]]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0]+1, self.cordenadas[1] , 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0]+1, self.cordenadas[1]]
        elif numero == 2:
            if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)] != '':
                if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'derecha':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0] , self.cordenadas[1]+1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]+1]
                elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0] + (1 * y)].direccion == 'izquierda':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0] , self.cordenadas[1]-1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]-1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0] , self.cordenadas[1]-1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]-1]
            elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]] != '':
                if mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]].direccion == 'derecha':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0] , self.cordenadas[1]+1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]+1]
                elif mapa[self.cordenadas[1] + (1 * x)][self.cordenadas[0]].direccion == 'izquierda':
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0] , self.cordenadas[1]-1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]-1]
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0], self.cordenadas[1]+1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]+1]

    def siguiente_calle(self, mapa, lista_salida, grilla, auto):
        if self.direccion == 'izquierda':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 2] == '':
                self.simplifica_siguiente_calle(mapa, grilla, 1, -2, -1,auto)
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_auto(self.cordenadas[0], self.cordenadas[1]-1, 0, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]-1]
        elif self.direccion == 'derecha':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif self.cordenadas[1]<=len(mapa[0])or self.cordenadas[0]<=len(mapa) :
                if mapa[self.cordenadas[0] - 1][self.cordenadas[1]] == '':
                    self.simplifica_siguiente_calle(mapa, grilla, 1, -2, -1)
                else:
                    grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                    grilla.agregar_auto(self.cordenadas[0], self.cordenadas[1]+1, 0, False)
                    auto.cordenadas_vehiculo = [self.cordenadas[0], self.cordenadas[1]+1]
        elif self.direccion == 'arriba':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0] - 2][self.cordenadas[1] - 1] == '':
                self.simplifica_siguiente_calle(mapa, grilla, 2, -1, -2)
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_auto(self.cordenadas[0]-1, self.cordenadas[1], 0, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0]-1, self.cordenadas[1]]
        elif self.direccion == 'abajo':
            if mapa[self.cordenadas[0] - 1][self.cordenadas[1] - 1] in lista_salida:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                del auto
            elif mapa[self.cordenadas[0]][self.cordenadas[1] - 1] == '':
                self.simplifica_siguiente_calle(mapa, grilla, 2, -1, -2)
            else:
                grilla.quitar_imagen(self.cordenadas[0], self.cordenadas[1])
                grilla.agregar_auto(self.cordenadas[0]+1, self.cordenadas[1], 90, False)
                auto.cordenadas_vehiculo = [self.cordenadas[0]+1, self.cordenadas[1]]


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
    cantidad_autos=[]

    def __init__(self, tipo, tiempo_llegada, cordenadas):
        self.tipo = tipo
        self.tipo_vehiculo = Vehiculo.tipo_auto[tipo]
        self.tiempo_llegada = tiempo_llegada
        self.velocidad = uniform(0.5, 1)
        self.cordenadas_vehiculo = cordenadas

    def __repr__(self):
        return 'Tipo vehiculo: {0}'.format(self.tipo_vehiculo)
