__author__ = 'JuanFrancisco'


class Edificios:
    edificio = {}

    def __init__(self, ubi_clinica, ubi_comisaria, ubi_bomba):
        self.clinica = ubi_clinica
        self.calle_clinica = ''
        self.comisaria = ubi_comisaria
        self.calle_comisaria = ''
        self.bomba = ubi_bomba
        self.calle_bomba = ''
        Edificios.edificio = {'comisaria': [self.comisaria, self.calle_comisaria],
                              'clinica': [self.clinica, self.calle_clinica], 'bomba': [self.bomba, self.calle_bomba]}

    def encontrar_calle(self, mapa):
        orden = [self.clinica, self.comisaria, self.bomba]
        for i in range(3):
            fijar = orden[i]
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
            if i == 0:
                self.calle_clinica = opciones
                Edificios.edificio['clinica'] = [self.clinica, self.calle_clinica]
            elif i == 1:
                self.calle_comisaria = opciones
                Edificios.edificio['comisaria'] = [self.comisaria, self.calle_comisaria]
            else:
                self.calle_bomba = opciones
                Edificios.edificio['bomba'] = [self.bomba, self.calle_bomba]
