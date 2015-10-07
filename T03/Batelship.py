__author__ = 'JuanFrancisco'


class Armas:
    def __init__(self, lista):
        self.nombre = lista[0]
        self.sobrenombre = lista[1]
        self.dano = lista[2]
        self.area = lista[3]
        self.disponibilidad = lista[4]
        self.turno_desactivado = None
        self.inutil = False
        self.cordenadas_napalm = []


class Vehiculo:
    def __init__(self, pieza, agua, area_ocu, resistencia, ataques):
        self.pieza = pieza
        self.area = area_ocu
        self.resistencia = resistencia
        self.max_resistencia = resistencia
        self.ataques = ataques
        self.barco = agua
        self.activo = True
        self.habilitado = 0
        self.dano_total = 0

    def recibir_dano(self, arma):
        self.resistencia -= arma.dano
        self.dano_total += arma.dano
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
            if self.ataques[i].inutil is False:
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
        self.ataque_exitosos = 0
        self.ataques_exitosos_tipo = {}  # sumar afuera
        self.dano_causado = 0
        self.dano_recibido = 0  # esta en el vehculo sumarlos
        self.ataque_ocupado = {}
        self.movimientos = {}  # sumar afuera
        self.numero_ataques = 0

    def crear(self):
        todas_armas = [['Misil UGM-133 Trident II', 'Trident II', 5, [1, 1], 'Siempre'],
                       ['Misil de crucero BGM-109 Tomahawk', 'Tomahawk', 5, [1, 'n'], 3],
                       ['Napalm', 'Napalm', 5, [1, 1], 8],
                       ['Misil Balistico Intercontinental Minuteman III', 'Minuteman III', 15, [1, 1], 3],
                       ['Kamikaze', 'Kamikaze', 10000, [1, 1], 1],
                       ['Kit de Ingenieros', 'Kit de Ingenieros', 0, [1], 2],
                       ['GBU-43/B Massive Ordnance Air Blast Paralizer', 'Paralizer', 0, [1, 1], 'Siempre'],
                       ['Explorar', 'Explorar', 0, [3, 3], 'Siempre']]
        a = Vehiculo('Barco Pequeno', True, [3, 1], 30, [Armas(todas_armas[0]), Armas(todas_armas[3]),
                                                         Armas(todas_armas[6])])
        b = Vehiculo('Buque de Guerra', True, [3, 2], 60, [Armas(todas_armas[0]), Armas(todas_armas[1]),
                                                           Armas(todas_armas[6])])
        c = Vehiculo('Lancha', True, [2, 1], 10, [Armas(todas_armas[6])])
        d = Vehiculo('Puerto', True, [4, 2], 80, [Armas(todas_armas[0]), Armas(todas_armas[5]), Armas(todas_armas[6])])
        e = Vehiculo('Avion explorador', False, [2, 2], None, [Armas(todas_armas[7])])
        f = Vehiculo('Kamikaze IXXI', False, [1, 1], None, [Armas(todas_armas[4])])
        g = Vehiculo('Avion Caza', False, [1, 1], None, [Armas(todas_armas[2])])
        listita = [a, b, c, d, e, f, g]
        self.vehiculos += listita

    def mostrar_vehiculos(self, avion):
        for i in range(len(self.vehiculos)):
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

    def mostrar_vehiculos_activos(self):
        orden = []
        a = 1
        for i in range(len(self.vehiculos)):
            if self.vehiculos[i].activo is True:
                r = '[' + str(a) + '] ' + self.vehiculos[i].pieza
                print(r)
                orden2 = [a, i]
                orden.append(orden2)
                a += 1
        return orden

    def habilitar_explorador(self):
        self.vehiculos[4].habilitado -= 1
        if self.vehiculos[4].habilitado <= 0:
            self.vehiculos[4].activo = True

    def revisar_si_gano(self):
        a = [0, 1, 3]
        todos = False
        for i in a:
            if self.vehiculos[i].activo is True:
                todos = True
        return todos

    def ataque_excitoso(self, danados, arma):
        self.ataque_exitosos += 1
        self.dano_causado += len(danados) * arma.dano
        self.ataque_ocupado[arma] += 1

    def mostrar_estadisticas(self, turno):
        r = 'Nombre jugador{}\nPorcentaje ataques exitosos: '.format(self.nombre_jugador)
        if self.numero_ataques > 0:
            r += str((self.ataque_exitosos * 100) / self.numero_ataques) + '%'
        r += '\nDano total causado: ' + str(self.dano_causado)
        lista = list(self.ataque_ocupado.keys())
        lista2 = list(self.ataques_exitosos_tipo.keys())
        for i in range(len(lista2)):
            for z in lista2[i].ataques:
                for n in range(len(lista)):
                    if z == lista[n]:
                        r += lista2[i].pieza + '  '
                        r += str((self.ataques_exitosos_tipo[lista2[i]] * 100) / self.ataque_ocupado[lista[n]]) + '\n\t'
        r += '\nDano total recibido: '
        a = 0
        for i in self.vehiculos:
            a += i.dano_total
        r += str(a) + '\nAtaque mas utilizado: '
        lista = list(self.ataque_ocupado.keys())
        b = 0
        ataque = ''
        for i in range(len(lista)):
            if b < self.ataque_ocupado[lista[i]]:
                b = self.ataque_ocupado[lista[i]]
                ataque = lista[i].nombre
        r += ataque + '\nBarco con mas movimientos: '
        l_movimientos = list(self.movimientos.keys())
        c = 0
        barco = ''
        for i in range(len(l_movimientos)):
            if c < self.movimientos[l_movimientos[i]]:
                b = self.movimientos[l_movimientos[i]]
                barco = lista[i].pieza
        r += barco + '\n Cantidad de turnos: ' + str(turno)
        print(r)


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
                        danadas += [fila, i, mapa[fila][i], 0]
                        destruido = mapa[fila][i].recibir_dano(arma)
                        if destruido is True:
                            destruidas.append(mapa[fila][i])
                            print('Barco {} destruido '.format(mapa[fila][i].pieza))
                            self.mostrar_cordenadas(mapa, mapa[fila][i])
                print('Casillas que dieron con algun blanco: {}'.format(len(danadas)))
            elif lugar == 2:
                for i in range(len(mapa)):
                    if mapa[i][columna] != '':
                        danadas += [i, columna, mapa[i][columna], 0]
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


