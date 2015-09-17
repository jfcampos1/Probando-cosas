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
nodos=lista_nodos
with open('red.txt','w') as arch:
    nodo=nodos.cabeza
    while nodo:
        print('Puerto {}'.format(nodo.valor),file=arch)
        nodo=nodo.siguiente
    nodo=nodos.cabeza
    while nodo:
        pos=puertos.posicion(nodo.valor)
        num_conec=numero_conexiones.obtener(pos)
        a=0
        while a!=num_conec-1:
            pos=puertos.nodos(nodo.valor,a,conexion_ocupada,tipo_conexion)
            tip=tipo_conexion.obtener(pos)
            if tip==1:
                print('Conexion {} {} {}'.format(nodo.valor,puertos.obtener(pos),'Alt o Rand'),file=arch)
            else:
                print('Conexion {} {}'.format(nodo.valor,puertos.obtener(pos)),file=arch)
                a+=1
        nodo=nodo.siguiente
nodo_actual=puertos.cabeza
with open('ciclos.txt','w') as arch:
    a=0
    while nodo_actual:
        if nodo_actual.valor==nodo_actual.siguiente.siguiente.siguiente.valor:
            b=0
            for i in range(3):
                if tipo_conexion.obtener(a+i)==-1:
                    b=-1
            if b!=-1:
                n_0=nodo_actual.valor
                n_1=nodo_actual.siguiente.valor
                n_2=nodo_actual.siguiente.siguiente.valor
                print('{} {} {}'.format(n_0,n_1,n_2),file=arch)
        elif nodo_actual.valor==nodo_actual.siguiente.siguiente.siguiente.siguiente.valor:
            b=0
            for i in range(4):
                if tipo_conexion.obtener(a+i)==-1:
                    b=-1
            if b!=-1:
                n_0=nodo_actual.valor
                n_1=nodo_actual.siguiente.valor
                n_2=nodo_actual.siguiente.siguiente.valor
                n_3=nodo_actual.siguiente.siguiente.siguiente.valor
                print('{} {} {} {}'.format(n_0,n_1,n_2,n_3),file=arch)
        nodo_actual=nodo_actual.siguiente




l = ListaLigada()
l.agregar_nodo(2)
l.agregar_nodo(4)
l.agregar_nodo(7)
l.cabeza.siguiente.valor=1
print(l.posicion(2))
print(l.obtener(3))
print(l.obtener(1))
d=3
print(d%2)

print(l)