__author__ = 'JuanFrancisco'
import random


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
                            try:
                                numero1 = vehi.ataques_exitosos_tipo[i]
                                numero1 += 1
                                vehi.ataques_exitosos_tipo[i] = numero1
                            except KeyError:
                                vehi.ataques_exitosos_tipo[i] = 1
                            vehi.numero_ataques += 1
                            resultado = vehi2.revisar_si_gano()
                            if resultado is False:
                                print('Jugador {} a ganado'.format(vehi.nombre_jugador))
                                return True
                        except IndexError:
                            print('0 Barcos alcanzados')
                            table.agregar_radar([], [])
                    if turno_actual - i.ataques[n].turno_desactivado == i.ataques[n].disponibilidad:
                        i.ataques[n].inutil = False
        explorador = vehi2.vehiculos[4].ataques[0]
        if explorador.inutil is True:
            if turno_actual - explorador.turno_desactivado == 1 or turno_actual - explorador.turno_desactivado == 0:
                posibilidad = random.randrange(100)
                if posibilidad < 50:
                    print('Fuiste espiado: \n')
                    tablero2.mostrar_cordenada(tablero2.agua, vehi2.vehiculos[4])
        tablero2.verificar_destruidos()
        table.mostrar_tablero(table.agua, vehi)
        table.mostrar_tablero(table.aire, vehi)
        vehi.mostrar_vehiculos('Todos')
        print('-' * 40)
        print('')
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
                    if elegido.activo is True:
                        orden = []
                        b = True
                        ataque = -1
                        while b is True:
                            try:
                                print('Seleccione ataque a ocupar:')
                                orden = elegido.mostrar_ataques()
                                ataque = int(input())
                                if len(orden) == 0:
                                    b = False
                                    print('No hay ataques para ocupar')
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
                                print('1 Barco alcanzado en las cordenadas {},{}'.format(chr(fila + 65),
                                                                                         str(columna + 1)))
                                vehi.ataque_excitoso([1], elegido.ataques[opcion])
                                try:
                                    numero1 = vehi.ataques_exitosos_tipo[elegido]
                                    numero1 += 1
                                    vehi.ataques_exitosos_tipo[elegido] = numero1
                                except KeyError:
                                    vehi.ataques_exitosos_tipo[elegido] = 1
                            except IndexError:
                                print('0 Barcos alcanzados')
                                table.agregar_radar([], [])
                            elegido.ataques[opcion].inutil = True
                            elegido.ataques[opcion].turno_desactivado = turno_actual
                            elegido.ataques[opcion].cordenadas_napalm = [fila, columna]
                            vehi.numero_ataques += 1
                            f = False
                        else:
                            resultado = tablero2.ataque(elegido.ataques[opcion], vehi2, vehi, table, turno_actual)
                            if elegido.ataques[opcion].disponibilidad != 'Siempre':
                                elegido.ataques[opcion].inutil = True
                                elegido.ataques[opcion].turno_desactivado = turno_actual
                            if resultado is True:
                                try:
                                    numero1 = vehi.ataques_exitosos_tipo[elegido]
                                    numero1 += 1
                                    vehi.ataques_exitosos_tipo[elegido] = numero1
                                except KeyError:
                                    vehi.ataques_exitosos_tipo[elegido] = 1
                            vehi.numero_ataques += 1
                            f = False
                    else:
                        print('Vehiculo destruido no dispone de ataques')
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
                        table.mostrar_radar(-1, vehi2)
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
                                if 0 < menu <= len(table.lista_radar):
                                    c = False
                                if c is True:
                                    print('Ingrese un numero dentro del rango de opciones')
                            except ValueError:
                                if len(table.lista_radar) == 0:
                                    print('No hay radar para mostrar')
                                    c = False
                                else:
                                    print('Ingrese un numero de la lista no letras')
                                    c = True
                        table.mostrar_radar(menu - 1, vehi2)
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
                            try:
                                numero1 = vehi.movimientos[opcion]
                                numero1 += 1
                                vehi.movimientos[opcion] = numero1
                            except KeyError:
                                vehi.movimientos[opcion] = 1
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
                                try:
                                    numero1 = vehi.movimientos[opcion]
                                    numero1 += 1
                                    vehi.movimientos[opcion] = numero1
                                except KeyError:
                                    vehi.movimientos[opcion] = 1
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
                                try:
                                    numero1 = vehi.movimientos[opcion]
                                    numero1 += 1
                                    vehi.movimientos[opcion] = numero1
                                except KeyError:
                                    vehi.movimientos[opcion] = 1
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
                                try:
                                    numero1 = vehi.movimientos[opcion]
                                    numero1 += 1
                                    vehi.movimientos[opcion] = numero1
                                except KeyError:
                                    vehi.movimientos[opcion] = 1
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
                                try:
                                    numero1 = vehi.movimientos[opcion]
                                    numero1 += 1
                                    vehi.movimientos[opcion] = numero1
                                except KeyError:
                                    vehi.movimientos[opcion] = 1
                        if b is False:
                            print('Movimiento no permitido')
                        else:
                            f = False
                elif menu1 == 4:
                    print('Jugador {} se a rendido'.format(vehi.nombre_jugador))
                    return True
            menu1 = 3
        table.verificar_destruidos()
        tablero2.verificar_destruidos()
        resultado = vehi2.revisar_si_gano()
        if resultado is False:
            print('Jugador {} a ganado'.format(vehi.nombre_jugador))
            return True

    def computador(self, tablero_computador, tablero_jugador, vehi_c, vehi_jugador):
        b = True
        tablero_computador.mostrar_tablero(tablero_computador.agua, vehi_c)
        while b is True:
            accion = random.randint(1, 2)
            if accion == 1:
                tablero_jugador.ataque_computador(tablero_computador, vehi_c, vehi_jugador)
                b=False
            elif accion == 2:
                vehiculo = random.randint(0, 3)
                opcion = vehi_c.vehiculos[vehiculo]
                direccion = random.randint(1, 4)
                mapa = tablero_computador.agua
                if opcion.pieza == 'Lancha':
                    fila = random.randrange(len(mapa))
                    columna = random.randrange(len(mapa[0]))
                    if mapa[fila][columna] == '':
                        for i in range(len(mapa)):
                            for n in range(len(mapa[0])):
                                if mapa[i][n] == opcion:
                                    mapa[i][n] = ''
                        mapa[fila][columna] = opcion
                        try:
                            numero1 = vehi_c.movimientos[opcion]
                            numero1 += 1
                            vehi_c.movimientos[opcion] = numero1
                        except KeyError:
                            vehi_c.movimientos[opcion] = 1
                        b = False
                    else:
                        b = True
                else:
                    if direccion == 1:
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
                            try:
                                numero1 = vehi_c.movimientos[opcion]
                                numero1 += 1
                                vehi_c.movimientos[opcion] = numero1
                            except KeyError:
                                vehi_c.movimientos[opcion] = 1
                    elif direccion == 2:
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
                            try:
                                numero1 = vehi_c.movimientos[opcion]
                                numero1 += 1
                                vehi_c.movimientos[opcion] = numero1
                            except KeyError:
                                vehi_c.movimientos[opcion] = 1
                    elif direccion == 3:
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
                            try:
                                numero1 = vehi_c.movimientos[opcion]
                                numero1 += 1
                                vehi_c.movimientos[opcion] = numero1
                            except KeyError:
                                vehi_c.movimientos[opcion] = 1
                    elif direccion == 4:
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
                            try:
                                numero1 = vehi_c.movimientos[opcion]
                                numero1 += 1
                                vehi_c.movimientos[opcion] = numero1
                            except KeyError:
                                vehi_c.movimientos[opcion] = 1
        tablero_computador.verificar_destruidos()
        tablero_jugador.verificar_destruidos()
        resultado = vehi_jugador.revisar_si_gano()
        if resultado is False:
            print('Jugador {} a ganado'.format(vehi_c.nombre_jugador))
            return True
