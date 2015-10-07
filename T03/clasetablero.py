__author__ = 'JuanFrancisco'


class Tablero:
    def __init__(self, filas, columnas):
        lista = []
        lista2 = []
        lista3 = []
        for i in range(filas):
            lista.append([''] * columnas)
            lista2.append([''] * columnas)
            lista3.append([''] * columnas)
        self.agua = lista
        self.aire = lista2
        self.radar_acumulado = lista3
        self.lista_radar = []

    def agregar_radar(self, danadas, destruidas):
        lista = []
        for i in range(len(self.agua)):
            lista.append([''] * len(self.agua[0]))
        try:
            for i, n, j, z in danadas:
                self.radar_acumulado[i][n] = [j, z]
                lista[i][n] = [j, z]
        except TypeError:
            self.radar_acumulado[danadas[0]][danadas[1]] = [danadas[2], danadas[3]]
            lista[danadas[0]][danadas[1]] = [danadas[2], danadas[3]]
        for i in destruidas:
            for n in range(len(lista)):
                for z in range(len(lista[0])):
                    try:
                        if i == lista[n][z][0]:
                            lista[n][z] = ''
                            self.radar_acumulado[n][z] = ''
                    except IndexError:
                        pass
        self.lista_radar.append(lista)

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

    def verificar_destruidos(self):
        for i in range(len(self.agua)):
            for n in range(len(self.agua[0])):
                if self.agua[i][n]!='':
                    if self.agua[i][n].activo is False:
                        self.agua[i][n]=''

    def mostrar_radar(self, numero, embarcaciones):
        if numero == -1:
            mapa = self.radar_acumulado
            print('  Radar acumulado  ')
        else:
            mapa = self.lista_radar[numero]
            print('  Radar ataque {}'.format(numero + 1))
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
                    for z in range(len(embarcaciones.vehiculos)):
                        try:
                            if embarcaciones.vehiculos[z] == j[0] and j[1] == 1:
                                j = str(z + 1)
                            elif j[1] == 0:
                                j = 'x'
                        except IndexError:
                            pass
                r += j + ' '
            print(r)

    def ataque(self, arma, vehiculos_atacados, vehiculos_atacantes, tablero_atacante, turno):
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
            danadas = []
            destruidas = []
            if lugar == 1:
                for i in range(len(mapa[0])):
                    if mapa[fila][i] != '':
                        algo = [fila, i, mapa[fila][i], 0]
                        danadas.append(algo)
                        destruido = mapa[fila][i].recibir_dano(arma)
                        if destruido is True:
                            destruidas.append(mapa[fila][i])
                            print('Barco {} destruido '.format(mapa[fila][i].pieza))
                            self.mostrar_cordenadas(mapa, mapa[fila][i])
                print('Casillas que dieron con algun blanco: {}'.format(len(danadas)))
            elif lugar == 2:
                for i in range(len(mapa)):
                    if mapa[i][columna] != '':
                        algo= [i, columna, mapa[i][columna], 0]
                        danadas.append(algo)
                        destruido = mapa[i][columna].recibir_dano(arma)
                        if destruido is True:
                            destruidas.append(mapa[i][columna])
                            print('Barco {} destruido '.format(mapa[i][columna].pieza))
                            self.mostrar_cordenadas(mapa, mapa[i][columna])
                print('Casillas que dieron con algun blanco: {}'.format(len(danadas)))
            tablero_atacante.agregar_radar(danadas, destruidas)
            if len(danadas) > 0:
                vehiculos_atacantes.ataque_excitoso(danadas, arma)
                return True
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
                if mapa[fila][columna] == vehiculos_atacados.vehiculos[4] and mapa[fila - 1][columna] == \
                        vehiculos_atacados.vehiculos[4]:
                    print('Ataque fue un excito')
                    vehiculos_atacados.vehiculos[4].habilitado = turno
                    vehiculos_atacados.vehiculos[4].activo = False
                    vehiculos_atacantes.ataque_excitoso([1], arma)
                    return True
            elif lugar == 2:
                if fila + 1 > len(mapa):
                    return False
                if mapa[fila][columna] == vehiculos_atacados.vehiculos[4] and mapa[fila + 1][columna] == \
                        vehiculos_atacados.vehiculos[4]:
                    print('Ataque fue un excito')
                    vehiculos_atacados.vehiculos[4].habilitado = turno
                    vehiculos_atacados.vehiculos[4].activo = False
                    vehiculos_atacantes.ataque_excitoso([1], arma)
                    return True
            elif lugar == 3:
                if columna - 1 < 0:
                    return False
                if mapa[fila][columna - 1] == vehiculos_atacados.vehiculos[4] and mapa[fila][columna] == \
                        vehiculos_atacados.vehiculos[4]:
                    print('Ataque fue un excito')
                    vehiculos_atacados.vehiculos[4].habilitado = turno
                    vehiculos_atacados.vehiculos[4].activo = False
                    vehiculos_atacantes.ataque_excitoso([1], arma)
                    return True
            elif lugar == 4:
                if columna + 1 > len(mapa):
                    return False
                if mapa[fila][columna + 1] == vehiculos_atacados.vehiculos[4] and mapa[fila][columna] == \
                        vehiculos_atacados.vehiculos[4]:
                    print('Ataque fue un excito')
                    vehiculos_atacados.vehiculos[4].habilitado = turno
                    vehiculos_atacados.vehiculos[4].activo = False
                    vehiculos_atacantes.ataque_excitoso([1], arma)
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
            descubiertas = []
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
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
                    elif lugar2 == 2:
                        for i in range(fila - 3, fila):
                            for n in range(columna, columna + 3):
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
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
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna, columna + 3):
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
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
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna - 3, columna):
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
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
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
                    elif lugar2 == 2:
                        for i in range(fila, fila + 3):
                            for n in range(columna, columna + 3):
                                try:
                                    print(mapa[i][n].pieza, (i, n))
                                    vista = [i, n, mapa[i][n], 1]
                                    descubiertas.append(vista)
                                except AttributeError:
                                    pass
            tablero_atacante.agregar_radar(descubiertas, [])
            if len(descubiertas) > 0:
                vehiculos_atacantes.ataque_excitoso([1], arma)
        else:
            try:
                resultado = False
                descubiertas = [fila, columna, mapa[fila][columna], 0]
                if arma.sobrenombre == 'Trident II':
                    resultado = mapa[fila][columna].recibir_dano(arma)
                elif arma.sobrenombre == 'Minuteman III':
                    resultado = mapa[fila][columna].recibir_dano(arma)
                elif arma.sobrenombre == 'Kamikaze':
                    resultado = mapa[fila][columna].recibir_dano(arma)
                    vehiculos_atacantes.vehiculos[5].activo = False
                print('1 Barco alcanzado en las cordenadas {},{}'.format(chr(fila + 65), str(columna + 1)))
                destruidas = []
                if resultado is True:
                    print('Barco {} destruido '.format(mapa[fila][columna].pieza))
                    self.mostrar_cordenadas(mapa, mapa[fila][columna])
                    destruidas.append(mapa[fila][columna])
                tablero_atacante.agregar_radar(descubiertas, destruidas)
                vehiculos_atacantes.ataque_excitoso([1], arma)
                return True
            except AttributeError:
                print('0 Barcos alcanzados')
                tablero_atacante.agregar_radar([], [])

    def ataque_computador(self, tablero_atacante, vehiculos_robot, vehiculos_jugador):
        mapa = tablero_atacante.radar_acumulado
        posibles_lugares = []
        for i in range(len(mapa)):
            for n in range(len(mapa[0])):
                if mapa[i][n] != '':
                    a = [i, n]
                    posibles_lugares.append(a)
        pass

    def mostrar_cordenadas(self, aire_o_agua, barco):
        mapa = aire_o_agua
        r = ''
        for i in range(len(mapa)):
            for n in range(len(mapa[0])):
                if mapa[i][n] == barco:
                    r += ' (' + str(chr(i + 65)) + ',' + str(n + 1) + ') '
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
            barco = ''
            c = True
            while c is True:
                try:
                    a = int(input())
                    barco = naves.vehiculos[a - 1]
                    if a - 1 < 0:
                        print('Ingrese numero dentro del rango')
                        c = True
                    else:
                        c = False
                except ValueError:
                    print('Ingrese un numero no letras')
                except IndexError:
                    print('Ingrese numero dentro del rango')
            if barco.activo is True:
                barco.reparar()
                print('Barco raparado')
                return True
            else:
                print('Barco no reparable')

    def lugares(self, filas, columnas, mapa, fila, columna):
        libre = True
        if filas < 0 or columnas < 0 or len(mapa) < fila or len(mapa[0]) < columna:
            print('Fuera de rango del mapa')
            return False
        for z in range(filas, fila):
            for n in range(columnas, columna):
                if mapa[z][n] != '':
                    libre = False
        return libre

    def inputs_cordenadas(self, mapas):
        mapa = mapas
        d = True
        fila = -1
        while d is True:
            try:
                fila = str(input('Ingrese la fila: '))
                fila = ord(fila.upper()) - 65
                if fila < 0 or fila > len(mapa) - 1:
                    print('Ingrese una letra correspondiente')
                else:
                    d = False
            except SyntaxError:
                print('Ingrese un letra correspondiente')
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
                                    mapa[fila + n][columna - z] = a
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
                        libre2 = self.lugares(fila - a.area[1] + 1, columna, mapa, fila, columna + a.area[0])
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
                    self.mostrar_tablero(self.agua, vehi)
                    vehi.mostrar_vehiculos(False)
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = self.agregar_barcos(self.agua, a)
                    if b is not True:
                        b = False
                        print('Barco no puede ponerse en estos cuadrantes')
                else:
                    self.mostrar_tablero(agua_o_tierra=self.aire, embarcaciones=vehi)
                    vehi.mostrar_vehiculos(True)
                    print('El {} es de dimensiones {} x {}\nIngrese un cordenada'.format(a.pieza, a.area[0], a.area[1]))
                    b = self.agregar_barcos(self.aire, a)
                    if b is not True:
                        b = False
                        print('Avion no puede ponerse en estos cuadrantes')
            print('{} Ingresado correctamente'.format(a.pieza))
        print('Termino exitosamente de posicionar los vehiculos\n')
        self.mostrar_tablero(self.agua, vehi)
        self.mostrar_tablero(agua_o_tierra=self.aire, embarcaciones=vehi)
        vehi.mostrar_vehiculos('Todos')
