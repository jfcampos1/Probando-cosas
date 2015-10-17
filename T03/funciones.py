__author__ = 'JuanFrancisco'

import random
import menu
import clasesbasicas
import clasetablero


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
    vehi1 = clasesbasicas.CrearVehiculos(nombre1)
    vehi1.crear()
    table1 = clasetablero.Tablero(largo, ancho)
    c = True
    nombre2 = ''
    while c is True:
        try:
            nombre2 = str(input('Nombre jugador 2: '))
            c = False
        except SyntaxError:
            print('Vuelva a intentarlo')
    vehi2 = clasesbasicas.CrearVehiculos(nombre2)
    vehi2.crear()
    table2 = clasetablero.Tablero(largo, ancho)
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
            resultado = menu.Menu().correr(vehiculos, tablero, vehiculos2, tablero2, turno)
            if resultado is True:
                terminar = True
                vehiculos.mostrar_estadisticas(turno)
                print('-' * 40)
                print('')
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
            resultado = menu.Menu().correr(vehiculos, tablero, vehiculos2, tablero2, turno)
            if resultado is True:
                terminar = True
                vehiculos.mostrar_estadisticas(turno)
                print('-' * 40)
                print('')
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
    vehi1 = clasesbasicas.CrearVehiculos(nombre1)
    vehi1.crear()
    table1 = clasetablero.Tablero(largo, ancho)
    vehi2 = clasesbasicas.CrearVehiculos('Computador')
    vehi2.crear()
    table2 = clasetablero.Tablero(largo, ancho)
    numero = random.randint(1, 2)
    a = 1
    turno = 1
    if numero == 1:
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        table2.posicionar_robot(vehi2)
        while terminar is False:
            print('Turno jugador {}: '.format(vehi1.nombre_jugador))
            resultado = menu.Menu().correr(vehi1, table1, vehi2, table2, turno)
            menu.Menu().computador(table2,table1,vehi2,vehi1,turno)
            if resultado is True:
                terminar = True
                vehi1.mostrar_estadisticas(turno)
                print('-' * 40)
                print('')
                vehi2.mostrar_estadisticas(turno)
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    else:
        table2.posicionar_robot(vehi2)
        print('Turno jugador {} de poner sus vehiculos'.format(vehi1.nombre_jugador))
        table1.agregar_vehiculo(vehi1)
        while terminar is False:
            menu.Menu().computador(table2,table1,vehi2,vehi1,turno)
            print('Turno jugador {}: '.format(vehi1.nombre_jugador))
            # computador
            resultado = menu.Menu().correr(vehi1, table1, vehi2, table2, turno)
            if resultado is True:
                terminar = True
                vehi1.mostrar_estadisticas(turno)
                print('-' * 40)
                print('')
                vehi2.mostrar_estadisticas(turno)
            if a == 1:
                a += 1
            else:
                a = 1
                turno += 1
    print('Fin del juego')
