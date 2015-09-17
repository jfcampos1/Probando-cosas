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

    def posicion(self, nodo, conexion_ocupada, tipo_conexion):
        nodo_actual = self.cabeza
        a = 0
        b = -1
        while nodo_actual:
            if nodo == nodo_actual.valor:
                if b == -1:
                    b = a
                else:
                    if tipo_conexion.obtener(a) != -1:
                        if conexion_ocupada.obtener(a) > conexion_ocupada.obtener(b):
                            b = a
            nodo_actual = nodo_actual.siguiente
            a += 1
        if b != -1:
            return b
        else:
            return False

    def esta_dentro(self, nodo):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == nodo:
                return True
            nodo_actual=nodo_actual.siguiente
        return False

    def solo_nodos(self):  # lista de los nodos sin repetir
        nodo_actual = self.cabeza
        lista_nodos = ListaLigada()
        while nodo_actual:
            if lista_nodos.obtener(nodo_actual.valor) is False:
                lista_nodos.agregar_nodo(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return lista_nodos

    def nodos(self, nodo, valor, lista_conec, lista_tipo):
        nodo_actual = self.cabeza
        a = 0
        while nodo_actual:
            if nodo_actual.valor == nodo and lista_conec.obtener(a) == valor and lista_tipo.obtener(a) != -1:
                return a
            else:
                nodo_actual = nodo_actual.siguiente
                a += 1

    def __repr__(self):
        rep = ''
        nodo_actual = self.cabeza

        while nodo_actual:
            rep += '{0}->'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return rep


def camino(punto_inicio, punto_final):
    punto_actual = sistema.preguntar_puerto_actual()
    puertos = ListaLigada()
    conexion_ocupada = ListaLigada()
    numero_conexciones = ListaLigada()
    tipo_conexcion = ListaLigada()
    las_listas = ListaLigada()
    while punto_actual[0] != punto_final:
        conexciones = sistema.posibles_conexiones()
        numero_conexciones.agregar_nodo(conexciones)
        pos = puertos.posicion(punto_actual[0], conexion_ocupada, tipo_conexcion)
        if pos is not False:
            puertos.agregar_nodo(punto_actual[0])
            conec = conexion_ocupada.obtener(pos)
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
            tipo_conexcion.agregar_nodo(-1)
        else:
            tipo_conexcion.agregar_nodo(0)
        # En tipo 0=normal, -1=me atraparon, 1=alt o random
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


def camino2(punto_inicio, punto_final, lista):
    punto_actual = sistema.preguntar_puerto_actual()
    puertos = lista.obtener(0)
    conexion_ocupada = lista.obtener(1)
    numero_conexciones = lista.obtener(2)
    tipo_conexcion = lista.obtener(3)
    las_listas = ListaLigada()
    while punto_actual[0] != punto_final:
        conexciones = sistema.posibles_conexiones()
        numero_conexciones.agregar_nodo(conexciones)
        pos = puertos.posicion(punto_actual[0], conexion_ocupada, tipo_conexcion)
        if pos is not False:
            puertos.agregar_nodo(punto_actual[0])
            conec = conexion_ocupada.obtener(pos)
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
            tipo_conexcion.agregar_nodo(-1)
        else:
            tipo_conexcion.agregar_nodo(0)
        # En tipo 0=normal, -1=me atraparon, 1=alt o random
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
    nodos_listos = ListaLigada()
    todos_nodos = puertos.cabeza
    nodo = puertos.cabeza
    c = 0
    while todos_nodos:
        if nodos_listos.esta_dentro(todos_nodos.valor) is False:
            pos = puertos.posicion(todos_nodos.valor, conexion_ocupada, tipo_conexion)
            ultima_conexion = conexion_ocupada.obtener(pos)
            max_conexiones = numero_conexciones.obtener(pos)
            if ultima_conexion == max_conexiones - 1:
                nodos_listos.agregar_nodo(todos_nodos.valor)
                todos_nodos = todos_nodos.siguiente
            else:
                while ultima_conexion != max_conexiones - 1:
                    print('a')
                    a = 0
                    tipo = tipo_conexion.cabeza
                    nodos = ListaLigada()
                    conec = ListaLigada()
                    numconec = ListaLigada()
                    tip = ListaLigada()
                    while nodo.valor != todos_nodos.valor:
                        sistema.hacer_conexion(conexion_ocupada.obtener(a))
                        punto_actual = sistema.preguntar_puerto_actual()
                        if punto_actual[0] == nodo.siguiente.valor:
                            nodos.agregar_nodo(nodo.valor)
                            conec.agregar_nodo(conexion_ocupada.obtener(a))
                            numconec.agregar_nodo(numero_conexciones.obtener(a))
                            tip.agregar_nodo(tipo_conexion.obtener(a))
                            nodo = nodo.siguiente
                            tipo = tipo.siguiente
                            a += 1
                        elif tipo_conexion.obtener(a) == -1:
                            camino(punto_actual[0], nodo.siguiente.valor)
                            nodo = nodo.siguiente
                            tipo = tipo.siguiente
                            nodos = ListaLigada()
                            conec = ListaLigada()
                            numconec = ListaLigada()
                            tip = ListaLigada()
                            a += 1
                        elif punto_actual[1]:
                            nodo = puertos.cabeza
                            tipo = tipo_conexion.cabeza
                            nodos = ListaLigada()
                            conec = ListaLigada()
                            numconec = ListaLigada()
                            tip = ListaLigada()
                            a = 0
                        else:
                            nodos.agregar_nodo(nodo.valor)
                            conec.agregar_nodo(conexion_ocupada.obtener(a))
                            numconec.agregar_nodo(numero_conexciones.obtener(a))
                            tip.agregar_nodo(1)
                            nodos.agregar_nodo(punto_actual[0])
                            conec.agregar_nodo(-1)
                            numconec.agregar_nodo(sistema.posibles_conexiones())
                            tip.agregar_nodo(-1)
                            camino(punto_actual[0], nodo.siguiente.valor)
                            tipo = tipo.siguiente
                            nodo = nodo.siguiente
                            a += 1
                    sistema.hacer_conexion(conexion_ocupada.obtener(pos) + 1)
                    punto_actual = sistema.preguntar_puerto_actual()
                    if punto_actual[1] is True:
                        pass
                    else:
                        nodos.agregar_nodo(nodo.valor)
                        conec.agregar_nodo(conexion_ocupada.obtener(pos) + 1)
                        numconec.agregar_nodo(numero_conexciones.obtener(a))
                        tip.agregar_nodo(0)
                        nodos.agregar_nodo(punto_actual[0])
                        conec.agregar_nodo(-1)
                        numconec.agregar_nodo(sistema.posibles_conexiones())
                        tip.agregar_nodo(-1)
                        tips = tip.cabeza
                        b = 0
                        while tips:
                            puertos.agregar_nodo(nodos.obtener(b))
                            conexion_ocupada.agregar_nodo(conec.obtener(b))
                            numero_conexciones.agregar_nodo(numconec.obtener(b))
                            tipo_conexion.agregar_nodo(tip.obtener(b))
                            b += 1
                            tips = tips.siguiente
                    camino(punto_actual[0], puertos.cabeza.valor)
                    nodo = puertos.cabeza
                    pos = puertos.posicion(todos_nodos.valor, conexion_ocupada, tipo_conexion)
                    ultima_conexion = conexion_ocupada.obtener(pos)
                nodos_listos.agregar_nodo(todos_nodos.valor)
                todos_nodos = todos_nodos.siguiente
        else:
            todos_nodos = todos_nodos.siguiente
        print('siguiente nodoooooooooooooooooooooooooo', c)
        c += 1
    print('Eeeeeexitooooo')
    las_listas = ListaLigada()
    las_listas.agregar_nodo(puertos)
    las_listas.agregar_nodo(conexion_ocupada)
    las_listas.agregar_nodo(numero_conexciones)
    las_listas.agregar_nodo(tipo_conexion)
    return las_listas


def red(lista):
    puertos = lista.obtener(0)
    conexion_ocupada = lista.obtener(1)
    numero_conexiones = lista.obtener(2)
    tipo_conexion = lista.obtener(3)
    nodos = puertos.solo_nodos()
    with open('red.txt', 'w') as arch:
        nodo = nodos.cabeza
        while nodo:
            print('Puerto {}'.format(nodo.valor), file=arch)
            nodo = nodo.siguiente
        nodo = nodos.cabeza
        while nodo:
            pos = puertos.posicion(nodo.valor)
            num_conec = numero_conexiones.obtener(pos)
            a = 0
            while a != num_conec - 1:
                pos = puertos.nodos(nodo.valor, a, conexion_ocupada, tipo_conexion)
                tip = tipo_conexion.obtener(pos)
                if tip == 1:
                    print('Conexion {} {} {}'.format(nodo.valor, puertos.obtener(pos), 'Alt o Rand'), file=arch)
                else:
                    print('Conexion {} {}'.format(nodo.valor, puertos.obtener(pos)), file=arch)
                    a += 1
            nodo = nodo.siguiente


def ciclos(lista):
    puertos = lista.obtener(0)
    tipo_conexion = lista.obtener(3)
    nodo_actual = puertos.cabeza
    with open('ciclos.txt', 'w') as arch:
        a = 0
        while nodo_actual:
            if nodo_actual.valor == nodo_actual.siguiente.siguiente.siguiente.valor:
                b = 0
                for i in range(3):
                    if tipo_conexion.obtener(a + i) == -1:
                        b = -1
                if b != -1:
                    n_0 = nodo_actual.valor
                    n_1 = nodo_actual.siguiente.valor
                    n_2 = nodo_actual.siguiente.siguiente.valor
                    print('{} {} {}'.format(n_0, n_1, n_2), file=arch)
            elif nodo_actual.valor == nodo_actual.siguiente.siguiente.siguiente.siguiente.valor:
                b = 0
                for i in range(4):
                    if tipo_conexion.obtener(a + i) == -1:
                        b = -1
                if b != -1:
                    n_0 = nodo_actual.valor
                    n_1 = nodo_actual.siguiente.valor
                    n_2 = nodo_actual.siguiente.siguiente.valor
                    n_3 = nodo_actual.siguiente.siguiente.siguiente.valor
                    print('{} {} {} {}'.format(n_0, n_1, n_2, n_3), file=arch)
            nodo_actual = nodo_actual.siguiente


def menu():
    punto_inicio = sistema.puerto_inicio()
    punto_final = sistema.puerto_final()
    lista = camino(punto_inicio, punto_final)
    vuelta = camino2(punto_final, punto_inicio, lista)
    d = 0
    while d != 4:
        if d % 2 == 0:
            vuelta = camino2(punto_inicio, punto_final=punto_final, lista=vuelta)
        else:
            vuelta = camino2(punto_final, punto_final=punto_inicio, lista=vuelta)
        print('funciona', d)
        d += 1
    listota = rellernar_el_mapa(lista)
    red(listota)
    ciclos(listota)


t = datetime.datetime.now()
menu()
print(datetime.datetime.now() - t)