class Menu:
    def __init__(self):
        self.menu = True

    def mostrar(self, numero):
        if numero == 1:
            print('[1] Atacar o repararse\n[2] Mostrar radar\n[3] Mover\n[4] Rendirse')
        elif numero == 2:
            print('[1] Radar de Ataques\n[2] Radar de defensa\n[3] Salir de radar')
        elif numero == 3:
            print('[1] Mostrar radar acumulado\n[2] Mostrar radar turno en especifico')

    def correr(self, jugador1, tablero1, jugador2, tablero2, turno_actual):
        vehi = jugador1
        table = tablero1
        vehi2 = jugador2
        tablero2 = tablero2
        table.mostrar_tablero(table.agua, vehi)
        table.mostrar_tablero(table.aire, vehi)
        vehi.mostrar_vehiculos('Todos')
        print('-' * 40)
        print('')
        vehi.habilitar_explorador()
        menu1 = 0
        for i in vehi.vehiculos:
            for n in range(len(i.ataques)):
                if i.ataques[n].inutil is True:
                    if i.ataques[n].sobrenombre == 'Napalm' and turno_actual - i.ataques[n].turno_desactivado == 1:
                        try:
                            mapa = tablero2.agua
                            [fila, columna] = i.ataques[n].cordenadas_napalm
                            resultado = mapa[fila][columna].recibir_dano(i.ataques[n])
                            if resultado is True:
                                print('Barco {} destruido '.format(mapa[fila][columna].pieza))
                                tablero2.mostrar_cordenadas(mapa, mapa[fila][columna])
                            print('1 Barco alcanzado en las cordenadas {},{}'.format(chr(fila + 65), str(columna + 1)))
                            vehi.ataque_excitoso([1], i.ataques[n])
                            vehi.ataques_exitosos_tipo[i] += 1
                            vehi.numero_ataques += 1
                        except IndexError:
                            print('0 Barcos alcanzados')
                            table.agregar_radar([], [])
                    if turno_actual - i.ataques[n].turno_desactivado == i.ataques[n].disponibilidad:
                        i.ataques[n].inutil = False
        while menu1 != 3:
            f = True
            while f is True:
                Menu().mostrar(1)
                c = True
                while c is True:
                    try:
                        menu1 = int(input('Seleccione accion a tomar:\t'))
                        if 0 < menu1 <= 4:
                            c = False
                        if c is True:
                            print('Ingrese un numero dentro del rango de opciones')
                    except ValueError:
                        print('Ingrese un numero de la lista no letras')
                        c = True
                if menu1 == 1:
                    print('Seleccione Vehiculo a ocupar:')
                    b = True
                    vehi.mostrar_vehiculos('Todos')
                    selec = 0
                    while b is True:
                        try:
                            selec = int(input())
                            if 0 < selec <= 7:
                                b = False
                            if b is True:
                                print('Ingrese un numero dentro del rango de opciones')
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
                            elegido.ataques[opcion].inutil = True
                            elegido.ataques[opcion].turno_desactivado = turno_actual
                            f = False
                    elif elegido.ataques[opcion].sobrenombre == 'Napalm':
                        mapa = tablero2.agua
                        fila, columna = tablero2.inputs_cordenadas(mapa)
                        try:
                            resultado = mapa[fila][columna].recibir_dano(elegido.ataques[opcion])
                            if resultado is True:
                                print('Barco {} destruido '.format(mapa[fila][columna].pieza))
                                tablero2.mostrar_cordenadas(mapa, mapa[fila][columna])
                            print('1 Barco alcanzado en las cordenadas {},{}'.format(chr(fila + 65), str(columna + 1)))
                            vehi.ataque_excitoso([1], elegido.ataques[opcion])
                            vehi.ataques_exitosos_tipo[elegido] += 1
                        except IndexError:
                            print('0 Barcos alcanzados')
                            table.agregar_radar([], [])
                        elegido.ataques[opcion].inutil = True
                        elegido.ataques[opcion].turno_desactivado = turno_actual
                        elegido.ataques[opcion].cordenadas_napalm = [fila, columna]
                        vehi.numero_ataques += 1
                        f = False
                    else:
                        resultado = tablero2.ataque(elegido.ataques[opcion], vehi2, vehi, table)
                        if elegido.ataques[opcion].disponibilidad != 'Siempre':
                            elegido.ataques[opcion].inutil = True
                            elegido.ataques[opcion].turno_desactivado = turno_actual
                        if resultado is True:
                            vehi.ataques_exitosos_tipo[elegido] += 1
                        vehi.numero_ataques += 1
                        f = False
                elif menu1 == 2:
                    Menu().mostrar(3)
                    c = True
                    menu = 0
                    while c is True:
                        try:
                            menu = int(input('\t'))
                            if 0 < menu <= 2:
                                c = False
                            if c is True:
                                print('Ingrese un numero dentro del rango de opciones')
                        except ValueError:
                            print('Ingrese un numero de la lista no letras')
                            c = True
                    if menu == 1:
                        table.mostrar_radar(-1, vehi)
                        vehi2.mostrar_vehiculos_activos()
                        print('-' * 40)
                        print('')
                    elif menu == 2:
                        c = True
                        menu = 0
                        print('Eliga radar a ver de {} ataques en ataque:'.format(len(table.lista_radar)))
                        while c is True:
                            try:
                                menu = int(input('\t'))
                                if len(table.lista_radar) == 0:
                                    c = False
                                if 0 < menu <= len(table.lista_radar):
                                    c = False
                                if c is True:
                                    print('Ingrese un numero dentro del rango de opciones')
                            except ValueError:
                                print('Ingrese un numero de la lista no letras')
                                c = True
                        table.mostrar_radar(menu - 1, vehi)
                        vehi2.mostrar_vehiculos_activos()
                        print('-' * 40)
                        print('')
                elif menu1 == 3:
                    orden = []
                    b = True
                    ataque = -1
                    while b is True:
                        try:
                            print('Seleccione vehiculo a mover:')
                            orden = vehi.mostrar_vehiculos_activos()
                            ataque = int(input())
                            if 0 < ataque <= len(orden):
                                b = False
                            else:
                                print('Fuera de rango de opciones')
                        except ValueError:
                            print('Ingrese un numero de la lista no letras')
                            b = True
                    opcion = orden[ataque - 1][1]
                    if opcion < 4:
                        mapa = table.agua
                    else:
                        mapa = table.aire
                    opcion = vehi.vehiculos[opcion]
                    if opcion.pieza == 'Lancha':
                        fila, columna = table.inputs_cordenadas(table.agua)
                        if mapa[fila][columna] == '':
                            for i in range(len(mapa)):
                                for n in range(len(mapa[0])):
                                    if mapa[i][n] == opcion:
                                        mapa[i][n] = ''
                            mapa[fila][columna] = opcion
                            print('Movimiento exitoso')
                            vehi.movimientos[opcion] += 1
                            f = False
                        else:
                            print('Movimiento no permitido')
                            f = True
                    else:
                        c = True
                        lugar = 0
                        while c is True:
                            try:
                                lugar = int(input('Ingrese direccion de movimiento del vehiculo:\n[1] Arriba\n'
                                                  '[2] Abajo\n[3] Izquierda\n[4] Derecha\t'))
                                if 0 < lugar <= 4:
                                    c = False
                                if c is True:
                                    print('Ingrese direccion dentro del rango de opciones')
                            except ValueError:
                                print('Ingrese un numero no letras')
                                c = True
                        b = True
                        if lugar == 1:
                            for i in range(len(mapa)):
                                for n in range(len(mapa[0])):
                                    if opcion == mapa[i][n]:
                                        if (mapa[i - 1][n] != '' and mapa[i - 1][n] != opcion) or i - 1 < 0:
                                            b = False
                            if b is True:
                                for i in range(len(mapa)):
                                    for n in range(len(mapa[0])):
                                        if opcion == mapa[i][n]:
                                            mapa[i - 1][n] = opcion
                                            mapa[i][n] = ''
                                print('Movimiento exitoso')
                                vehi.movimientos[opcion] += 1
                        elif lugar == 2:
                            for i in range(len(mapa)):
                                for n in range(len(mapa[0])):
                                    if opcion == mapa[i][n]:
                                        if (mapa[i + 1][n] != '' and mapa[i + 1][n] != opcion) or i + 1 > len(mapa):
                                            b = False
                            if b is True:
                                for i in reversed(range(len(mapa))):
                                    for n in range(len(mapa[0])):
                                        if opcion == mapa[i][n]:
                                            mapa[i + 1][n] = opcion
                                            mapa[i][n] = ''
                                print('Movimiento exitoso')
                                vehi.movimientos[opcion] += 1
                        elif lugar == 3:
                            for i in range(len(mapa)):
                                for n in range(len(mapa[0])):
                                    if opcion == mapa[i][n]:
                                        if (mapa[i][n - 1] != '' and mapa[i][n - 1] != opcion) or n - 1 < 0:
                                            b = False
                            if b is True:
                                for i in range(len(mapa)):
                                    for n in range(len(mapa[0])):
                                        if opcion == mapa[i][n]:
                                            mapa[i][n - 1] = opcion
                                            mapa[i][n] = ''
                                print('Movimiento exitoso')
                                vehi.movimientos[opcion] += 1
                        elif lugar == 4:
                            for i in range(len(mapa)):
                                for n in range(len(mapa[0])):
                                    if opcion == mapa[i][n]:
                                        if (mapa[i][n + 1] != '' and mapa[i][n + 1] != opcion) or n + 1 > len(mapa[0]):
                                            b = False
                            if b is True:
                                for i in range(len(mapa)):
                                    for n in reversed(range(len(mapa[0]))):
                                        if opcion == mapa[i][n]:
                                            mapa[i][n + 1] = opcion
                                            mapa[i][n] = ''
                                print('Movimiento exitoso')
                                vehi.movimientos[opcion] += 1
                        if b is False:
                            print('Movimiento no permitido')
                        else:
                            f = False
                elif menu1 == 4:
                    print('Jugador {} se a rendido'.format(vehi.nombre_jugador))
                    return True
            menu1 = 3
        resultado = vehi2.revisar_si_gano()
        if resultado is False:
            print('Jugador {} a ganado'.format(vehi.nombre_jugador))
            return True


