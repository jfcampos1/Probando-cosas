# coding=utf-8
import socket
import threading
import time
import os
import sys


class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.historia = ""
        self.turno = True
        self.turno2=True
        try:
            self.s_cliente.connect((self.host, self.port))
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
            print('Es su turno')
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while True:
            self.turno = True
            data = self.s_cliente.recv(1024)
            palabras = data.decode('utf-8')
            if palabras == "True":
                print("Ganaste")
            else:
                print(palabras)
                self.turno2=False
                time.sleep(5)
                os.system("cls")
                print('Es su turno')
                self.turno2=True

    def enviar(self, mensaje):
        mensaje=mensaje.lower()
        palabra = mensaje.split(" ")
        historia = self.historia.split(" ")
        if self.turno and self.turno2:
            if (len(palabra) != len(historia) + 3
                    or historia != palabra[:-3]) and historia!=[''] :
                self.historia=mensaje
                print("Perdiste")
                self.s_cliente.send("True".encode("utf-8"))
            else:
                self.s_cliente.send(mensaje.encode("utf-8"))
                print('Mensaje enviado correctamente espere su turno')
            self.turno = False
        else:
            print("Aun no es tu turno")


class Servidor:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1)
        self.cliente = None
        self.aceptar()
        self.historia = ""
        self.turno = False
        self.turno2=False
        print('Espere su turno')

    def recibir_mensajes(self):
        while True:
            self.turno = True
            data = self.cliente.recv(1024)
            palabras = data.decode('utf-8')
            if palabras == "True":
                print("Ganaste")
            else:
                print(palabras)
                self.turno2=False
                time.sleep(5)
                os.system("cls")
                print('Es su turno')
                self.turno2=True

    def enviar(self, mensaje):
        mensaje=mensaje.lower()
        palabra = mensaje.split(" ")
        historia = self.historia.split(" ")
        if self.turno and self.turno2:
            if (len(palabra) != len(historia) + 3
                    or historia != palabra[:-3]) and historia!=[''] :
                self.historia=mensaje
                print("Perdiste")
                self.cliente.send("True".encode("utf-8"))
            else:
                self.cliente.send(mensaje.encode("utf-8"))
            self.turno = False
            print('Mensaje enviado espere su turno')
        else:
            print("Aun no es tu turno")

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(
            target=self.recibir_mensajes, args=())
        thread_cliente.daemon = True
        thread_cliente.start()


if __name__ == "__main__":

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        while True:
            texto = input()
            server.enviar(texto)

    elif pick == "C":
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        while True:
            texto = input()
            client.enviar(texto)