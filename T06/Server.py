import socket
import threading
import hashlib
import uuid
import pickle
import time

from serializar import crear_persona, get_persona, existe_persona, make_dir, write_persona


class Servidor:
    def __init__(self, num_clients=5):
        self.usuario = 'Server'
        self.host = '127.0.0.1'
        print(self.host)
        self.port = 3491
        self.port2=3492
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(num_clients)
        self.s_servidor2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor2.bind((self.host, self.port2))
        self.s_servidor2.listen(num_clients)
        self.clientes2=[]
        self.clientes = []
        self.conectados=[]
        self.connection = True
        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        thread_aceptar.daemon = True
        thread_aceptar.start()
        thread_aceptar2 = threading.Thread(target=self.aceptar2, args=())
        thread_aceptar2.daemon = True
        thread_aceptar2.start()

    def recibir_mensajes(self, cliente):
        salir = True
        while self.connection and salir is True:
            print('En recibir mensajes')
            data = cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.clientes.remove(cliente)
                self.conectados.remove(mensaje.split(': ')[0])
                self.enviar_a_todos()
                salir = False
            else:
                s_cliente, codigo, largo = mensaje.split(':')
                if codigo == ' 009':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = cliente.recv(l)
                        l -= len(d)
                        data += d
                    mensaje = pickle.loads(data)
                    self.crear_archivo(cliente, mensaje)

                elif codigo == ' 011':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = cliente.recv(l)
                        l -= len(d)
                        data += d
                    mensaje = pickle.loads(data)
                    self.crear_carpeta(cliente, mensaje)
                elif codigo == ' 015':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = cliente.recv(l)
                        l -= len(d)
                        data += d
                    mensaje = data.decode('utf-8')
                    idnodo, path = mensaje.split(',')
                    c = self.clientes.index(cliente)
                    persona1 = get_persona(s_cliente, 'Servidor')
                    print('aqui buscando nodo')
                    archivo = persona1.archivos.obtener_nodo(int(idnodo))
                    print(archivo)
                    msj_final = [self.usuario, '010', path, archivo.valor]
                    pick = pickle.dumps(msj_final)
                    print(c)
                    self.clientes[int(c)].sendall('{}: 010:{}'.format(self.usuario, str(len(pick))).encode('utf-8'))
                    self.clientes[int(c)].sendall(pick)
                    print('{}: 010:{}'.format(self.usuario, len(pick)))
                elif codigo == ' 016':
                    persona1 = get_persona(s_cliente, 'Servidor')
                    try:
                        largo=int(largo)
                    except:
                        pass
                    if type(largo) == type(str()):
                        padre2 = persona1.archivos.obtener_nodo_nombre(largo)
                    else:
                        padre2 =  persona1.archivos.obtener_nodo(int(largo))
                    self.borrar_archivo(persona1,padre2,cliente,s_cliente)
                    print('s_cliente',s_cliente)
            print(mensaje)
            print('conectado')

    def recibir_mensajes2(self, cliente):
        salir = True
        while self.connection and salir is True:
            print('En recibir mensajes')
            data = cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.clientes.remove(cliente)
                self.conectados.remove(mensaje.split(': ')[0])
                self.enviar_a_todos()
                salir = False
            else:
                s_cliente, s_a ,codigo, largo = mensaje.split(':')
                cenviar=self.conectados.index(s_a)
                if codigo == '019':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = cliente.recv(l)
                        l -= len(d)
                        data += d
                    self.clientes2[cenviar].sendall('{}:{}:019:{}'.format(s_cliente, str(len(data))).encode('utf-8'))
                    self.clientes2[cenviar].sendall(data)
                else:
                    self.clientes2[cenviar].sendall(mensaje.encode('utf-8'))

            print(mensaje)
            print('conectado')

    def crear_archivo(self, cliente, mensaje):
        client, padre, codigo, archivo = mensaje
        persona = get_persona(client, 'Servidor')
        archi = persona.archivos
        camino = persona.camino_archivos
        print('Creando archivo')
        print(archivo.nombre)
        print(padre, type(padre))
        padre2 = None
        if type(padre) == type(str()):
            padre = persona.archivos.obtener_nodo_nombre(padre)
            print('Este es el padre', padre)
            padre2 = padre.id_nodo
        else:
            padre2 = padre
        print(archi)
        print(archi.id_nodo)
        nuevo_id = get_persona('contadorid', 'Servidor')
        archi.agregar_nodo(nuevo_id.cant_guardado, archivo.nombre, valor=archivo, id_padre=padre2)
        camino.agregar_nodo(nuevo_id.cant_guardado, archivo.nombre, valor='012', id_padre=padre2)
        write_persona(persona, 'Servidor')
        write_persona(nuevo_id, 'Servidor')
        print('nuevo archivo')
        self.actualizar_layout(cliente,client)

    def borrar_archivo(self,persona,idnodo,cliente,client):
        nodo=idnodo
        nodopadre=persona.archivos.obtener_nodo(nodo.id_padre)
        nodocamino=persona.camino_archivos.obtener_nodo(nodo.id_padre)
        print('Borrando:',nodopadre.hijos[nodo.id_nodo])
        del nodopadre.hijos[nodo.id_nodo]
        del nodocamino.hijos[nodo.id_nodo]
        write_persona(persona, 'Servidor')
        self.actualizar_layout(cliente,client)

    def actualizar_layout(self,cliente,client):
        c = self.clientes.index(cliente)
        print(c)
        persona1 = get_persona(client, 'Servidor')
        camino1 = persona1.camino_archivos
        msj_final2 = [self.usuario, '014', camino1]
        pick2 = pickle.dumps(msj_final2)
        self.clientes[int(c)].sendall('{}: 014:{}'.format(self.usuario, str(len(pick2))).encode('utf-8'))
        self.clientes[int(c)].sendall(pick2)

    def crear_carpeta(self, cliente, mensaje):
        client, padre, codigo, archivo = mensaje
        persona = get_persona(client, 'Servidor')
        archi = persona.archivos
        camino = persona.camino_archivos
        print(type(padre))
        padre2 = None
        if type(padre) == type(str()):
            padre = persona.archivos.obtener_nodo_nombre(padre)
            print('Este es el padre', padre)
            padre2 = padre.id_nodo
        else:
            padre2 = padre
        print('Creando Carpeta')
        print(archivo.nombre)
        nuevo_id = get_persona('contadorid', 'Servidor')
        archi.agregar_nodo(nuevo_id.cant_guardado, archivo.nombre, valor=None, id_padre=padre2)
        camino.agregar_nodo(nuevo_id.cant_guardado, archivo.nombre, valor='013', id_padre=padre2)
        write_persona(persona, 'Servidor')
        write_persona(nuevo_id, 'Servidor')
        print('nuevo archivo')
        self.actualizar_layout(cliente,client)

    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            print(address)
            self.clientes.append(cliente_nuevo)
            self.cliente = [cliente_nuevo, False]
            thread_mensajes = threading.Thread(target=self.identificar, args=(self.cliente,))
            thread_mensajes.daemon = True
            thread_mensajes.start()

    def aceptar2(self):
        while True:
            cliente_nuevo, address = self.s_servidor2.accept()
            self.clientes2.append(cliente_nuevo)

    def identificar(self, cliente):
        while cliente[1] is False:
            while self.connection and cliente[1] is False:
                data = cliente[0].recv(1024)
                mensaje = data.decode('utf-8')
                if mensaje.split(': ')[1] == 'quit':
                    self.clientes.remove(cliente[0])
                    cliente[1] = True
                else:
                    s_cliente, codigo, usuario, clave = mensaje.split(':')
                    if codigo == ' 005':
                        print('aqui')
                        if existe_persona(usuario, 'Servidor'):
                            persona = get_persona(usuario, 'Servidor')
                            password, salt = persona.clave.split(':')
                            if password == hashlib.sha256(salt.encode() + clave.encode()).hexdigest():
                                cliente[1] = True
                                print('clave correcta')
                                thread_mensajes = threading.Thread(target=self.recibir_mensajes, args=(cliente[0],))
                                thread_mensajes.daemon = True
                                thread_mensajes.start()
                                persona = get_persona(usuario, 'Servidor')
                                camino = persona.camino_archivos
                                msj_final = [self.usuario, '014', camino]
                                pick = pickle.dumps(msj_final)
                                c = self.clientes.index(cliente[0])
                                print(c)
                                self.clientes[int(c)].sendall(
                                    '{}: 014:{}'.format(self.usuario, str(len(pick))).encode('utf-8'))
                                self.clientes[int(c)].sendall(pick)
                                self.enviar(cliente[0], '002: {}'.format(usuario))
                                self.conectados.append(usuario)
                                self.enviar_a_todos()
                            else:
                                self.enviar(cliente[0], '001')
                                print('clave incorrecta')
                        else:
                            self.enviar(cliente[0], '001')
                    elif codigo == ' 003':
                        print('Creando')
                        if existe_persona(usuario, 'Servidor'):
                            self.enviar(cliente[0], '004')
                        else:
                            salt = uuid.uuid4().hex
                            # salt = str(os.urandom(16))
                            clave_encriptada = hashlib.sha256(salt.encode() + clave.encode()).hexdigest() + ':' + salt
                            crear_persona(usuario, usuario, clave_encriptada, 'Servidor')
                            self.enviar(cliente[0], '006')
        print('Acaa')

    def enviar_a_todos(self):
        for i in range(len(self.conectados)):
            time.sleep(3)
            pick=pickle.dumps(self.conectados)
            self.clientes[i].sendall('{}: 017:{}'.format(self.usuario,len(pick)).encode('utf-8'))
            self.clientes[i].sendall(pick)

    def enviar(self, cliente, mensaje):
        c = self.clientes.index(cliente)
        msj_final = self.usuario + ": " + mensaje
        self.clientes[int(c)].sendall(msj_final.encode('utf-8'))

    def desconectar(self):
        for i in range(len(self.clientes)):
            self.enviar(self.clientes[i], 'quit')
        self.connection = False
        self.s_servidor.close()
        self.s_servidor2.close()


if __name__ == "__main__":
    make_dir('Servidor')
    server = Servidor(num_clients=2)
    while server.connection:
        texto = input()
        if texto == 'quit':
            server.desconectar()
        else:
            server.enviar(texto)
