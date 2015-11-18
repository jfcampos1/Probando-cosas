import socket
import threading
import sys



class Servidor:

    def __init__(self, usuario, num_clients=1):
        self.usuario = usuario
        self.host = socket.gethostname()
        self.port = 3491
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(num_clients)
        self.clientes = []
        self.connection = True
        self.dic_clientes={}

        # No hacemos self.aceptar()

        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        thread_aceptar.daemon = True
        thread_aceptar.start()

    def recibir_mensajes(self, cliente):
        while self.connection:
            data = cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if cliente in self.clientes:
                if mensaje.split(': ')[1] == 'quit':
                    self.clientes.remove(cliente)
                print(mensaje)
                print('conectado')
            else:
                self.dic_clientes[cliente]=True
                print('Primera coneccion')

    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            print(address)
            self.clientes.append(cliente_nuevo)
            self.cliente=[cliente_nuevo, False]
            thread_mensajes = threading.Thread(target=self.identificar, args=(self.cliente,))
            thread_mensajes.daemon = True
            thread_mensajes.start()
            self.enviar('-1,ingresa usuario y clave separados por dos puntos:')

    def identificar(self,cliente):
        while cliente[1] is False:
            while self.connection and cliente[1] is False:
                data = cliente[0].recv(1024)
                mensaje = data.decode('utf-8')
                if mensaje.split(': ')[1] == 'quit':
                    self.clientes.remove(cliente)
                else:
                    s_cliente,codigo,usuario,clave=mensaje.split(':')
                    if codigo == ' 005':
                        print('aqui')
                        if usuario in self.dic_clientes:
                            if self.dic_clientes[usuario]==clave:
                                cliente[1]=True
                                print('clave correcta')
                                thread_mensajes = threading.Thread(target=self.recibir_mensajes, args=(cliente[0],))
                                thread_mensajes.daemon = True
                                thread_mensajes.start()
                                self.enviar('-1,002')
                            else:
                                self.enviar('-1,001')
                                print('clave incorrecta')
                        else:
                            self.enviar('-1,001')
                    elif codigo == ' 003':
                        print('Creando')
                        if usuario in self.dic_clientes:
                            self.enviar('-1,004')
                        else:
                            self.dic_clientes[usuario] = clave
                            self.enviar('-1,006')


    def enviar(self, mensaje):
        c, mensaje = mensaje.split(',')
        msj_final = self.usuario + ": " + mensaje
        self.clientes[int(c)].send(msj_final.encode('utf-8'))

    def desconectar(self):
        for i in range(len(self.clientes)):
            self.enviar(str(i) + ',quit')
        self.connection = False
        self.s_servidor.close()



if __name__ == "__main__":
    nombre = 'Server'
    server = Servidor(nombre, num_clients=2)
    while server.connection:
        texto = input()
        if texto == 'quit':
            server.desconectar()
        else:
            server.enviar(texto)
