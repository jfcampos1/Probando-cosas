__author__ = 'JuanFrancisco'
# coding=utf-8
import copy


class Arbol:
    def __init__(self, id_nodo, nombre=None, valor=None, id_padre=None):
        self.id_nodo = id_nodo
        self.id_padre = id_padre
        self.valor = valor
        self.nombre = nombre
        self.hijos = {}

    def agregar_nodo(self, id_nodo, nombre, valor=None, id_padre=None):
        if self.id_nodo == id_padre:
            # Si el nodo es el nodo padre, entonces actualizamos el diccionario con los hijos
            self.hijos.update({id_nodo: Arbol(id_nodo, nombre, valor, id_padre)})
        else:
            for hijo in self.hijos.values():
                hijo.agregar_nodo(id_nodo, nombre, valor, id_padre)

    def borrar_nodo(self, id_padre, id_nodo):
        if self.id_nodo == id_padre:
            del self.hijos[id_nodo]
        else:
            for hijo in self.hijos.values():
                hijo.borrar_nodo(id_padre, id_nodo)

    def obtener_nodo(self, id_nodo):
        if self.id_nodo == id_nodo:
            return self
        else:
            for hijo in self.hijos.values():
                nodo = hijo.obtener_nodo(id_nodo)
                if nodo:
                    return nodo

    def obtener_nodo_nombre(self, nombre):
        if self.nombre == nombre:
            return self
        else:
            for hijo in self.hijos.values():
                nodo = hijo.obtener_nodo_nombre(nombre)
                if nodo:
                    return nodo

    def obtener_donde_no_esta_nodo(self, nombre):
        if self.nombre != nombre and nombre not in self.hijos:
            return self
        else:
            for hijo in self.hijos.values():
                nodo = hijo.obtener_nodo_nombre(nombre)
                if nodo:
                    return nodo

    def sacar_nodo(self, nodo):
        nodo_padre = self.obtener_nodo(nodo.id_padre)
        aux = copy.copy(nodo)
        del nodo_padre.hijos[nodo.id_nodo]
        return aux

    def agregando_a_arbol(self, arbol, path):
        id_padre = path
        id_nodo = path + '/' + self.nombre
        arbol.agregar_nodo(id_nodo=id_nodo, valor=self.valor, id_padre=id_padre, nombre=self.nombre)
        for i in self.hijos.values():
            i.agregando_a_arbol(arbol, id_nodo)

    def __repr__(self):
        # Para visualizar el arbol redefinimos el método __repr__ para recorrer recursivamente todos los nodos del árbol
        def recorrer_arbol(raiz):
            for hijo in raiz.hijos.values():
                self.ret += "id-nodo: {} -> id_padre: {} -> valor: {}\n".format(hijo.id_nodo, hijo.id_padre, hijo.valor)
                recorrer_arbol(hijo)
            return self

        self.ret = 'RAIZ:\nroot-id: {} -> valor: {}\n\nHIJOS:\n'.format(self.id_nodo, self.valor)
        recorrer_arbol(self)
        return self.ret
