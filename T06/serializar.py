__author__ = 'JuanFrancisco'
# coding=utf-8
import os
import pickle
from datetime import datetime

from Arbol import Arbol


class Persona:
    def __init__(self, id, nombre, clave):
        self.nombre = nombre
        self.id = id
        contador = get_persona('contadorid')
        print(contador.cant_guardado)
        self.archivos = Arbol(contador.cant_guardado)
        write_persona(contador)
        self.persona_favorita = ''
        self.cant_guardado = 0
        self.clave = clave

    def __getstate__(self):  # retorna el estado actual del objeto, para que sea serializado por pickle
        self.cant_guardado += 1
        nueva = self.__dict__.copy()  # aquí creamos una copia del diccionario actual, para modificar la copia y no el objeto original
        ahora = datetime.now()
        nueva.update({"fecha": (ahora.day, ahora.month, ahora.year)})
        nueva.update({"hora": (ahora.hour, ahora.minute, ahora.second)})
        return nueva


def existe_persona(_id):
    lista = os.listdir('Servidor')
    for i in lista:
        if _id + '.drop' == i:
            return True
    return False


def get_persona(_id):
    if existe_persona(_id):
        lista = os.listdir('Servidor')
        for i in lista:
            if _id + '.drop' == i:
                with open("Servidor/{}".format(i), 'rb') as file:
                    mi_persona = pickle.load(file)
                    return mi_persona


def write_persona(persona):
    person = persona
    id = person.id
    with open("Servidor/{}.drop".format(id), 'wb') as file:
        pickle.dump(person, file)


def crear_persona(_id, nombre_completo, clave):
    if not existe_persona(_id):
        person = Persona(_id, nombre_completo, clave)
        write_persona(person)


def agregar_amigo(id_1, id_2):
    if existe_persona(id_1) and existe_persona(id_2):
        id1 = get_persona(id_1)
        id2 = get_persona(id_2)
        if id_2 not in id1.amigos and id_1 not in id2.amigos:
            id1.amigos.append(id_2)
            id2.amigos.append(id_1)
            write_persona(id1)
            write_persona(id2)


def set_persona_favorita(_id, id_favorito):
    if existe_persona(_id) and existe_persona(id_favorito):
        id1 = get_persona(_id)
        id1.persona_favorita = id_favorito
        write_persona(id1)


def get_persona_mas_favorita():
    lista_favoritos = []
    lista = os.listdir('Servidor')
    for i in lista:
        id = i.split('.')
        id = id[0]
        persona = get_persona(id)
        persona = persona.persona_favorita
        for n in lista_favoritos:
            if persona in n[0]:
                n[1] += 1
            else:
                list = [persona, 1]
                lista_favoritos.append(list)
        if len(lista_favoritos) == 0:
            list = [persona, 1]
            lista_favoritos.append(list)
    a = 0
    id = ''
    for i in lista_favoritos:
        if i[1] > a:
            a = i[1]
            id = i[0]
    nombre1 = get_persona(id)
    nombre = nombre1.nombre
    return (nombre, a)


# ----------------------------------------------------- #
# Codigo para probar su tarea - No necesitan entenderlo #


def print_data(persona):
    if persona is None:
        print("[AVISO]: get_persona no está implementado")
        return

    for key, val in persona.__dict__.items():
        print("{} : {}".format(key, val))
    print("-" * 80)


# Metodo que sirve para crear el directorio Servidor si no existia #

def make_dir():
    if not os.path.exists("./Servidor"):
        os.makedirs("./Servidor")
        crear_persona("contadorid", "server", '')


    # if __name__ == '__main__':
    #     make_dir()
    # crear_persona("jecastro1", "Jaime Castro")
    # crear_persona("bcsaldias", "Belen Saldias")
    # crear_persona("kpb", "Karim Pichara")
    # set_persona_favorita("jecastro1", "bcsaldias")
    # set_persona_favorita("bcsaldias", "kpb")
    # set_persona_favorita("kpb", "kpb")
    # agregar_amigo("kpb", "jecastro1")
    # agregar_amigo("kpb", "bcsaldias")
    # agregar_amigo("jecastro1", "bcsaldias")
    #
    # jecastro1 = get_persona("jecastro1")
    # bcsaldias = get_persona("bcsaldias")
    # kpb = get_persona("kpb")
    #
    # print_data(jecastro1)
    # print_data(bcsaldias)
    # print_data(kpb)
    #
    # print(get_persona_mas_favorita())
