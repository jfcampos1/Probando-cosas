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
        self.hora_salas = []

    def inscribir_ramo(self, nrc, usuario):
        if self.disp != 0:
            cumple = True
            if self.nombre in usuario.permisos:
                return 'bien'
            creditos = 0
            for i in usuario.cursos_tomar:
                creditos += i.creditos
            if creditos + self.creditos > (55 + (6 - usuario.grupo) * 2):
                return 'Exceso de creditos'
            else:
                usuario.evaluaciones_alumno()
                for i in usuario.evaluaciones_alum:
                    for n in self.evaluaciones:
                        if i.fecha == n.fecha and i.hora == n.hora:
                            return 'Tope de evaluaciones'
                for z in usuario.cursos_tomar:
                    for j in z.hora_salas[0].hora:
                        for i in self.hora_salas[0].hora:
                            hora_nueva = i
                            hora_tomada = j
                            dia = hora_tomada[0]
                            modulo = hora_tomada[1]
                            dia_nuevo = hora_nueva[0]
                            modulo_nuevo = hora_nueva[1]
                            for y in dia:
                                for a in dia_nuevo:
                                    for n in modulo:
                                        for b in modulo_nuevo:
                                            if y == a and n == b:
                                                return 'Tope de horario'

                if cumple == True:
                    requisitos = self.requisitos
                    if requisitos == 'No tiene':
                        self.ocu = self.ocu + 1
                        self.disp = self.disp - 1
                        self.lista_alumnos.append(usuario)
                        usuario.cursos_tomar.append(self)
                        return 'bien'
                    else:
                        requisitos += '?'
                        a = 0
                        lista1 = []
                        ramos_pre = usuario.cursos_aprobados
                        curso = ''
                        while a != len(requisitos):
                            if requisitos[a] == '(' and requisitos[a + 1] != 'c':
                                lista = []
                                curso = ''
                                a += 1
                                while requisitos[a] != ')':
                                    if requisitos[a] == 'o':
                                        lista.append(curso)
                                        lista.append('o')
                                        curso = ''
                                    elif requisitos[a] == 'y':
                                        lista.append(curso)
                                        lista.append('y')
                                        curso = ''
                                    elif requisitos[a] == '(':
                                        a += 2

                                    elif requisitos[a] == ' ':
                                        pass
                                    else:
                                        curso += requisitos[a]
                                    a += 1
                                if requisitos[a] == ')':
                                    lista.append(curso)
                                lista1.append(lista)
                                curso = ''
                            elif requisitos[a] == 'y':
                                if curso != '':
                                    lista1.append(curso)
                                lista1.append('y')
                                curso = ''
                            elif requisitos[a] == 'o':
                                if curso != '' and curso != ')':
                                    lista1.append(curso)
                                lista1.append('o')
                                curso = ''
                            elif requisitos[a] == '?':
                                if curso != '':
                                    lista1.append(curso)
                            elif requisitos[a] == ' ':
                                pass
                            elif requisitos[a] == '(':
                                curso = curso
                                a += 2
                            else:
                                curso += requisitos[a]
                            a += 1
                        lista2 = []
                        for i in range(len(lista1)):
                            b = lista1[i]
                            if type(b) == type([]):
                                nueva = []
                                for n in range(len(b) - 1):
                                    if n % 2 != 0:
                                        if b[n] == 'o':
                                            if b[n - 1] in ramos_pre or b[n + 1] in ramos_pre:
                                                a = True
                                                if n >= 3:
                                                    nueva.append('o')
                                            else:
                                                a = False
                                                if n >= 3:
                                                    nueva.append('o')
                                            nueva.append(a)
                                        elif b[n] == 'y':
                                            if b[n - 1] in ramos_pre and b[n + 1] in ramos_pre:
                                                a = True
                                                if n >= 3:
                                                    nueva.append('y')
                                            else:
                                                a = False
                                                if n >= 3:
                                                    nueva.append('y')
                                            nueva.append(a)
                                lista2.append(nueva)
                            elif b == 'o':
                                lista2.append('o')
                            elif b == 'y':
                                lista2.append('y')
                            else:
                                if b in ramos_pre:
                                    a = True
                                    lista2.append(a)
                                else:
                                    a = False
                                    lista2.append(a)
                        lista3 = lista2
                        for i in range(len(lista3)):
                            listita = lista3[i]
                            if type(listita) == type([]):
                                if len(listita) >= 3:
                                    n = 0
                                    for n in range(1, len(listita), 2):
                                        if listita[n] == 'o':
                                            listita[n + 1] = listita[n - 1] or listita[n + 1]
                                        else:
                                            listita[n + 1] = listita[n - 1] and listita[n + 1]
                                    lista3[i] = listita[n + 1]
                                else:
                                    lista3[i] = listita[0]
                        ramo = lista3[0]
                        for i in range(1, len(lista3), 2):
                            if lista3[i] == 'o':
                                ramo = ramo or lista3[i + 1]
                            else:
                                ramo = ramo and lista3[i + 1]
                        if ramo == True:
                            self.ocu = self.ocu + 1
                            self.disp = self.disp - 1
                            self.lista_alumnos.append(usuario)
                            usuario.cursos_tomar.append(self)
                            # cumple requisito
                            return 'bien'
                        else:
                            return 'No cumple requisitos'
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
        self.evaluaciones_alum = []
        self.permisos = []

    def botar_ramo(self, sigla_curso):
        for i in range(len(self.cursos_tomar)):
            if self.cursos_tomar[i].sigla == sigla_curso:
                del self.cursos_tomar[i]

    def bacan(self, idolos=[], alumnos=[]):
        if self.nombre in idolos:
            return 1
        else:
            for i in range(len(alumnos)):
                if self.nombre in alumnos[i].idolos:
                    idolos.append(self.nombre)
                    return 1 + alumnos[i].bacan(idolos, alumnos) / len(alumnos[i].idolos)

    def evaluaciones_alumno(self):
        self.evaluaciones_alum = []
        for i in self.cursos_tomar:
            for n in i.evaluaciones:
                self.evaluaciones_alum.append(n)

    def permiso(self, ramo):
        lista = self.permisos
        lista.append(ramo)
        self.permisos = lista

    def con_permiso(self, alumno):
        lista = self.permisos
        lista.append(alumno)
        self.permisos = lista

    def quitar_permiso(self, alumno):
        for i in range(len(self.permisos)):
            if alumno == self.permisos[i]:
                del self.permisos[i]

    def botar_permiso(self, ramo):
        if ramo in self.cursos_tomar:
            ramo.botar_ramo(self.nombre)
        for i in range(len(self.permisos)):
            if ramo == self.permisos[i]:
                del self.permisos[i]


