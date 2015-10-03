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
        self.habilitado = 0

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
    def __init__(self, nombre):
        self.vehiculos = []
        self.nombre_jugador = nombre

    def crear(self):
        todas_armas = [['Misil UGM-133 Trident II', 'Trident II', 5, [1, 1], 'Siempre'],
                       ['Misil de crucero BGM-109 Tomahawk', 'Tomahawk', 3, [1, 'n'], 3],
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
                elif a.barco is False:
                    r += ' [Deshabilitado] ' + str(a.habilitado)
                else:
                    r += ' [Destruido]'
            elif avion is True:
                if a.barco is False and a.activo is True:
                    r += ' [Activo] Ataques Disponibles: ' + b
                elif a.barco is True:
                    r = ''
                else:
                    r += ' [Deshabilitado] ' + str(a.habilitado)
            else:
                if a.barco is True and a.activo is True and (avion == 'Todos' or avion is False):
                    r += ': Vida ' + str(a.resistencia) + ' [Activo] Ataques Disponibles: ' + b
                elif a.activo is not True:
                    r += ' [Destruido]'
                else:
                    r = ''
            if r != '':
                print(r)


class Tablero:
    def __init__(self, filas, columnas):
        lista = []
        lista2 = []
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

    def ataque(self, arma, vehiculos_atacados,vehiculos_atacantes):
        area = arma.area
        if arma.sobrenombre == 'Paralizer':
            mapa = self.aire
        else:
            mapa = self.agua
        print('\nEl ataque {} es de area {} x {}, ingrese una cordenada'.format(arma.sobrenombre, area[0], area[1]))
        fila, columna = self.inputs_cordenadas(mapa)
        if arma.sobrenombre == 'Tomahawk':
            c = True
            lugar = 0
            while c is True:
                try:
                    lugar = int(input('Ingrese direccion del ataque:\n[1] Horizontal\n'
                                      '[2] Vertical\t'))
                    if 0 < lugar <= 2:
                        c = False
                    if c is True:
                        print('Ingrese direccion dentro del rango de opciones')
                except ValueError:
                    print('Ingrese un numero no letras')
                    c = True
            if lugar == 1:
                danadas = 0
                for i in range(len(mapa[0])):
                    if mapa[fila][i] != '':
                        danadas += 1
                        destruido = mapa[fila][i].recibir_dano(arma)
                        if destruido is True:
                            print('Barco {} destruido '.format(mapa[fila][i].pieza))
                            self.mostrar_cordenadas(mapa, mapa[fila][i])
                print('Casillas que dieron con algun blanco: {}'.format(danadas))
            elif lugar == 2:
                danadas = 0
                for i in range(len(mapa)):
                    if mapa[i][columna] != '':
                        danadas += 1
                        destruido = mapa[i][columna].recibir_dano(arma)
                        if destruido is True:
                            print('Barco {} destruido ')
                            self.mostrar_cordenadas(mapa, mapa[i][columna])
                print('Casillas que dieron con algun blanco: {}'.format(danadas))
        elif arma.sobrenombre == 'Paralizer':
            c = True
            lugar = 0
            while c is True:
                try:
                    lugar = int(input('Ingrese direccion de largo de la siguiente cordenada:\n[1] Arriba\n'
                                      '[2] Abajo\n[3] Izquierda\n[4] Derecha\t'))
                    if 0 < lugar <= 4:
                        c = False
                    if c is True:
                        print('Ingrese direccion dentro del rango de opciones')
                except ValueError:
                    print('Ingrese un numero no letras')
                    c = True
            if lugar == 1:
                if fila - 1 < 0:
                    return False
                if mapa[fila][columna] == vehiculos_atacados[4] and mapa[fila - 1][columna] == \
                        vehiculos_atacados[4]:
                    print('Ataque fue un excitoso')
                    vehiculos_atacados[4].habilitado = 5
                    vehiculos_atacados[4].activo = False
            elif lugar == 2:
                if fila + 1 > len(mapa):
                    return False
                if mapa[fila][columna] == vehiculos_atacados[4] and mapa[fila + 1][columna] == \
                        vehiculos_atacados[4]:
                    print('Ataque fue un excitoso')
                    vehiculos_atacados[4].habilitado = 5
                    vehiculos_atacados[4].activo = False
            elif lugar == 3:
                if columna - 1 < 0:
                    return False
                if mapa[fila][columna - 1] == vehiculos_atacados[4] and mapa[fila][columna] == \
                        vehiculos_atacados[4]:
                    print('Ataque fue un excitoso')
                    vehiculos_atacados[4].habilitado = 5
                    vehiculos_atacados[4].activo = False
            elif lugar == 4:
                if columna + 1 > len(mapa):
                    return False
                if mapa[fila][columna + 1] == vehiculos_atacados[4] and mapa[fila][columna] == \
                        vehiculos_atacados[4]:
                    print('Ataque fue un excitoso')
                    vehiculos_atacados[4].habilitado = 5
                    vehiculos_atacados[4].activo = False
            return True
        elif arma.sobrenombre == 'Explorar':
            c = True
            lugar = 0
            while c is True:
                try:
                    lugar = int(input('Ingrese direccion de largo de la siguiente cordenada:\n[1] Arriba\n'
                                      '[2] Abajo\n[3] Izquierda\n[4] Derecha\t'))
                    if 0 < lugar <= 4:
                        c = False
                    if c is True:
                        print('Ingrese direccion dentro del rango de opciones')
                except ValueError:
                    print('Ingrese un numero no letras')
                    c = True
            if lugar == 1:
                if fila - 1 < 0:
                    return False
                else:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Izquierda\n[2] Derecha\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        for i in range(fila - 3, fila):
                            for n in range(columna - 3, columna):
                                print(mapa[i][n].pieza, (i, n))
                    elif lugar2 == 2:
                        for i in range(fila - 3, fila):
                            for n in range(columna, columna + 3):
                                print(mapa[i][n].pieza, (i, n))
            elif lugar == 2:
                if fila + 1 > len(mapa):
                    return False
                else:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Izquierda\n[2] Derecha\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        for i in range(fila, fila + 3):
                            for n in range(columna - 3, columna):
                                print(mapa[i][n].pieza, (i, n))
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna, columna + 3):
                                print(mapa[i][n].pieza, (i, n))
            elif lugar == 3:
                if columna - 1 < 0:
                    return False
                else:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Arriba\n[2] Abajo\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        for i in range(fila - 3, fila):
                            for n in range(columna - 3, columna):
                                print(mapa[i][n].pieza, (i, n))
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna - 3, columna):
                                print(mapa[i][n].pieza, (i, n))
            elif lugar == 4:
                if columna + 1 > len(mapa):
                    return False
                else:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Arriba\n[2] Abajo\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        for i in range(fila - 3, fila):
                            for n in range(columna, columna + 3):
                                print(mapa[i][n].pieza, (i, n))
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna, columna + 3):
                                print(mapa[i][n].pieza, (i, n))
        else:
            try:
                resultado=False
                if arma.sobrenombre == 'Trident II':
                    resultado=mapa[fila][columna].recibir_dano(arma)
                elif arma.sobrenombre=='Minuteman III':
                    resultado=mapa[fila][columna].recibir_dano(arma)
                elif arma.sobrenombre=='Kamikaze':
                    resultado=mapa[fila][columna].recibir_dano(arma)
                    vehiculos_atacantes[5].activo=False
                if resultado is True:
                    print('Barco {} destruido '.format(mapa[fila][columna].pieza))
                    self.mostrar_cordenadas(mapa, mapa[fila][columna])
            except AttributeError:
                print('0 Barcos alcanzados')
                                # importa el orden hacer excepcion para el puerto

    def mostrar_cordenadas(self, aire_o_agua, barco):
        mapa = aire_o_agua
        r = ''
        for i in range(len(mapa)):
            for n in range(len(mapa[0])):
                if mapa[i][n] == barco:
                    r += ', (' + str(chr(i + 65)) + ',' + str(n + 1) + ') '
        print('Cordenadas del barco destruido:')
        print(r)

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
            naves.mostrar_vehiculos('Todos')
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

    def lugares(self, filas, columnas, mapa, fila, columna):
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

    def inputs_cordenadas(self, mapas):
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
                if 0 <= columna < len(mapa[0]):
                    c = False
                if c is True:
                    print('Ingrese columna dentro del rango')
            except ValueError:
                print('Ingrese un numero no letras')
                c = True
        return fila, columna

    def agregar_barcos(self, mapas, barco):
        a = barco
        mapa = mapas
        fila, columna = self.inputs_cordenadas(mapa)
        if a.area == [1, 1]:
            if mapa[fila][columna] == '':
                mapa[fila][columna] = a
                return True
            else:
                return False
        elif mapa[fila][columna] == '':
            c = True
            lugar = 0
            while c is True:
                try:
                    lugar = int(input('Ingrese direccion de largo de la siguiente cordenada:\n[1] Arriba\n'
                                      '[2] Abajo\n[3] Izquierda\n[4] Derecha\t'))
                    if 0 < lugar <= 4:
                        c = False
                    if c is True:
                        print('Ingrese direccion dentro del rango de opciones')
                except ValueError:
                    print('Ingrese un numero no letras')
                    c = True
            if lugar == 1:
                libre = self.lugares(fila - a.area[0] + 1, columna, mapa, fila + 1, columna + 1)
                if libre is False:
                    return False
                elif a.area[1] >= 2:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Izquierda\n[2] Derecha\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        libre2 = self.lugares(fila - a.area[0], columna - a.area[1], mapa, fila + 1, columna + 1)
                        if libre2 is True:
                            for z in range(a.area[1]):
                                for n in range(a.area[0]):
                                    mapa[fila - n][columna - z] = a
                            return True
                    elif lugar2 == 2:
                        libre2 = self.lugares(fila - a.area[0] + 1, columna, mapa, fila + 1, columna + a.area[1])
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
                libre = self.lugares(fila, columna, mapa, fila + a.area[0], columna + 1)
                if libre is False:
                    return False
                if a.area[1] >= 2:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Izquierda\n[2] Derecha\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        libre2 = self.lugares(fila, columna - a.area[1], mapa, fila + a.area[0], columna + 1)
                        if libre2 is True:
                            for z in range(a.area[1]):
                                for n in range(a.area[0]):
                                    mapa[fila + n][columna - z] = a
                            return True
                    elif lugar2 == 2:
                        libre2 = self.lugares(fila, columna, mapa, fila + a.area[0], columna + a.area[1])
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
                libre = self.lugares(fila, columna - a.area[0] + 1, mapa, fila + 1, columna + 1)
                if libre is False:
                    return False
                if a.area[1] >= 2:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Arriba\n[2] Abajo\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        libre2 = self.lugares(fila - a.area[1] + 1, columna - a.area[0] + 1, mapa, fila + 1,
                                              columna + 1)
                        if libre2 is True:
                            for z in range(a.area[0]):
                                for n in range(a.area[1]):
                                    mapa[fila - n][columna - z] = a
                            return True
                    elif lugar2 == 2:
                        libre2 = self.lugares(fila, columna - a.area[0] + 1, mapa, fila + a.area[1], columna + 1)
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
                libre = self.lugares(fila, columna, mapa, fila + 1, columna + a.area[0])
                if libre is False:
                    return False
                if a.area[1] >= 2:
                    c = True
                    lugar2 = 0
                    while c is True:
                        try:
                            lugar2 = int(input('Ingrese direccion de ancho de la siguiente cordenada:\n'
                                               '[1] Arriba\n[2] Abajo\t'))
                            if 0 < lugar2 <= 2:
                                c = False
                            if c is True:
                                print('Ingrese direccion dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero no letras')
                            c = True
                    if lugar2 == 1:
                        libre2 = self.lugares(fila - a.area[1], columna, mapa, fila + 1, columna + a.area[0])
                        if libre2 is True:
                            for z in range(a.area[0]):
                                for n in range(a.area[1]):
                                    mapa[fila - n][columna + z] = a
                            return True
                    elif lugar2 == 2:
                        libre2 = self.lugares(fila, columna, mapa, fila + a.area[1], columna + a.area[0])
                        if libre2 is True:
                            for z in range(a.area[0]):
                                for n in range(a.area[1]):
                                    mapa[fila + n][columna + z] = a
                            return True
                elif libre is True:
                    for z in range(a.area[0]):
                        mapa[fila][columna + z] = a
                    return True

    def agregar_vehiculo(self, vehi):
        naves = vehi.vehiculos
        for i in range(len(naves)):
            b = False
            a = naves[i]
            while b is False:
                a = naves[i]
                if a.barco is True:
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = self.agregar_barcos(self.agua, a)
                    self.mostrar_tablero(self.agua, vehi)
                    vehi.mostrar_vehiculos(False)
                    if b is not True:
                        b = False
                        print('Barco no puede ponerse en estos cuadrantes')
                else:
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = self.agregar_barcos(self.aire, a)
                    self.mostrar_tablero(agua_o_tierra=self.aire, embarcaciones=vehi)
                    vehi.mostrar_vehiculos(True)
                    if b is not True:
                        b = False
                        print('Avion no puede ponerse en estos cuadrantes')
            print('{} Ingresado correctamente'.format(a.pieza))
        print('Termino excitosamente de pocisionar los vehiculos\n')


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

    def correr(self, jugador1, tablero1, jugador2, tablero2):
        vehi = jugador1
        table = tablero1
        vehi2 = jugador2
        tablero2 = tablero2
        table.mostrar_tablero(table.agua, vehi)
        # table.mejorar(vehi)
        menu1 = 0
        while menu1 != 3:
            Menu().mostrar(1)
            c = True
            f = True
            while f is True:
                while c is True:
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
                    orden = []
                    b = True
                    ataque = -1
                    while b is True:
                        try:
                            print('Seleccione ataque a ocupar:')
                            orden = elegido.mostrar_ataques()
                            ataque = int(input())
                            if 0 < ataque <= len(orden):
                                b = False
                            else:
                                print('Fuera de rango de opciones')
                        except ValueError:
                            print('Ingrese un numero de la lista no letras')
                            b = True
                    opcion = orden[ataque - 1][1]
                    if elegido.ataques[opcion].sobrenombre == 'Kit de Ingenieros':
                        resultado = table.mejorar(vehi)
                        if resultado is True:
                            f = False
                    elif elegido.ataques[opcion].sobrenombre == 'Napalm':
                        mapa=tablero2.agua
                        fila, columna = tablero2.inputs_cordenadas(mapa)
                        resultado=mapa[fila][columna].recibir_dano(elegido.ataques[opcion])
                        if resultado is True:
                            print('Barco {} destruido '.format(mapa[fila][columna].pieza))
                            tablero2.mostrar_cordenadas(mapa, mapa[fila][columna])
                        f=False
                    else:
                        tablero2.ataque(elegido.ataques[opcion], vehi2,vehi)
                        f=False
                    algo = input()
                elif menu1 == 2:
                    pass
                elif menu1 == 3:
                    print('Jugador {} se a rendido'.format(vehi.nombre_jugador))
                    return True
            menu1 = 3


