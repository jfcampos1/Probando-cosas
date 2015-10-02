__author__ = 'JuanFrancisco'


class Armas:
    def __init__(self, lista):
        self.nombre = lista[0]
        self.sobrenombre = lista[1]
        self.dano = lista[2]
        self.area = lista[3]
        self.disponibilidad = lista[4]
        self.inutil = False


class Vehiculo:
    def __init__(self, pieza, agua, area_ocu, resistencia, Ataques):
        self.pieza = pieza
        self.area = area_ocu
        self.resistencia = resistencia
        self.max_resistencia = resistencia
        self.ataques = Ataques
        self.barco = agua
        self.activo = True

    def recibir_dano(self, arma):
        self.resistencia -= arma.dano
        if self.resistencia <= 0:
            self.activo = False
            return True
        return False

    def reparar(self):
        if self.resistencia < self.max_resistencia:
            self.resistencia += 1
            return True
        else:
            print('No puedes exceder el max de resistencia')
            return False

    def mostrar_ataques(self):
        orden = []
        a = 1
        for i in range(len(self.ataques)):
            if self.ataques[i].inutil != True:
                r = '[' + str(a) + '] ' + self.ataques[i].nombre
                print(r)
                orden2 = [a, i]
                orden.append(orden2)
                a += 1
        return orden


class CrearVehiculos:
    def __init__(self):
        self.vehiculos = []

    def crear(self):
        todas_armas = [['Misil UGM-133 Trident II', 'Trident II', 5, [1, 1], 'Siempre'],
                       ['Misil de crucero BGM-109 Tomahawk', 'Tomahawk', 3, 'linea', 3],
                       ['Napalm', 'Napalm', 5, [1, 1], 8],
                       ['Misil Balistico Intercontinental Minuteman III', 'Minuteman III', 15, [1, 1], 3],
                       ['Kamikaze', 'Kamikaze', 10000, [1, 1], 1],
                       ['Kit de Ingenieros', 'Kit de Ingenieros', 0, [1], 2],
                       ['GBU-43/B Massive Ordnance Air Blast Paralizer', 'Paralizer', 'Stop', [1, 1], 'Siempre'],
                       ['Explorar', 'Explorar', 0, [3, 3], 'Siempre']]
        a = Vehiculo('Barco Pequeno', True, [3, 1], 30, [Armas(todas_armas[0]), Armas(todas_armas[3]),
                                                         Armas(todas_armas[6])])
        b = Vehiculo('Buque de Guerra', True, [3, 2], 60, [Armas(todas_armas[0]), Armas(todas_armas[1]),
                                                           Armas(todas_armas[6])])
        c = Vehiculo('Lancha', True, [2, 1], 1, [Armas(todas_armas[6])])
        d = Vehiculo('Puerto', True, [4, 2], 80, [Armas(todas_armas[0]), Armas(todas_armas[5]), Armas(todas_armas[6])])
        e = Vehiculo('Avion explorador', False, [2, 2], None, [Armas(todas_armas[7])])
        f = Vehiculo('Kamikaze IXXI', False, [1, 1], None, [Armas(todas_armas[4])])
        g = Vehiculo('Avion Caza', False, [1, 1], None, [Armas(todas_armas[2])])
        listita = [a, b, c, d, e, f, g]
        self.vehiculos += listita

    def mostrar_vehiculos(self, avion):
        for i in range(len(self.vehiculos)):
            r = ''
            a = self.vehiculos[i]
            r = '[' + str(i + 1) + '] ' + a.pieza
            b = ''
            for n in range(len(a.ataques)):
                if a.ataques[n].inutil is not True:
                    b += a.ataques[n].sobrenombre + '   '
            if avion == 'Todos':
                if a.barco is True and a.activo is True:
                    r += ': Vida ' + str(a.resistencia) + ' [Activo] Ataques Disponibles: ' + b
                elif a.activo is True:
                    r += ' [Activo] Ataques Disponibles: ' + b
                else:
                    r += ' [Destruido]'
                print(r)
            elif avion is True:
                if a.barco is False and a.activo is True:
                    r += ' [Activo] Ataques Disponibles: ' + b
                elif a.barco is True:
                    r=''
                else:
                    r += ' [Destruido]'
                print(r)
            else:
                if a.barco is True and a.activo is True and (avion == 'Todos' or avion is False):
                    r += ': Vida ' + str(a.resistencia) + ' [Activo] Ataques Disponibles: ' + b
                elif a.activo is not True:
                    r += ' [Destruido]'
                else:
                    r=''
                print(r)



