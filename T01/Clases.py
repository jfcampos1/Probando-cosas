__author__ = 'JuanFrancisco'
import Leearchivo


class Curso:
    def __init__(self, sigla, profesor, seccion, campus, capacidad_max, nombre, creditos, ocupados, apr, disponibles,
                 nrc, eng, retiro):
        self.sigla = sigla
        self.profesor = profesor
        self.lista_alumnos = []
        self.seccion = seccion
        self.campus = campus
        self.evaluaciones = []
        self.requisitos = ''
        self.capacidad_max = capacidad_max
        self.creditos = creditos
        self.ocu = int(ocupados)
        self.disp = disponibles
        self.NRC = nrc
        self.eng = eng
        self.retiro = retiro
        self.apr = apr
        self.nombre = nombre
        self.equiv = []

    def inscribir_ramo(self, nrc, usuario):
        todo = False
        if self.disp != 0:
            # poner las otras restricciones antes
            cumple = True
            if cumple == True:
                requisitos = self.requisitos
                if requisitos == 'No tiene':
                    self.ocu = self.ocu + 1
                    self.disp = self.disp - 1
                    self.lista_alumnos.append(usuario)
                    usuario.cursos_tomar.append(self)
                else:
                    requisitos = requisitos + '"'
                    a = 0
                    lista1 = []
                    while a != len(requisitos):
                        curso = ''
                        if requisitos[a] == '(':
                            lista = []
                            while requisitos[a] != ')':
                                curso = ''
                                if requisitos[a] == 'o':
                                    lista.append(curso)
                                    lista.append('o')
                                    curso = ''
                                elif requisitos[a] == 'y':
                                    lista.append(curso)
                                    lista.append('y')
                                    curso = ''
                                elif requisitos[a + 1] == ')':
                                    lista.append(curso)
                                else:
                                    curso += requisitos[a]
                                a += 1
                            lista1.append(lista)
                        elif requisitos[a] == 'y':
                            lista1.append(curso)
                            lista1.append('y')
                            curso = ''
                        elif requisitos[a] == 'o':
                            lista1.append(curso)
                            lista1.append('o')
                            curso = ''
                        elif requisitos[a + 1] == '"':
                            lista1.append(curso)
                        else:
                            curso += requisitos[a]
                        a += 1
                    # [['hola','o','chao','o','otro'],'y',[]]
                    for i in lista1:
                        if type(i) is list:
                            nueva = []
                            for n in range(len(i) - 1):
                                if n % 2 == 0:
                                    if i[n - 1] == 'o' and (i[n - 2] == usuario or nueva == i[n]):
                                        pass
                                        # Seguir idea





        else:
            return 'vacantes'

    def botar_ramo(self, nombre_alumno):
        for i in range(len(self.lista_alumnos)):
            if nombre_alumno == self.lista_alumnos[i].nombre:
                del self.lista_alumnos[i]
        self.ocu = self.ocu - 1
        self.disp = self.disp + 1


class Alumno:
    def __init__(self, nombre, usuario, contrasena, cursos_aprobados, idolos, alumno):
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.horario_inscripcion = []
        self.cursos_aprobados = cursos_aprobados
        self.cursos_tomar = []
        self.idolos = idolos
        self.alumno = alumno

    def botar_ramo(self, sigla_curso):
        for i in range(len(self.cursos_tomar)):
            if self.cursos_tomar[i].sigla == sigla_curso:
                del self.cursos_tomar[i]


class Horario:
    def __init__(self, dic):
        pass
        if 'hora_cat' in dic:
            hora_cat = dic['hora_cat']
            if len(hora_cat) > 3:
                hora = hora_cat.split(':').split('-')
                hora = [hora[0].split('')]
        if 'hora_ayud' in dic:
            hora_ayud = dic['hora_ayud']
            hora_salas['hora_ayud'] = hora_ayud
        if 'hora_lab' in dic:
            hora_lab = dic['hora_lab']
            hora_salas['hora_lab'] = hora_lab
        if 'sala_cat' in dic:
            sala_cat = dic['sala_cat']
            hora_salas['sala_cat'] = sala_cat
        if 'sala_ayud' in dic:
            sala_ayud = dic['sala_ayud']
            hora_salas['sala_ayud'] = sala_ayud
        if 'sala_lab' in dic[i]:
            sala_lab = dic['sala_lab']
            hora_salas['sala_lab'] = sala_lab
        self.tipo = tipo
        pass


class Evaluacion:
    def __init__(self, sigla, tipo, sec, fecha):
        fechayhora = fecha
        fechaconhora = fechayhora.split(' - ')
        if fechaconhora[1] == 'NA':
            self.hora = 'No asignada'
        else:
            hora = fechaconhora[1].split(':')
            hora = [int(hora[0]), int(hora[1])]
            self.hora = hora
        ficha = fechaconhora[0].split('/')
        self.fecha = ficha
        self.tipo = tipo
        self.sec = sec
        self.sigla = sigla


