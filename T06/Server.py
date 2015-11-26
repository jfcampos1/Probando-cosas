import socket
import threading
import hashlib
import uuid
import pickle

from serializar import crear_persona, get_persona, existe_persona, make_dir, write_persona


class Servidor:
    def __init__(self, num_clients=1):
        self.usuario = 'Server'
        self.host = socket.gethostname()
        self.port = 3491
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(num_clients)
        self.clientes = []
        self.connection = True

        # No hacemos self.aceptar()

        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        thread_aceptar.daemon = True
        thread_aceptar.start()

    def recibir_mensajes(self, cliente):
        salir = True
        while self.connection and salir is True:
            print('En recibir mensajes')
            data = cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.clientes.remove(cliente)
                salir = False
            else:
                posicion = self.clientes.index(cliente)
                s_cliente, codigo, largo = mensaje.split(':')
                if codigo == ' 009':
                    data = b''
                    l = int(largo)
                    while l > 0:
                        d = cliente.recv(l)
                        l -= len(d)
                        data += d
                    mensaje = pickle.loads(data)
                    client, codigo, archivo = mensaje
                    persona = get_persona(client, 'Servidor')
                    archi = persona.archivos
                    camino=persona.camino_archivos
                    print(archi)
                    print(archi.id_nodo)
                    nuevo_id = get_persona('contadorid', 'Servidor')
                    ultimo_numero=nuevo_id.cant_guardado
                    archi.agregar_nodo(nuevo_id.cant_guardado,archivo.nombre,valor=archivo, id_padre=archi.id_nodo)
                    camino.agregar_nodo(nuevo_id.cant_guardado,archivo.nombre,valor='012', id_padre=archi.id_nodo)
                    write_persona(persona,'Servidor')
                    write_persona(nuevo_id, 'Servidor')
                    print('nuevo archivo')
                    # probar que mande archivo de vuelta
                    persona1 = get_persona(client, 'Servidor')
                    print(persona1)
                    print(persona1.archivos)
                    archivo=persona1.archivos.obtener_nodo(ultimo_numero)
                    print(archivo)
                    msj_final = [self.usuario, '010', archivo]
                    pick = pickle.dumps(msj_final)
                    c = self.clientes.index(cliente)
                    print(c)
                    self.clientes[int(c)].sendall('{}: 010:{}'.format(self.usuario, str(len(pick))).encode('utf-8'))
                    self.clientes[int(c)].sendall(pick)
                    print('{}: 010:{}'.format(self.usuario, len(pick)))
                elif codigo==' 011':
                    pass
            print(mensaje)
            print('conectado')

    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            print(address)
            self.clientes.append(cliente_nuevo)
            self.cliente = [cliente_nuevo, False]
            thread_mensajes = threading.Thread(target=self.identificar, args=(self.cliente,))
            thread_mensajes.daemon = True
            thread_mensajes.start()

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
                                persona=get_persona(usuario,'Servidor')
                                camino=persona.camino_archivos
                                msj_final = [self.usuario, '014', camino]
                                pick = pickle.dumps(msj_final)
                                c = self.clientes.index(cliente[0])
                                print(c)
                                mandar=self.clientes[int(c)]
                                self.clientes[int(c)].sendall('{}: 014:{}'.format(self.usuario, str(len(pick))).encode('utf-8'))
                                self.clientes[int(c)].sendall(pick)
                                self.enviar(cliente[0],'002: {}'.format(usuario))
                            else:
                                self.enviar(cliente[0],'001')
                                print('clave incorrecta')
                        else:
                            self.enviar(cliente[0],'001')
                    elif codigo == ' 003':
                        print('Creando')
                        if existe_persona(usuario, 'Servidor'):
                            self.enviar(cliente[0],'004')
                        else:
                            salt = uuid.uuid4().hex
                            # salt = str(os.urandom(16))
                            clave_encriptada = hashlib.sha256(salt.encode() + clave.encode()).hexdigest() + ':' + salt
                            crear_persona(usuario, usuario, clave_encriptada, 'Servidor')
                            self.enviar(cliente[0],'006')
        print('Acaa')

    def enviar(self, cliente,mensaje):
        c = self.clientes.index(cliente)
        msj_final = self.usuario + ": " + mensaje
        self.clientes[int(c)].sendall(msj_final.encode('utf-8'))

    def desconectar(self):
        for i in range(len(self.clientes)):
            self.enviar(self.clientes[i] , 'quit')
        self.connection = False
        self.s_servidor.close()


if __name__ == "__main__":
    make_dir('Servidor')
    server = Servidor(num_clients=2)
    while server.connection:
        texto = input()
        if texto == 'quit':
            server.desconectar()
        else:
            server.enviar(texto)
