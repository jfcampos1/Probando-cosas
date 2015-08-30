__author__ = 'JuanFrancisco'
import Leearchivo
class Curso:
    def __init__(self,sigla,profesor,lista_alumnos,horario,seccion,campus,evaluaciones,requisitos,capacidad_max,creditos):
        self.sigla=sigla
        self.profesor=profesor
        self.lista_alumnos=[]
        self.horario=horario
        self.seccion=seccion
        self.campus=campus
        self.evaluaciones=evaluaciones
        self.requisitos=requisitos
        self.capacidad_max=capacidad_max
        self.creditos=creditos
    def inscribir_ramo(self,sigla):
        if muchas_cosas:
        self.capacidad_max=self.capacidad_max -1


    def botar_ramo(self,nombre_alumno):
        self.lista_alumnos.remove(nombre_alumno)
        self.capacidad_max=self.capacidad_max+1

class Alumno:
    def __init__(self,nombre,apellido,contrasena,cursos_aprobados):
        self.nombre=nombre
        self.apellido=apellido
        self.contrasena=contrasena
        self.horario_inscripcion=''
        self.cursos_aprobados=cursos_aprobados
        self.cursos_tomar=[]
class Horario:
    def __init__(self):
        self.tipo=tipo
class Evaluacion:
    def __init__(self):
        self.nombre=nombre
        self.hora=hora
        self.sala=sala
        self.sigla=sigla
def Menu():
    #formar los cursos
    curso=Leearchivo.Archivo()
    curso.leer('cursos.txt')
    cursos_dic=curso.diccionario
    for i in range(len(cursos_dic)):
        nombre_curso=cursos_dic[i]['curso']
        sigla=cursos_dic[i]['sigla']
        nrc=cursos_dic[i]['NRC']
        retiro=cursos_dic[i]['retiro']
        eng=cursos_dic[i]['eng']
        sec=cursos_dic[i]['sec']
        apr=cursos_dic[i]['apr']
        profesor=cursos_dic[i]['profesor']
        campus=cursos_dic[i]['campus']
        cred=cursos_dic[i]['cred']
        ofr=cursos_dic[i]['ofr']
        ocu=cursos_dic[i]['ocu']
        disp=cursos_dic[i]['disp']