class Tablero:
    def __init__(self, filas, columnas):
        lista = []
        lista2=[]
        for i in range(filas):
            lista.append([''] * columnas)
            lista2.append([''] * columnas)
        self.agua = lista
        self.aire = lista2

    def mostrar_tablero(self, agua_o_tierra, embarcaciones):
        mapa = agua_o_tierra
        if mapa == self.agua:
            print('  Agua  ')
        else:
            print('  Cielo  ')
        r = ' '
        for i in range(len(mapa[0])):
            r += ' ' + str(i + 1)
        print(r)
        for i in range(len(mapa)):
            r = chr(65 + i) + ' '
            for j in mapa[i]:
                for z in range(len(embarcaciones.vehiculos)):
                    if j == '':
                        j = '0'
                    elif embarcaciones.vehiculos[z] == j:
                        j = str(z + 1)
                r += j + ' '
            print(r)

    def ataque(self, arma):
        area = arma.area
        self.mostrar_tablero(self.agua)
        print('\nEl ataque es de area {} x {}, ingrese una cordenada'.format(area[0], area[1]))
        cordenada_fila = input('Fila: ')
        cordenada_columna = input('Columna: ')

        # importa el orden hacer excepcion para el puerto

    def mejorar(self, naves):
        b = True
        while b is True:
            print('Seleccione Vehiculo a reparar:\n')
            resultado = False
            for i in range(len(naves.vehiculos)):
                try:
                    a = naves.vehiculos[i]
                    if a.resistencia < a.max_resistencia and a.barco is True:
                        resultado = True
                except TypeError:
                    pass
            naves.mostrar_vehiculos()
            if resultado is False:
                print('No tiene barcos que necesiten repararse')
                return False
            a = int(input())  # agregar try except por aca
            barco = naves.vehiculos[a - 1]
            if barco.activo is True:
                barco.reparar()
                b = False
                print('Barco raparado')
            else:
                print('Barco no reparable')

    def agregar_vehiculo(self, vehi):
        naves = vehi.vehiculos
        for i in range(len(naves)):
            b = False
            while b is False:
                a = naves[i]

                def lugares(filas, columnas, mapa, fila, columna):
                    libre = True
                    for z in range(filas, fila):
                        for n in range(columnas, columna):
                            if mapa[z][n] != '':
                                libre = False
                            print(z, n)
                    if filas < 0 or columnas < 0:
                        libre = False
                        print('Fuera de rango del mapa')
                    return libre

                def inputs(mapas):
                    mapa = mapas
                    d = True
                    fila = -1
                    while d is True:
                        fila = input('Ingrese la fila: ')
                        fila = ord(fila.upper()) - 65
                        if fila < 0 or fila > len(mapa) - 1:
                            print('Ingrese una letra correspondiente')

                        else:
                            d = False
                    c = True
                    columna = -1
                    while c is True:
                        try:
                            columna = int(input('Ingrese la columna: ')) - 1
                            if columna < len(mapa[0]):
                                c = False
                            if c is True:
                                print('Ingrese columna dentro del rango')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if mapa[fila][columna] == '':
                        lugar = int(input('Ingrese direccion de largo de la siguiente cordenada:\n[1] Arriba\n'
                                          '[2] Abajo\n[3] Izquierda\n[4] Derecha\t'))
                        if lugar == 1:
                            libre = lugares(fila - a.area[0] + 1, columna, mapa, fila + 1, columna + 1)
                            if libre is False:
                                return False
                            elif a.area[1] >= 2:
                                lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                                   '[1] Izquierda\n[2] Derecha\t'))
                                if lugar2 == 1:
                                    libre2 = lugares(fila - a.area[0], columna - a.area[1], mapa, fila + 1, columna + 1)
                                    if libre2 is True:
                                        for z in range(a.area[1]):
                                            for n in range(a.area[0]):
                                                mapa[fila - n][columna - z] = a
                                        return True
                                elif lugar2 == 2:
                                    libre2 = lugares(fila - a.area[0] + 1, columna, mapa, fila + 1, columna + a.area[1])
                                    if libre2 is True:
                                        for z in range(a.area[1]):
                                            for n in range(a.area[0]):
                                                mapa[fila - n][columna + z] = a
                                        return True
                            elif libre is True:
                                for z in range(a.area[0]):
                                    mapa[fila - z][columna] = a
                                return True
                        elif lugar == 2:
                            libre = lugares(fila, columna, mapa, fila + a.area[0], columna + 1)
                            if libre is False:
                                return False
                            if a.area[1] >= 2:
                                lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                                   '[1] Izquierda\n[2] Derecha\t'))
                                if lugar2 == 1:
                                    libre2 = lugares(fila, columna - a.area[1], mapa, fila + a.area[0], columna + 1)
                                    if libre2 is True:
                                        for z in range(a.area[1]):
                                            for n in range(a.area[0]):
                                                mapa[fila + n][columna - z] = a
                                        return True
                                elif lugar2 == 2:
                                    libre2 = lugares(fila, columna, mapa, fila + a.area[0], columna + a.area[1])
                                    if libre2 is True:
                                        for z in range(a.area[1]):
                                            for n in range(a.area[0]):
                                                mapa[fila + n][columna + z] = a
                                        return True
                            elif libre is True:
                                for z in range(a.area[0]):
                                    mapa[fila + z][columna] = a
                                return True
                        elif lugar == 3:
                            libre = lugares(fila, columna - a.area[0]+1, mapa, fila + 1, columna+1)
                            if libre is False:
                                return False
                            if a.area[1] >= 2:
                                lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                                   '[1] Arriba\n[2] Abajo\t'))
                                if lugar2 == 1:
                                    libre2 = lugares(fila - a.area[1]+1, columna - a.area[0]+1, mapa, fila + 1,
                                                     columna + 1)
                                    if libre2 is True:
                                        for z in range(a.area[0]):
                                            for n in range(a.area[1]):
                                                mapa[fila - n][columna - z] = a
                                        return True
                                elif lugar2 == 2:
                                    libre2 = lugares(fila, columna - a.area[0]+1, mapa, fila + a.area[1], columna + 1)
                                    if libre2 is True:
                                        for z in range(a.area[0]):
                                            for n in range(a.area[1]):
                                                mapa[fila - n][columna + z] = a
                                        return True
                            elif libre is True:
                                for z in range(a.area[0]):
                                    mapa[fila][columna - z] = a
                                return True
                        elif lugar == 4:
                            libre = lugares(fila, columna, mapa, fila + 1, columna + a.area[0])
                            if libre is False:
                                return False
                            if a.area[1] >= 2:
                                lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                                   '[1] Arriba\n[2] Abajo\t'))
                                if lugar2 == 1:
                                    libre2 = lugares(fila - a.area[1], columna, mapa, fila + 1, columna + a.area[0])
                                    if libre2 is True:
                                        for z in range(a.area[0]):
                                            for n in range(a.area[1]):
                                                mapa[fila - n][columna + z] = a
                                        return True
                                elif lugar2 == 2:
                                    libre2 = lugares(fila, columna, mapa, fila + a.area[1], columna + a.area[0])
                                    if libre2 is True:
                                        for z in range(a.area[0]):
                                            for n in range(a.area[1]):
                                                mapa[fila + n][columna + z] = a
                                        return True
                            elif libre is True:
                                for z in range(a.area[0]):
                                    mapa[fila][columna + z] = a
                                return True

                if a.barco is True:
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = inputs(self.agua)
                    self.mostrar_tablero(self.agua, vehi)
                    vehi.mostrar_vehiculos(False)
                    if b is not True:
                        b = False
                        print('Barco no puede ponerse en estos cuadrantes')
                else:
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = inputs(self.aire)
                    self.mostrar_tablero(agua_o_tierra=self.aire, embarcaciones=vehi)
                    vehi.mostrar_vehiculos(True)
                    if b is not True:
                        b = False
                        print('Avion no puede ponerse en estos cuadrantes')