def Archivos():
    # leer cursos.txt
    todos_cursos = []
    curso = Leearchivo.Archivo()
    curso.leer('cursos.txt')
    cursos_dic = curso.diccionario
    for i in range(len(cursos_dic)):
        nombre_curso = cursos_dic[i]['curso']
        sigla = cursos_dic[i]['sigla']
        nrc = cursos_dic[i]['NRC']
        retiro = cursos_dic[i]['retiro']
        eng = cursos_dic[i]['eng']
        sec = cursos_dic[i]['sec']
        apr = cursos_dic[i]['apr']
        profesor = cursos_dic[i]['profesor']
        campus = cursos_dic[i]['campus']
        cred = cursos_dic[i]['cred']
        ofr = cursos_dic[i]['ofr']
        ocu = cursos_dic[i]['ocu']
        disp = cursos_dic[i]['disp']
        cur = Curso(sigla=sigla, profesor=profesor, seccion=sec, campus=campus, capacidad_max=ofr, creditos=cred,
                    ocupados=ocu, disponibles=disp, nrc=nrc, eng=eng, apr=apr, retiro=retiro, nombre=nombre_curso)
        hora_salas = {}
        if 'hora_cat' in cursos_dic[i]:
            hora_cat = cursos_dic[i]['hora_cat']
            hora_salas['hora_cat'] = hora_cat
        if 'hora_ayud' in cursos_dic[i]:
            hora_ayud = cursos_dic[i]['hora_ayud']
            hora_salas['hora_ayud'] = hora_ayud
        if 'hora_lab' in cursos_dic[i]:
            hora_lab = cursos_dic[i]['hora_lab']
            hora_salas['hora_lab'] = hora_lab
        if 'sala_cat' in cursos_dic[i]:
            sala_cat = cursos_dic[i]['sala_cat']
            hora_salas['sala_cat'] = sala_cat
        if 'sala_ayud' in cursos_dic[i]:
            sala_ayud = cursos_dic[i]['sala_ayud']
            hora_salas['sala_ayud'] = sala_ayud
        if 'sala_lab' in cursos_dic[i]:
            sala_lab = cursos_dic[i]['sala_lab']
            hora_salas['sala_lab'] = sala_lab
        cur.hora = hora_salas
        todos_cursos.append(cur)
    # leer requisitos.txt
    requisito = Leearchivo.Archivo()
    requisito.leer('requisitos.txt')
    equivalencias = {}
    for i in range(len(todos_cursos)):
        for n in range(len(requisito.diccionario)):
            sigla_curso = todos_cursos[i].sigla
            sigla_evaluacion = requisito.diccionario[n]['sigla']
            if sigla_curso == sigla_evaluacion:
                todos_cursos[i].requisitos = requisito.diccionario[n]['prerreq']
                if requisito.diccionario[n]['equiv'] == 'No tiene':
                    equivalencias[sigla_curso] = []
                else:
                    str = requisito.diccionario[n]['equiv']
                    str = str[1:-1]
                    str = str.split(' o ')
                    todos_cursos[i].equiv = str
                    equivalencias[sigla_curso] = str
    # leer evaluaciones

    evaluaciones = Leearchivo.Archivo()
    evaluaciones.leer('evaluaciones.txt')
    for i in range(len(todos_cursos)):
        for n in range(len(evaluaciones.diccionario)):
            sigla_curso = todos_cursos[i].sigla
            sec_curso = todos_cursos[i].seccion
            sec_evaluacion = evaluaciones.diccionario[n]['sec']
            sigla_evaluacion = evaluaciones.diccionario[n]['sigla']
            if sigla_curso == sigla_evaluacion and sec_curso == sec_evaluacion:
                evaluacion = Evaluacion(sigla=sigla_evaluacion, tipo=evaluaciones.diccionario[n]['tipo'],
                                        sec=sec_evaluacion, fecha=evaluaciones.diccionario[n]['fecha'])
                todos_cursos[i].evaluaciones.append(evaluacion)
    # leer personas
    lista_personas = []
    lista_alumnos = []
    personas = Leearchivo.Archivo()
    personas.leer('personas.txt')
    for i in range(len(personas.diccionario)):
        idolos = personas.diccionario[i]['idolos']
        nombre = personas.diccionario[i]['nombre']
        clave = personas.diccionario[i]['clave']
        ramos_pre = personas.diccionario[i]['ramos_pre']
        encontradas=[]
        for z in ramos_pre:
            if z in equivalencias:
                equi = equivalencias[z]
                for n in equi:
                    encontradas.append(n)
        for n in encontradas:
            ramos_pre.append(n)
        alumno = personas.diccionario[i]['alumno']
        usuario = personas.diccionario[i]['usuario']
        alum = Alumno(nombre=nombre, usuario=usuario, contrasena=clave, cursos_aprobados=ramos_pre, idolos=idolos,
                      alumno=alumno)
        lista_personas.append(alum)
        if alumno == 'SI':
            lista_alumnos.append(alum)
    algo=equivalencias
    listas = [todos_cursos, lista_personas, lista_alumnos]
    return listas

# termine de indexar los archivos
