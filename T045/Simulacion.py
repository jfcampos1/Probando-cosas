__author__ = 'JuanFrancisco'

from random import randrange, choice

from PyQt4 import QtGui

from Ccalles import Vehiculo, Semaforo
from Cevento import Edificios, Eventos
from Leerarchivo import nuevo_mapa, cantidad_calles_lista


class Simulacion:
    def __init__(self, tiempo_maximo, tasa_llegada):
        self.tiempo_maximo_sim = tiempo_maximo
        self.tasa_llegada = tasa_llegada
        self.tiempo_simulacion = 0
        self.vehiculos_atendidos = 0

    def run(self):
        app = QtGui.QApplication([])
        lista_casas, mapa_calles, lista_vacios, lista_calle_entrada, lista_calle_salida, grilla, esquinas = nuevo_mapa(
            app)
        grilla.show()
        for z in lista_vacios:
            for j in lista_vacios:
                if z is not j:
                    for y in lista_vacios:
                        if y is not z and y is not j:
                            cantidad = 0
                            self.tiempo_simulacion = 0
                            Vehiculo.cantidad_autos = []
                            edificios = Edificios(z, j, y)
                            grilla.agregar_comisaria(edificios.comisaria[0], edificios.comisaria[1])
                            grilla.agregar_cuartel_bomberos(edificios.bomba[0], edificios.bomba[1])
                            grilla.agregar_hospital(edificios.clinica[0], edificios.clinica[1])
                            edificios.encontrar_calle(mapa_calles)
                            lista_casas[0].tiempo_inicio_eventos()
                            lista_casas[0].encontrar_calle(mapa_calles)
                            cantidad_calles, lista_calles = cantidad_calles_lista(mapa_calles)
                            cantidad_vehiculos_max = cantidad_calles // 2
                            entradas = len(lista_calle_entrada)
                            grilla.actualizar()
                            semaforos = Semaforo(self.tiempo_simulacion)
                            while cantidad != 50:
                                while self.tiempo_simulacion < self.tiempo_maximo_sim:
                                    grilla.tiempo_intervalo = self.tasa_llegada
                                    if cantidad_vehiculos_max > len(Vehiculo.cantidad_autos):
                                        p_taxi = randrange(10)
                                        rand = randrange(entradas)
                                        cordenadas = lista_calle_entrada[rand].cordenadas
                                        if lista_calle_entrada[rand].ocupado is False:
                                            if p_taxi < 2:
                                                grilla.agregar_taxi(cordenadas[0], cordenadas[1], 90, False)
                                                taxi = Vehiculo('taxi', self.tiempo_simulacion, cordenadas)
                                                Vehiculo.cantidad_autos.append(taxi)
                                                lista_calle_entrada[rand].ocupado = taxi
                                            else:
                                                tipo_auto = choice(['sedan', 'camioneta', 'convertible'])
                                                if tipo_auto == 'sedan':
                                                    grilla.agregar_sedan(cordenadas[0], cordenadas[1], 90, False)
                                                elif tipo_auto == 'camioneta':
                                                    grilla.agregar_pickup(cordenadas[0], cordenadas[1], 90, False)
                                                elif tipo_auto == 'convertible':
                                                    grilla.agregar_convertible(cordenadas[0], cordenadas[1], 90, False)
                                                auto2 = Vehiculo(tipo_auto, self.tiempo_simulacion, cordenadas)
                                                Vehiculo.cantidad_autos.append(auto2)
                                                lista_calle_entrada[rand].ocupado = auto2
                                    semaforos.cambiar_semaforo(self.tiempo_simulacion)
                                    for i in Eventos.evento:
                                        if i.tiempo_simulacion + i.tiempo >= self.tiempo_simulacion:
                                            if i.en_proceso is True:
                                                i.mover(mapa_calles, grilla)
                                            else:
                                                i.en_proceso = True
                                                i.crear_vehiculo(self.tiempo_simulacion, grilla)
                                                i.casa.cambiar_estado(grilla, i)
                                    for i in Vehiculo.cantidad_autos:
                                        if i.tiempo_llegada + i.velocidad < self.tiempo_simulacion:
                                            i.tiempo_llegada += i.velocidad
                                        elif i.tiempo_llegada + i.velocidad >= self.tiempo_simulacion:
                                            if i.tipo == 'taxi' and i.libre is True:
                                                if i.tiempo_libre >= self.tiempo_simulacion:
                                                    i.destino_taxi(mapa_calles, lista_calles, esquinas)
                                                calle = mapa_calles[i.cordenadas_vehiculo[0] - 1][
                                                    i.cordenadas_vehiculo[1] - 1]
                                                calle.siguiente_calle(mapa_calles, lista_calle_salida, grilla, i,
                                                                      esquinas, 2,
                                                                      self.tiempo_simulacion)
                                            elif i.tipo == 'taxi' and i.libre is False:
                                                pass
                                            else:
                                                calle = mapa_calles[i.cordenadas_vehiculo[0] - 1][
                                                    i.cordenadas_vehiculo[1] - 1]
                                                calle.siguiente_calle(mapa_calles, lista_calle_salida, grilla, i,
                                                                      esquinas, 2,
                                                                      self.tiempo_simulacion)
                                    grilla.actualizar()
                                    self.tiempo_simulacion += 0.5
                                cantidad += 1
                            grilla.quitar_imagen(edificios.comisaria[0], edificios.comisaria[1])
                            grilla.quitar_imagen(edificios.bomba[0], edificios.bomba[1])
                            grilla.quitar_imagen(edificios.clinica[0], edificios.clinica[1])
        app.exec_()


if __name__ == '__main__':
    tasa_llegada_vehiculos = 0.3
    s = Simulacion(100, tasa_llegada_vehiculos)
    s.run()
