__author__ = 'Alain Lotissier'
class Audifono:

    def __init__(self, freq_min, freq_max, impedancia, intensidad_maxima, **kwargs):
        super().__init__(**kwargs)
        self.freq_min = freq_min
        self.freq_max = freq_max
        self.impedancia = impedancia
        self.intensidad_maxima = intensidad_maxima


    def escuchar(self, cancion,y=''):
        print('la cancion '+str(cancion)+' esta siendo reproducida desde un audifono '+y)


class Circumaulares(Audifono):

    def __init__(self, porcentaje_aislacion, **kwargs):
        super().__init__(**kwargs)
        self.porcentaje_aislacion = porcentaje_aislacion

    def escuchar(self,cancion):
        super().escuchar(cancion,y='')



class Intramaurales(Audifono):

    def __init__(self, porcentaje_incomodidad, **kwargs):
        super().__init__(**kwargs)
        self.porcentaje_incomodidad = porcentaje_incomodidad

    def escuchar(self, cancion):
        super().escuchar(cancion,y='')


class Inalambrico(Audifono):

    def __init__(self, rango_maximo, **kwargs):
        super().__init__(**kwargs)
        self.rango_maximo = rango_maximo

    def escuchar(self, cancion):
        super().escuchar(cancion,y='Inalambrico')

class Bluetooth(Inalambrico):

    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id = id

    def escuchar(self, cancion):
        super().escuchar(cancion,y="con Bluetooth")

Audifono1 = Audifono (1, 1, 1, 1)
Bluetooth1= Bluetooth(id=12,rango_maximo=6,freq_min=1,freq_max=2,intensidad_maxima=3,impedancia=4)
print(Bluetooth1.escuchar("Iris"))



