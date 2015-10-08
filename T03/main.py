__author__ = 'JuanFrancisco'
import funciones


def juego():
    print('BattleSheep')
    print('Ingrese el tamano del tablero a ocupar, tiene que ser mayor o igual a uno de 7x7:')
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
        funciones.personavspersona(largo, ancho)
    elif player == 2:
        funciones.personavscomputador(largo,ancho)


juego()
