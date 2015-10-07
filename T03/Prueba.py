__author__ = 'JuanFrancisco'
agua = [1, 2]
a = 0
print(chr(a+65))

print(agua[3])




class Vuelo():
    def __init__(self, numero, origen, destino, horario, filas, columnas):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.filas = filas
        self.columnas = columnas
        self.asientos = []
        # creacion de asientos
        for i in range(filas):
            self.asientos.append([])
            for j in range(columnas):
                self.asientos[i].append(False)

    def reservar_asiento(self, fila, columa):
        self.asientos[fila - 1][columa - 1] = True

    def asiento_reservado(self, fila, columna):
        return self.asientos[fila - 1][columna - 1]

    def obtener_informacion(self):
        return self.numero + " " + self.origen + " - " + self.destino + ", " + self.horario

    def asientos_disponibles(self):
        disponibles = 0
        for filas in self.asientos:
            for asiento in filas:
                if not asiento:
                    disponibles += 1
        return disponibles

    def mostrar_vuelo(self):
        # Imprimir cabecera
        fila = " \n "
        for c in range(self.columnas):
            fila += " " + chr(65 + c)
        print(fila)
        # Imprimir el resto
        for f in range(self.filas):
            fila = str(f + 1)
            for c in range(self.columnas):
                if self.asientos[f][c]:
                    fila += " X "
                else:
                    fila += " D "
            print(fila)
        print(" ")
        # Programa principal


# vuelos = []
# cerrar = False
# while not cerrar:
#     print(" \nBienvenido a Camino al Cielo Airline ")
#     print(" [1] Crear un nuevo vuelo ")
#     print(" [2] Reserva de pasajes ")
#     print(" [3] Salir del Sistema ")
#     opcion = input(" ")
#     if opcion == "1":
#         numero = input(" Ingrese el numero de vuelo : ")
#         origen = input(" Ingrese la ciudad de origen : ")
#         destino = input(" Ingrese la ciudad de destino : ")
#         horario = input(" Ingrese el horario : ")
#         filas = input(" Ingrese la cantidad de filas : ")
#         columnas = input(" Ingrse la cantidad de asientos por fila : ")
#         vuelo = Vuelo(numero, origen, destino, horario, int(filas), int(columnas))
#         vuelos.append(vuelo)
#     elif opcion == "2":
#         if len(vuelos) == 0:
#             print(" No existen vuelos disponibles ")
#         else:
#             print(" Selecciona el vuelo ")
#             for i in range(len(vuelos)):
#                 print(" [ " + str(i + 1) + " ] " + vuelos[i].obtener_informacion())
#             nro_vuelo = int(input(" "))
#             vuelo = vuelos[nro_vuelo - 1]
#             if vuelo.asientos_disponibles == 0:
#                 print(" No quedan asientos disponibles en el vuelo ")
#             else:
#                 vuelo.mostrar_vuelo()
#                 reserva = False
#                 while not reserva:
#                     fila = int(input(" Selecciona la fila : "))
#                     columna = ord(input(" Selecciona la columna : ")) - 64
#                     if not vuelo.asiento_reservado(fila, columna):
#                         vuelo.reservar_asiento(fila, columna)
#                         print(" Asiento reservado correctamente ")
#                         reserva = True
#                     else:
#                         print(" Este asiento ya esta reservado , por favor seleccione otro ")
#     else:
#         cerrar = True