class Horario:
    def __init__(self, dic):
        self.hora = {}
        self.salas = {}
        if 'hora_cat' in dic:
            hora_cat = dic['hora_cat']
            hora = hora_cat.split(':')
            dias = hora[0].split('-')
            hora = hora[1].split(',')
            horas = [dias] + [hora]
            self.hora['hora_cat'] = horas
        if 'hora_ayud' in dic:
            hora_ayud = dic['hora_ayud']
            hora = hora_ayud.split(':')
            dias = hora[0].split('-')
            hora = hora[1].split(',')
            horas = [dias] + [hora]
            self.hora['hora_ayud'] = horas
        if 'hora_lab' in dic:
            hora_lab = dic['hora_lab']
            hora = hora_lab.split(':')
            dias = hora[0].split('-')
            hora = hora[1].split(',')
            horas = [dias] + [hora]
            self.hora['hora_lab'] = horas
        if 'sala_cat' in dic:
            sala_cat = dic['sala_cat']
            self.salas['sala_cat'] = sala_cat
        if 'sala_ayud' in dic:
            sala_ayud = dic['sala_ayud']
            self.salas['sala_ayud'] = sala_ayud
        if 'sala_lab' in dic:
            sala_lab = dic['sala_lab']
            self.salas['sala_lab'] = sala_lab


class Evaluacion:
    def __init__(self, sigla, tipo, sec, fecha):
        self.fechayhora = fecha
        fechaconhora = self.fechayhora.split(' - ')
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
        hora = Horario(hora_salas)
        cur.hora_salas.append(hora)
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
        encontradas = []
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
    for i in lista_alumnos:
        bacanocidad = i.bacan(alumnos=lista_alumnos)
        i.bacanocidad = bacanocidad
    for i in range(len(lista_alumnos)):
        for n in range(1, len(lista_alumnos) - 1):
            if lista_alumnos[n].bacanocidad > lista_alumnos[i].bacanocidad:
                a = lista_alumnos[i]
                lista_alumnos[i] = lista_alumnos[n]
                lista_alumnos[n] = a
    cantidad_alumnos = len(lista_alumnos)
    grupos = {}
    for i in range(1, 11):
        grupos[i] = lista_alumnos[(cantidad_alumnos * (i - 1)) // 10:(cantidad_alumnos * i) // 10]
    for i in grupos:
        grupo = grupos[i]
        for n in grupo:
            n.grupo = i

    algo = equivalencias
    listas = [todos_cursos, lista_personas, lista_alumnos, grupos]
    return listas

# termine de indexar los archivos
