__author__ = 'JuanFrancisco'
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
    def posicion(self,nodo):
        nodo_actual=self.cabeza
        a=0
        while nodo_actual:
            if nodo==nodo_actual.valor:
                return a
            else:
                nodo_actual=nodo_actual.siguiente
                a+=1
        return False

    def __repr__(self):
        rep = ''
        nodo_actual = self.cabeza

        while nodo_actual:
            rep += '{0}->'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return rep

l = ListaLigada()
l.agregar_nodo(2)
l.agregar_nodo(4)
l.agregar_nodo(7)
print(l.posicion(2))
print(l.obtener(3))
print(l.obtener(1))

print(l)