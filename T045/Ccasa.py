__author__ = 'JuanFrancisco'
from random import expovariate,randint,uniform,randrange
from Cedificio import Edificios
from Cevento import Eventos

class Casa:
    materiales_peso = {'madera': 10, 'ladrillos': 7, 'hormigon': 4, 'metal': 2}
    materiales_tiempo_apagar = {'madera': [1800, 7200], 'ladrillos': [2400, 6000], 'hormigon': [3600, 4800],
                                'metal': [1800, 2400]}
    todas_casas = []

    def __init__(self, material, tiempo_robo, cordenadas):
        self.material = material
        self.peso = Casa.materiales_peso[material]
        self.tiempo_apagar = Casa.materiales_tiempo_apagar[material]
        self.tiempo_robo = tiempo_robo
        self.cordenadas = cordenadas
        self.calles_casa = []
        Casa.todas_casas.append(self)

    def encontrar_calle(self, mapa):
        orden = Casa.todas_casas
        for i in range(len(orden)):
            fijar = orden[i].cordenadas
            opciones = []
            if fijar[0] - 2 >= 0:
                if mapa[fijar[0] - 2][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0] - 2][fijar[1] - 1])
            if fijar[0] < len(mapa):
                if mapa[fijar[0]][fijar[1] - 1] != '':
                    opciones.append(mapa[fijar[0]][fijar[1] - 1])
            if fijar[1] - 2 >= 0:
                if mapa[fijar[0] - 1][fijar[1] - 2] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1] - 2])
            if fijar[1] < len(mapa[0]):
                if mapa[fijar[0] - 1][fijar[1]] != '':
                    opciones.append(mapa[fijar[0] - 1][fijar[1]])
            orden[i].calles_casa = opciones

    def proximo_robo(self, comisaria):
        cantidad_casas = len(Casa.todas_casas)
        todos_pesos = []
        for i in range(cantidad_casas):
            peso = 10 + abs(Casa.todas_casas[i].cordenadas[0] - comisaria[0]) + abs(
                Casa.todas_casas[i].cordenadas[1] - comisaria[1])
            todos_pesos.append(peso)
        suma_pesos = 0
        for i in todos_pesos:
            suma_pesos += i
        numero = randint(11, suma_pesos)
        casa = ''
        cont = 0
        for i in range(cantidad_casas):
            if numero - todos_pesos[i] < 0 and cont == 0:
                cont = 1
                casa = i
            else:
                numero -= todos_pesos[i]
        casa_robada = Casa.todas_casas[casa]
        return casa_robada

    def proximo_incendio(self):
        cantidad_casas = len(Casa.todas_casas)
        todos_pesos = 0
        for i in Casa.todas_casas:
            todos_pesos += i.peso
        probabilidad_todas = []
        for i in Casa.todas_casas:
            prob = i.peso / todos_pesos
            probabilidad_todas.append(prob)
        base = 2 / todos_pesos
        numero = uniform(base, 1)
        cont = 0
        casa = ''
        for i in range(cantidad_casas):
            if numero - probabilidad_todas[i] < 0 and cont == 0:
                cont = 1
                casa = i
            else:
                numero -= probabilidad_todas[i]
        casa_quemada = Casa.todas_casas[casa]
        return casa_quemada

    def proximo_enfermo(self):
        numero = randrange(len(Casa.todas_casas))
        casa_enfermo = Casa.todas_casas[numero]
        return casa_enfermo

    def tiempo_inicio_eventos(self):
        incendio = expovariate(1 / 10) * 3600
        robo = expovariate(1 / 4) * 3600
        enfermo = expovariate(1 / 2) * 3600
        casa_incendio = self.proximo_incendio()
        patrulla = Edificios.edificio['comisaria']
        casa_robo = self.proximo_robo(patrulla[0])
        casa_enfermo = self.proximo_enfermo()
        nuevo = Eventos('incendio', incendio, casa_incendio, 0)
        nuevo2 = Eventos('robo', robo, casa_robo, 0)
        nuevo3 = Eventos('enfermo', enfermo, casa_enfermo, 0)

    def cambiar_estado(self, grilla, evento):
        if evento.evento == 'enfermo':
            grilla.agregar_enfermo(self.cordenadas[0], self.cordenadas[1])
        elif evento.evento == 'robo':
            grilla.agregar_robo(self.cordenadas[0], self.cordenadas[1])
        elif evento.evento == 'incendio':
            grilla.agregar_incendio(self.cordenadas[0], self.cordenadas[1])

