__author__ = 'JuanFrancisco'


class Calle:
    def __init__(self, direccion, cordenadas):
        self.direccion = direccion
        self.cordenadas = cordenadas
        self.ocupado = None


class Casa:
    materiales_peso = {'madera': 10, 'ladrillos': 7, 'hormigon': 4, 'metal': 2}
    materiales_tiempo_apagar = {'madera': [30, 120], 'ladrillos': [40, 100], 'hormigon': [60, 80], 'metal': [30, 40]}

    def __init__(self, material, tiempo_robo, cordenadas):
        self.peso = Casa.materiales_peso[material]
        self.tiempo_apagar = Casa.materiales_tiempo_apagar[material]
        self.tiempo_robo = tiempo_robo
        self.cordenadas = cordenadas
