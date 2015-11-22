__author__ = 'JuanFrancisco'
# coding=utf-8
from collections import deque


class Arbol:
    def __init__(self, id_nodo, nombre=None, valor=None, id_padre=None):
        self.id_nodo = id_nodo
        self.id_padre = id_padre
        self.valor = valor
        self.nombre = nombre
        self.hijos = {}

    def agregar_nodo(self, id_nodo, nombre, valor=None, id_padre=None):
        # Cada vez que agregamos un nodo verificamos primero si corresponde al nodo padre donde queremos agregar
        # el nuevo nodo. Si no es el nodo, buscamos recursivamente a través de todos los nodos existentes hasta que
        # encontremos el nodo correspondiente.
        if self.id_nodo == id_padre:
            # Si el nodo es el nodo padre, entonces actualizamos el diccionario con los hijos
            self.hijos.update({id_nodo: Arbol(id_nodo, nombre, valor, id_padre)})
        else:
            for hijo in self.hijos.values():
                hijo.agregar_nodo(id_nodo, nombre, valor, id_padre)

    def obtener_nodo(self, id_nodo):
        # recursivamente obtenemos el nodo siempre y cuando exista la posicion.
        if self.id_nodo == id_nodo:
            return self
        else:
            for hijo in self.hijos.values():
                nodo = hijo.obtener_nodo(id_nodo)
                if nodo:
                    # retorna el nodo si es que existe en el árbol
                    return nodo

    def recorrer_arbol(self, raiz):  # por lineas
        Q = deque()
        Q.append(raiz)
        ret = ''
        while len(Q) > 0:
            p = Q.popleft()
            ret += "nodo_id: {}, id_padre: {} -> valor: {}\n".format(p.id_nodo, p.id_padre, p.valor)
            for hijo in p.hijos.values():
                Q.append(hijo)
        return ret

    def recorrer_hijos(self, raiz):  # es como obtener el os.listdir()
        ret = []
        p = raiz
        for hijo in p.hijos.values():
            ret.append(hijo)
        return ret

    def __repr__(self):
        # Para visualizar el arbol redefinimos el método __repr__ para recorrer recursivamente todos los nodos del árbol.
        def recorrer_arbol(raiz):
            for hijo in raiz.hijos.values():
                self.ret += "id-nodo: {} -> id_padre: {} -> valor: {}\n".format(hijo.id_nodo, hijo.id_padre, hijo.valor)
                recorrer_arbol(hijo)
            return self
        self.ret = 'RAIZ:\nroot-id: {} -> valor: {}\n\nHIJOS:\n'.format(self.id_nodo, self.valor)
        recorrer_arbol(self)
        return self.ret
