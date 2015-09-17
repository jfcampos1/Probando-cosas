__author__ = 'JuanFrancisco'
import sistema
import datetime


class Nodo:
    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor


class ListaLigada:
    def __init__(self):
        self.cola = None
        self.cabeza = None

    def agregar_nodo(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
            self.cola = self.cabeza
        else:
            self.cola.siguiente = Nodo(valor)
            self.cola = self.cola.siguiente

    def obtener(self, posicion):
        nodo = self.cabeza

        for i in range(posicion):
            if nodo:
                nodo = nodo.siguiente
        if not nodo:
            return False
        else:
            return nodo.valor

    def posicion(self, nodo, conexion_ocupada,tipo_conexion):
        nodo_actual = self.cabeza
        a = 0
        b = -1
        while nodo_actual:
            if nodo == nodo_actual.valor:
                if b == -1:
                    b = a
                else:
                    if conexion_ocupada.obtener(a) > conexion_ocupada.obtener(b) and tipo_conexion.obtener(a)!=-1:
                        b = a
            nodo_actual = nodo_actual.siguiente
            a += 1
        if b != -1:
            return b
        else:
            return False

    def posiciones_usadas(self, pos):
        nodo_actual = self.cabeza
        a = 0
        b = -1
        while nodo_actual:
            if nodo == nodo_actual.valor:
                b = a
            nodo_actual = nodo_actual.siguiente
            a += 1
        if b != -1:
            return b
        else:
            return False

    def nodos(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            b = 0
            while b != False:
                b = ListaLigada.posicion(nodo_actual.valor)
                pass

    def __repr__(self):
        rep = ''
        nodo_actual = self.cabeza

        while nodo_actual:
            rep += '{0}->'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return rep


def camino(punto_inicio, punto_final):
    print(punto_inicio,punto_final)
    punto_actual = sistema.preguntar_puerto_actual()
    puertos = ListaLigada()
    conexion_ocupada = ListaLigada()
    numero_conexciones = ListaLigada()
    tipo_conexcion = ListaLigada()
    las_listas = ListaLigada()
    a = 0
    b = 0
    while punto_actual[0] != punto_final:
        robot = sistema.preguntar_puerto_robot()  # hasta ahora no se ocupa
        conexciones = sistema.posibles_conexiones()
        numero_conexciones.agregar_nodo(conexciones)
        pos = puertos.posicion(punto_actual[0], conexion_ocupada,tipo_conexcion)
        if pos is not False:
            puertos.agregar_nodo(punto_actual[0])
            conec = conexion_ocupada.obtener(pos)
            print('se repite', punto_actual[0])
            a += 1
            if conec + 1 > conexciones - 1:
                conec = -1
            sistema.hacer_conexion(conec + 1)
            conexion_ocupada.agregar_nodo(conec + 1)
            punto_actual = sistema.preguntar_puerto_actual()
        else:
            puertos.agregar_nodo(punto_actual[0])
            sistema.hacer_conexion(0)
            conexion_ocupada.agregar_nodo(0)
            punto_actual = sistema.preguntar_puerto_actual()
        if punto_actual[1]:
            print('Atrapado, Te desconecto bla bla bla bla bla')
            tipo_conexcion.agregar_nodo(-1)
        else:
            tipo_conexcion.agregar_nodo(0)
        b += 1
        # En tipo 0=normal, -1=me atraparon, 1=alt o random
    print('saliste', punto_actual, punto_final, a, b)
    conexciones = sistema.posibles_conexiones()
    puertos.agregar_nodo(punto_final)
    numero_conexciones.agregar_nodo(conexciones)
    conexion_ocupada.agregar_nodo(0)
    tipo_conexcion.agregar_nodo(-1)
    las_listas.agregar_nodo(puertos)
    las_listas.agregar_nodo(conexion_ocupada)
    las_listas.agregar_nodo(numero_conexciones)
    las_listas.agregar_nodo(tipo_conexcion)
    return las_listas


def rellernar_el_mapa(lista):
    puertos = lista.obtener(0)
    conexion_ocupada = lista.obtener(1)
    numero_conexciones = lista.obtener(2)
    tipo_conexion = lista.obtener(3)
    todos_nodos = puertos.cabeza
    nodo = puertos.cabeza
    while todos_nodos:
        pos = puertos.posicion(todos_nodos.valor, conexion_ocupada,tipo_conexion)
        ultima_conexion = conexion_ocupada.obtener(pos)
        max_conexiones = numero_conexciones.obtener(pos)
        if ultima_conexion == max_conexiones - 1:
            todos_nodos = todos_nodos.siguiente
        else:
            while ultima_conexion != max_conexiones - 1:
                a = 0
                tipo = tipo_conexion.cabeza
                nodos = ListaLigada()
                conec = ListaLigada()
                numconec = ListaLigada()
                tip = ListaLigada()
                punto_actual = sistema.preguntar_puerto_actual()
                print('acaaaaaaaaaaaaaaaaaaaaaaaaa')
                while nodo.valor != todos_nodos.valor:
                    sistema.hacer_conexion(conexion_ocupada.obtener(a))
                    punto_actual = sistema.preguntar_puerto_actual()
                    if punto_actual[0] == nodo.siguiente.valor:
                        print('pase por aqui',a)
                        nodos.agregar_nodo(nodo.valor)
                        conec.agregar_nodo(conexion_ocupada.obtener(a))
                        numconec.agregar_nodo(numero_conexciones.obtener(a))
                        tip.agregar_nodo(tipo_conexion.obtener(a))
                        nodo = nodo.siguiente
                        tipo = tipo.siguiente

                        a += 1
                    elif tipo_conexion.obtener(a) == -1:
                        print('Ooooooh')
                        camino(punto_actual[0],nodo.siguiente.valor)
                        nodo = nodo.siguiente
                        tipo = tipo.siguiente
                        nodos = ListaLigada()
                        conec = ListaLigada()
                        numconec = ListaLigada()
                        tip = ListaLigada()

                        a += 1
                    else:
                        print('por acaaaaaaaaaaaaaaaaaa')
                        nodos.agregar_nodo(nodo.valor)
                        conec.agregar_nodo(conexion_ocupada.obtener(a))
                        numconec.agregar_nodo(numero_conexciones.obtener(a))
                        tip.agregar_nodo(1)
                        nodos.agregar_nodo(punto_actual[0])
                        conec.agregar_nodo(-1)
                        numconec.agregar_nodo(sistema.posibles_conexiones())
                        tip.agregar_nodo(-1)
                        camino(punto_actual[0],puertos.cabeza.valor)
                        tipo = tipo_conexion.cabeza
                        nodo = puertos.cabeza
                sistema.hacer_conexion(conexion_ocupada.obtener(pos)+1)
                punto_actual = sistema.preguntar_puerto_actual()
                if punto_actual[1]==True:
                    pass
                else:
                    print('aquiiiiiiiiiiiiiiiiiii')
                    nodos.agregar_nodo(nodo.valor)
                    conec.agregar_nodo(conexion_ocupada.obtener(pos)+1)
                    numconec.agregar_nodo(numero_conexciones.obtener(a))
                    tip.agregar_nodo(0)
                    nodos.agregar_nodo(punto_actual[0])
                    conec.agregar_nodo(-1)
                    numconec.agregar_nodo(sistema.posibles_conexiones())
                    tip.agregar_nodo(-1)
                    tips=tip.cabeza
                    b=0
                    while tips:
                        puertos.agregar_nodo(nodos.obtener(b))
                        conexion_ocupada.agregar_nodo(conec.obtener(b))
                        numero_conexciones.agregar_nodo(numconec.obtener(b))
                        tipo_conexion.agregar_nodo(tip.obtener(b))
                        b+=1
                        tips=tips.siguiente
                camino(punto_actual[0],puertos.cabeza.valor)
                nodo =puertos.cabeza
                pos = puertos.posicion(todos_nodos.valor, conexion_ocupada,tipo_conexion)
                ultima_conexion=conexion_ocupada.obtener(pos)
            todos_nodos = todos_nodos.siguiente


def menu():
    punto_inicio = sistema.puerto_inicio()
    punto_final = sistema.puerto_final()
    print('ida')
    lista=camino(punto_inicio, punto_final)
    camino(punto_final,punto_inicio)
    rellernar_el_mapa(lista)


t = datetime.datetime.now()
menu()
print(datetime.datetime.now() - t)
