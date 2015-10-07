__author__ = 'JuanFrancisco'


class Armas:
    def __init__(self, lista):
        self.nombre = lista[0]
        self.sobrenombre = lista[1]
        self.dano = lista[2]
        self.area = lista[3]
        self.disponibilidad = lista[4]
        self.turno_desactivado = None
        self.inutil = False
        self.cordenadas_napalm = []


class Vehiculo:
    def __init__(self, pieza, agua, area_ocu, resistencia, ataques):
        self.pieza = pieza
        self.area = area_ocu
        self.resistencia = resistencia
        self.max_resistencia = resistencia
        self.ataques = ataques
        self.barco = agua
        self.activo = True
        self.habilitado = 0
        self.dano_total = 0

    def recibir_dano(self, arma):
        self.resistencia -= arma.dano
        self.dano_total += arma.dano
        if self.resistencia <= 0:
            self.activo = False
            return True
        return False

    def reparar(self):
        if self.resistencia < self.max_resistencia:
            self.resistencia += 1
            return True
        else:
            print('No puedes exceder el max de resistencia')
            return False

    def mostrar_ataques(self):
        orden = []
        a = 1
        for i in range(len(self.ataques)):
            if self.ataques[i].inutil is False:
                r = '[' + str(a) + '] ' + self.ataques[i].nombre
                print(r)
                orden2 = [a, i]
                orden.append(orden2)
                a += 1
        return orden