import random


def personavspersona(largo, ancho):
    terminar = False
    c = True
    nombre1 = ''
    while c is True:
        try:
            nombre1 = str(input('Nombre jugador 1: '))
            c = False
        except SyntaxError:
            print('Vuelva a intentarlo')
    vehi1 = CrearVehiculos(nombre1)
    vehi1.crear()
    table1 = Tablero(largo, ancho)
    c = True
    nombre2 = ''
    while c is True:
        try:
            nombre2 = str(input('Nombre jugador 2: '))
            c = False
        except SyntaxError:
            print('Vuelva a intentarlo')
    vehi2 = CrearVehiculos(nombre2)
    vehi2.crear()
    table2 = Tablero(largo, ancho)
    numero = random.randint(1, 2)
    a = 1
    turno = 1
    if numero == 1:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        for i in range(20):  # Para generar espacio entre un jugador y otro
            print('')
        input('Aprete enter cuando le pase el juego al otro jugador:')
        print('Turno jugador {} de poner sus vehiculos'.format(vehi2.nombre_jugador))
        table2.agregar_vehiculo(vehi2)
        vehiculos = vehi1
        tablero = table1
        vehiculos2 = vehi2
        tablero2 = table2
        while terminar is False:
            for i in range(20):  # Para generar espacio entre un jugador y otro
                print('')
            input('Aprete enter cuando le pase el juego al otro jugador:')
            print('Turno jugador {}: '.format(vehiculos.nombre_jugador))
            resultado = Menu().correr(vehiculos, tablero, vehiculos2, tablero2, turno)
            if resultado is True:
                terminar = True
                vehiculos.mostrar_estadisticas(turno)
                vehiculos2.mostrar_estadisticas(turno)
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
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    else:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi2.nombre_jugador))
        table2.agregar_vehiculo(vehi2)
        for i in range(20):  # Para generar espacio entre un jugador y otro
            print('')
        input('Aprete enter cuando le pase el juego al otro jugador:')
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        vehiculos = vehi2
        tablero = table2
        vehiculos2 = vehi1
        tablero2 = table1
        while terminar is False:
            for i in range(20):  # Para generar espacio entre un jugador y otro
                print('')
            input('Aprete enter cuando le pase el juego al otro jugador:')
            print('Turno jugador {}: '.format(vehiculos.nombre_jugador))
            resultado = Menu().correr(vehiculos, tablero, vehiculos2, tablero2, turno)
            if resultado is True:
                terminar = True
                vehiculos.mostrar_estadisticas(turno)
                vehiculos2.mostrar_estadisticas(turno)
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
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    print('Fin del juego')