import random


def personavspersona():
    terminar = False
    nombre1 = input('Nombre jugador 1: ')
    vehi1 = CrearVehiculos(nombre1)
    vehi1.crear()
    table1 = Tablero(5, 6)
    nombre2 = input('Nombre jugador 2: ')
    vehi2 = CrearVehiculos(nombre2)
    vehi2.crear()
    table2 = Tablero(5, 6)
    numero = random.randint(1, 2)
    if numero == 1:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        # table1.agregar_vehiculo(vehi1)
        print('Turno jugador {} de poner sus vehiculos'.format(vehi2.nombre_jugador))
        # table2.agregar_vehiculo(vehi2)
        vehiculos = vehi1
        tablero = table1
        vehiculos2 = vehi2
        tablero2 = table2
        while terminar is False:
            print('Turno jugador {}: '.format(vehiculos.nombre_jugador))
            resultado = Menu().correr(vehiculos, tablero, vehiculos2, tablero2)
            if resultado == True:
                terminar = True
            elif vehiculos == vehi1:
                vehiculos = vehi2
                tablero = table2
                vehiculos2 = vehi1
                tablero2 = table1
            elif vehiculos == vehi2:
                vehiculos = vehi1
                tablero = table1
                vehiculos2 = vehi2
                tablero2 = table2
    else:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi2.nombre_jugador))
        # table2.agregar_vehiculo(vehi2)
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        # table1.agregar_vehiculo(vehi1)
        vehiculos = vehi2
        tablero = table2
        vehiculos2 = vehi1
        tablero2 = table1
        while terminar is False:
            print('Turno jugador {}: '.format(vehiculos.nombre_jugador))
            resultado = Menu().correr(vehiculos, tablero, vehiculos2, tablero2)
            if resultado == True:
                terminar = True
            elif vehiculos == vehi1:
                vehiculos = vehi2
                tablero = table2
                vehiculos2 = vehi1
                tablero2 = table1
            elif vehiculos == vehi2:
                vehiculos = vehi1
                tablero = table1
                vehiculos2 = vehi2
                tablero2 = table2
    print('Fin del juego')


personavspersona()
# ver Lab 9 vuelo