class CrearVehiculos:
    def __init__(self, nombre):
        self.vehiculos = []
        self.nombre_jugador = nombre
        self.ataque_exitosos = 0
        self.ataques_exitosos_tipo = {}  # sumar afuera
        self.dano_causado = 0
        self.dano_recibido = 0  # esta en el vehculo sumarlos
        self.ataque_ocupado = {}
        self.movimientos = {}  # sumar afuera
        self.numero_ataques = 0

    def crear(self):
        todas_armas = [['Misil UGM-133 Trident II', 'Trident II', 5, [1, 1], 'Siempre'],
                       ['Misil de crucero BGM-109 Tomahawk', 'Tomahawk', 5, [1, 'n'], 3],
                       ['Napalm', 'Napalm', 5, [1, 1], 8],
                       ['Misil Balistico Intercontinental Minuteman III', 'Minuteman III', 15, [1, 1], 3],
                       ['Kamikaze', 'Kamikaze', 10000, [1, 1], 1],
                       ['Kit de Ingenieros', 'Kit de Ingenieros', 0, [1], 2],
                       ['GBU-43/B Massive Ordnance Air Blast Paralizer', 'Paralizer', 0, [1, 1], 'Siempre'],
                       ['Explorar', 'Explorar', 0, [3, 3], 'Siempre']]
        a = Vehiculo('Barco Pequeno', True, [3, 1], 30, [Armas(todas_armas[0]), Armas(todas_armas[3]),
                                                         Armas(todas_armas[6])])
        b = Vehiculo('Buque de Guerra', True, [3, 2], 60, [Armas(todas_armas[0]), Armas(todas_armas[1]),
                                                           Armas(todas_armas[6])])
        c = Vehiculo('Lancha', True, [2, 1], 10, [Armas(todas_armas[6])])
        d = Vehiculo('Puerto', True, [4, 2], 80, [Armas(todas_armas[0]), Armas(todas_armas[5]), Armas(todas_armas[6])])
        e = Vehiculo('Avion explorador', False, [2, 2], None, [Armas(todas_armas[7])])
        f = Vehiculo('Kamikaze IXXI', False, [1, 1], None, [Armas(todas_armas[4])])
        g = Vehiculo('Avion Caza', False, [1, 1], None, [Armas(todas_armas[2])])
        listita = [a, b, c, d, e, f, g]
        self.vehiculos += listita

    def mostrar_vehiculos(self, avion):
        for i in range(len(self.vehiculos)):
            a = self.vehiculos[i]
            r = '[' + str(i + 1) + '] ' + a.pieza
            b = ''
            for n in range(len(a.ataques)):
                if a.ataques[n].inutil is not True:
                    b += a.ataques[n].sobrenombre + '   '
            if avion == 'Todos':
                if a.barco is True and a.activo is True:
                    r += ': Vida ' + str(a.resistencia) + ' [Activo] Ataques Disponibles: ' + b
                elif a.activo is True:
                    r += ' [Activo] Ataques Disponibles: ' + b
                elif a.barco is False:
                    r += ' [Deshabilitado] ' + str(a.habilitado)
                else:
                    r += ' [Destruido]'
            elif avion is True:
                if a.barco is False and a.activo is True:
                    r += ' [Activo] Ataques Disponibles: ' + b
                elif a.barco is True:
                    r = ''
                else:
                    r += ' [Deshabilitado] ' + str(a.habilitado)
            else:
                if a.barco is True and a.activo is True and (avion == 'Todos' or avion is False):
                    r += ': Vida ' + str(a.resistencia) + ' [Activo] Ataques Disponibles: ' + b
                elif a.activo is not True:
                    r += ' [Destruido]'
                else:
                    r = ''
            if r != '':
                print(r)

    def mostrar_vehiculos_activos(self):
        orden = []
        a = 1
        for i in range(len(self.vehiculos)):
            if self.vehiculos[i].activo is True:
                r = '[' + str(a) + '] ' + self.vehiculos[i].pieza
                print(r)
                orden2 = [a, i]
                orden.append(orden2)
                a += 1
        return orden

    def habilitar_explorador(self):
        self.vehiculos[4].habilitado -= 1
        if self.vehiculos[4].habilitado <= 0:
            self.vehiculos[4].activo = True

    def revisar_si_gano(self):
        a = [0, 1, 3]
        todos = False
        for i in a:
            if self.vehiculos[i].activo is True:
                todos = True
        return todos

    def ataque_excitoso(self, danados, arma):
        self.ataque_exitosos += 1
        self.dano_causado += len(danados) * arma.dano
        try:
            numero=self.ataque_ocupado[arma]
            numero+= 1
            self.ataque_ocupado[arma]=numero
        except KeyError:
            self.ataque_ocupado[arma]=1

    def mostrar_estadisticas(self, turno):
        r = 'Nombre jugador {}\nPorcentaje ataques exitosos: '.format(self.nombre_jugador)
        if self.numero_ataques > 0:
            r += str((self.ataque_exitosos * 100) / self.numero_ataques) + '%'
        r += '\nDano total causado: ' + str(self.dano_causado)
        lista = list(self.ataque_ocupado.keys())
        lista2 = list(self.ataques_exitosos_tipo.keys())
        r+='\nPorcentaje de ataques exitosos por barco y avion:'
        for i in range(len(lista2)):
            for z in lista2[i].ataques:
                for n in range(len(lista)):
                    if z == lista[n]:
                        r += '\n-'+lista2[i].pieza + '  '
                        r += str((self.ataques_exitosos_tipo[lista2[i]] * 100) / self.ataque_ocupado[lista[n]])
        r += '\nDano total recibido: '
        a = 0
        for i in self.vehiculos:
            a += i.dano_total
        r += str(a) + '\nAtaque mas utilizado: '
        lista = list(self.ataque_ocupado.keys())
        b = 0
        ataque = ''
        for i in range(len(lista)):
            if b < self.ataque_ocupado[lista[i]]:
                b = self.ataque_ocupado[lista[i]]
                ataque = lista[i].nombre
        r += ataque + '\nBarco con mas movimientos: '
        l_movimientos = list(self.movimientos.keys())
        c = 0
        barco = ''
        for i in range(len(l_movimientos)):
            if c < self.movimientos[l_movimientos[i]]:
                c = self.movimientos[l_movimientos[i]]
                barco = lista[i].pieza
        r += barco + '\nCantidad de turnos: ' + str(turno)
        print(r)