# hacer preguntas de si arriba o abajo :D


class Menu:
    def __init__(self):
        self.menu = True

    def mostrar(self, numero):
        if numero == 1:
            print('[1] Atacar, mover o repararse\n[2] Mostrar radar\n[3] Rendirse')
        elif numero == 2:
            print('[1] Radar de Ataques\n[2] Radar de defensa\n[3] Salir de radar')
        elif numero == 3:
            pass
            # mostrar_tablero()

    def correr(self):
        vehi = CrearVehiculos()
        vehi.crear()
        table = Tablero(5, 6)
        table.mostrar_tablero(table.agua, vehi)
        table.agregar_vehiculo(vehi)
        # table.mejorar(vehi)
        menu1 = 0
        while menu1 != 3:
            Menu().mostrar(1)
            c = True
            while c == True:
                try:
                    menu1 = int(input('Seleccione accion a tomar:\t'))
                    c = False
                except ValueError:
                    print('Ingrese un numero de la lista no letras')
                    c = True
            if menu1 == 1:
                print('Seleccione Vehiculo a ocupar:')
                b = True
                vehi.mostrar_vehiculos('Todos')
                selec = 0
                while b == True:
                    try:
                        selec = int(input())
                        b = False
                    except ValueError:
                        print('Ingrese un numero de la lista no letras')
                        b = True
                elegido = vehi.vehiculos[selec - 1]
                print('Seleccione ataque a ocupar:')
                orden = elegido.mostrar_ataques()
                b = True
                ataque = -1
                while b is True:
                    try:
                        ataque = int(input())  # que este dentro del rango de opciones
                        b = False
                    except ValueError:
                        print('Ingrese un numero de la lista no letras')
                        b = True
                opcion = orden[ataque - 1][1]
                if elegido.ataques[opcion].sobrenombre == 'Kit de Ingenieros':  # Devolverse a elegir accion
                    resultado = table.mejorar(vehi)
                else:
                    print('aca')
                print(opcion)
                algo = input()
            elif menu1 == 2:
                pass


Menu().correr()
# ver Lab 9 vuelo