def personavscomputador(largo, ancho):
    terminar = False
    c = True
    nombre1 = ''
    while c is True:
        try:
            nombre1 = str(input('Nombre jugador: '))
            c = False
        except SyntaxError:
            print('Vuelva a intentarlo')
    vehi1 = CrearVehiculos(nombre1)
    vehi1.crear()
    table1 = Tablero(largo, ancho)
    vehi2 = CrearVehiculos('Computador')
    vehi2.crear()
    table2 = Tablero(largo, ancho)
    numero = random.randint(1, 2)
    a = 1
    turno = 1
    if numero == 1:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        table2.agregar_vehiculo(vehi2)  # hacer algun metodo
        while terminar is False:
            print('Turno jugador {}: '.format(vehi1.nombre_jugador))
            resultado = Menu().correr(vehi1, table1, vehi2, table2, turno)
            # "computador"
            if resultado is True:
                terminar = True
                vehi1.mostrar_estadisticas(turno)
                vehi2.mostrar_estadisticas(turno)
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    else:
        table2.agregar_vehiculo(vehi2)  # metodo computador
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        while terminar is False:
            for i in range(20):  # Para generar espacio entre un jugador y otro
                print('')
            input('Aprete enter cuando le pase el juego al otro jugador:')
            print('Turno jugador {}: '.format(vehi1.nombre_jugador))
            # computador
            resultado = Menu().correr(vehi1, table1, vehi2, table2, turno)
            if resultado is True:
                terminar = True
                vehi1.mostrar_estadisticas(turno)
                vehi2.mostrar_estadisticas(turno)
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    print('Fin del juego')


def juego():
    print('BattleSheep')
    print('Ingrese el tamano del tablero a ocupar, tiene que ser mayor a uno de 7x7:')
    c = True
    largo = 0
    ancho = 0
    while c is True:
        try:
            largo = int(input('Largo: '))
            ancho = int(input('Ancho: '))
            if 6 < largo and 6 < ancho:
                c = False
            if c is True:
                print('Ingrese largo y ancho mayor o igual a 5')
        except ValueError:
            print('Ingrese un numero no letras')
            c = True
    c = True
    player = 0
    while c is True:
        try:
            player = int(input('Contra quien desea jugar:\n[1] Otro Jugador\n[2] Computador '))
            if 0 < player <= 2:
                c = False
            if c is True:
                print('Ingrese contrincante dentro del rango de opciones')
        except ValueError:
            print('Ingrese un numero no letras')
            c = True
    if player == 1:
        personavspersona(largo, ancho)
    elif player == 2:
        pass
        # computador


juego()
# ver Lab 9 vuelo
