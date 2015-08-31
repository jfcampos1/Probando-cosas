__author__ = 'JuanFrancisco'
import Leearchivo
class Curso:
    def __init__(self,sigla,profesor,seccion,campus,capacidad_max,nombre,creditos,ocupados,apr,disponibles,nrc,eng,retiro):
        self.sigla=sigla
        self.profesor=profesor
        self.lista_alumnos=[]
        self.horario=''
        self.seccion=seccion
        self.campus=campus
        self.evaluaciones=[]
        self.requisitos=''
        self.capacidad_max=capacidad_max
        self.creditos=creditos
        self.ocu=ocupados
        self.disp=disponibles
        self.NRC=nrc
        self.eng=eng
        self.retiro=retiro
        self.apr=apr
        self.nombre=nombre
        self.equiv=''

    def inscribir_ramo(self,sigla):
        if muchas_cosas:
        self.capacidad_max=self.capacidad_max -1


    def botar_ramo(self,nombre_alumno):
        self.lista_alumnos.remove(nombre_alumno)
        self.capacidad_max=self.capacidad_max+1

class Alumno:
    def __init__(self,nombre,usuario,contrasena,cursos_aprobados,idolos,alumno):
        self.nombre=nombre
        self.usuario=usuario
        self.contrasena=contrasena
        self.horario_inscripcion=''
        self.cursos_aprobados=cursos_aprobados
        self.cursos_tomar=[]
        self.idolos=idolos
        self.alumno=alumno
class Horario:
    def __init__(self):
        self.tipo=tipo
        pass
class Evaluacion:
    def __init__(self,sigla,tipo,sec,fecha):
        fechayhora=fecha
        fechaconhora=fechayhora.split(' - ')
        if fechaconhora[1]=='NA':
            self.hora='No asignada'
        else:
            self.hora=int(fechaconhora[1])
        fecha=fechaconhora[0].split('/')
        self.fecha=fecha
        self.tipo=tipo
        self.sec=sec
        self.sigla=sigla
def Archivos():
    #leer cursos.txt
    todos_cursos=[]
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
        cur=Curso(sigla=sigla,profesor=profesor,seccion=sec,campus=campus,capacidad_max=ofr,creditos=cred,ocupados=ocu,disponibles=disp,nrc=nrc,eng=eng,apr=apr,retiro=retiro,nombre=nombre_curso)
        if 'hora_cat' in cursos_dic[i]:
            hora_cat=cursos_dic[i]['hora_cat']
            cur.hora_cat=hora_cat
        if 'hora_ayud' in cursos_dic[i]:
            hora_ayud=cursos_dic[i]['hora_ayud']
            cur.hora_ayud=hora_ayud
        if 'hora_lab' in cursos_dic[i]:
            hora_lab=cursos_dic[i]['hora_lab']
            cur.hora_lab=hora_lab
        if 'sala_cat' in cursos_dic[i]:
            sala_cat=cursos_dic[i]['sala_cat']
            cur.sala_cat=sala_cat
        if 'sala_ayud' in cursos_dic[i]:
            sala_ayud=cursos_dic[i]['sala_ayud']
            cur.sala_ayud=sala_ayud
        if 'sala_lab' in cursos_dic[i]:
            sala_lab=cursos_dic[i]['sala_lab']
            cur.sala_lab=sala_lab
        todos_cursos.append(cur)
    #leer requisitos.txt
    requisito=Leearchivo.Archivo()
    requisito.leer('requisitos.txt')
    for i in range(len(todos_cursos)):
        for n in range(len(requisito.diccionario)):
            sigla_curso=todos_cursos[i].sigla
            sigla_evaluacion=requisito.diccionario[n]['sigla']
            if sigla_curso==sigla_evaluacion:
                todos_cursos[i].requisitos=requisito.diccionario[n]['prerreq']
                todos_cursos[i].equiv=requisito.diccionario[n]['equiv']
    #leer evaluaciones
    evaluaciones=Leearchivo.Archivo()
    evaluaciones.leer('evaluaciones.txt')
    for i in range(len(todos_cursos)):
        for n in range(len(evaluaciones.diccionario)):
            sigla_curso=todos_cursos[i].sigla
            sec_curso=todos_cursos[i].seccion
            sec_evaluacion=evaluaciones.diccionario[n]['sec']
            sigla_evaluacion=evaluaciones.diccionario[n]['sigla']
            if sigla_curso==sigla_evaluacion and sec_curso==sec_evaluacion:
                evaluacion=Evaluacion(sigla=sigla_evaluacion,tipo=evaluaciones.diccionario[n]['tipo'],sec=sec_evaluacion,fecha=evaluaciones.diccionario[n]['fecha'])
                todos_cursos[i].evaluaciones.append(evaluacion)
    #leer personas
    lista_personas=[]
    lista_alumnos=[]
    personas=Leearchivo.Archivo()
    personas.leer('personas.txt')
    for i in range(len(personas.diccionario)):
        idolos=personas.diccionario[i]['idolos']
        nombre=personas.diccionario[i]['nombre']
        clave=personas.diccionario[i]['clave']
        ramos_pre=personas.diccionario[i]['ramos_pre']
        alumno=personas.diccionario[i]['alumno']
        usuario=personas.diccionario[i]['usuario']
        alum=Alumno(nombre=nombre,usuario=usuario,contrasena=clave,cursos_aprobados=ramos_pre,idolos=idolos,alumno=alumno)
        lista_personas.append(alum)
        if alumno=='SI':
            lista_alumnos.append(alum)
    listas=[todos_cursos,lista_personas,lista_alumnos]
    return listas

#termine de indexar los archivos




















