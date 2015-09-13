__author__ = 'JuanFrancisco'
import sistema


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

    def posicion(self, nodo):
        nodo_actual = self.cabeza
        a = 0
        while nodo_actual:
            if nodo == nodo_actual.valor:
                return a
            else:
                nodo_actual = nodo_actual.siguiente
                a += 1
        return False

    def __repr__(self):
        rep = ''
        nodo_actual = self.cabeza

        while nodo_actual:
            rep += '{0}->'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return rep


def menu():
    punto_inicio = sistema.puerto_inicio()
    punto_final = sistema.puerto_final()
    print(punto_final, punto_inicio)
    punto_actual = sistema.preguntar_puerto_actual()
    puertos = ListaLigada()
    conexion_ocupada=ListaLigada()
    a = 0
    while punto_actual != punto_final:
        print(punto_actual)
        conexciones= sistema.posibles_conexiones()
        pos=puertos.posicion(punto_actual[0])
        if pos is not False:
            puertos.agregar_nodo(punto_actual[0])
            conec=conexion_ocupada.obtener(pos)
            print('se repite', punto_actual[0])
            a += 1
            print(conexciones)
            if conec+1>conexciones-1:
                conec=-1
            hacer_conexcion = sistema.hacer_conexion(conec+1)
            conexion_ocupada.agregar_nodo(conec+1)
            punto_actual = sistema.preguntar_puerto_actual()
        else:
            puertos.agregar_nodo(punto_actual[0])
            print(conexciones)
            hacer_conexcion = sistema.hacer_conexion(0)
            punto_actual = sistema.preguntar_puerto_actual()


menu()
