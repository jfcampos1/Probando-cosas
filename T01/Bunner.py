__author__ = 'JuanFrancisco'
import Clases


def Menu():
    [todos_cursos, lista_personas, lista_alumnos, grupos] = Clases.Archivos()
    print('Bienvenido a bummer')
    hora = input('Ingrese hora actual: ')
    hora = hora.split(':')
    hora = [int(hora[0]), int(hora[1])]
    hora = hora[0] * 100 + hora[1]
    log_in = ''
    correcto = False
    usuario = []
    while correcto != True:
        log_in = input('Ingrese usuario o 0 para salir: ')
        if log_in == '0':
            correcto = True
        else:
            clave = input('Ingrese clave: ')
            for i in range(len(lista_personas)):
                if log_in == lista_personas[i].usuario and clave == lista_personas[i].contrasena:
                    correcto = True
                    usuario = lista_personas[i]  # el self del usuario
            if correcto == False:
                print('Asegurese de ocupar las mayusculas en la clave y el usuario correctamente')
    if log_in == '0':
        print('Saliste con exito')
    else:
        if usuario.alumno == 'SI':
            print('Ingresaste como alumno')
            permiso = False
            for n in range(8, 18):
                if n * 100 + 30 <= hora <= (n + 2) * 100 + 30 and usuario in grupos[n - 7]:
                    permiso = True
            if permiso == False:
                print('No es su correspondiente horario bummer solo podra ver sus cursos y evaluaciones')
            else:
                print('Suerte tomando ramos')
            numero = 0
            while numero != 5:
                print('1: Inscribir ramo: \n'
                      '2: Botar ramo:\n'
                      '3: Generar Horario:\n'
                      '4: Ver Evaluaciones: \n'
                      '5: Salir: ')
                numero = int(input('Escoga que hacer: '))
                if numero == 5:
                    print('Saliste con exito')
                elif numero == 1 and permiso == True:
                    ramo = int(input('Ingrese nrc del ramo a tomar:'))
                    tomado = 0
                    for i in range(len(todos_cursos)):
                        if todos_cursos[i].NRC == ramo:
                            tomado = 1
                            resultado = todos_cursos[i].inscribir_ramo(ramo, usuario)
                            if resultado == 'bien':
                                print('Curso inscrito correctamente')
                            else:
                                print('Curso no cumple {}'.format(resultado))
                    if tomado == 0:
                        print('nrc no existe o fue mal ingresada')
                        # terminar el metodo, es bien largo
                elif numero == 2 and permiso == True:

                    ramos_actuales = []
                    for i in usuario.cursos_tomar:
                        ramos_actuales.append(i.sigla)
                    print('Ramos actuales:', ramos_actuales)
                    sigla = input('Ingrese sigla del ramo a botar: ')
                    usuario.botar_ramo(sigla)
                    for i in usuario.cursos_tomar:
                        if sigla == i.sigla:
                            i.botar_ramo(usuario.nombre)
                            print('Ramo correctamente eliminado')
                elif numero == 3:
                    pass
                elif numero == 4:
                    usuario.evaluaciones_alumno()
                    for i in usuario.evaluaciones_alum:
                        print('Ramo:{}\n'.format(i.sigla))
                        for n in range(1, len(usuario.evaluaciones_alum) - 1):
                            if i.sigla == usuario.evaluaciones_alum[n]:
                                print('Prueba: {}\nFecha: {}'.format(i.tipo, i.fechayhora))


        else:
            print('Ingresaste como profesor')
            numero = 0
            while numero != 3:
                print('1: Permiso especial a alumno\n'
                      '2: Quitar permiso a alumno\n'
                      '3: Salir')
                numero = int(input('Escoga que hacer: '))
                if numero == 3:
                    print('Saliste con exito')
                elif numero == 1:
                    a = True
                    self_alumno = ''
                    alumno = ''
                    ramo = ''
                    while a == True:
                        alumno = input('Ingrese el nombre del alumno correctamente: ')
                        for i in lista_alumnos:
                            if alumno == i.nombre:
                                self_alumno = i
                                a = False
                    b = True
                    self_curso = ''
                    while b == True:
                        ramo = input('Ingrese la sigla del ramo: ')
                        for i in todos_cursos:
                            if ramo == i.sigla:
                                self_curso = i
                                b = False
                    self_alumno.permiso(ramo)
                    usuario.con_permiso(alumno)
                    print('Permiso concedido')
                elif numero == 2:
                    a = True
                    self_alumno = ''
                    alumno = ''
                    ramo = ''
                    print(usuario.permisos)
                    while a == True:
                        alumno = input('Ingrese el nombre del alumno correctamente: ')
                        for i in lista_alumnos:
                            if alumno == i.nombre:
                                self_alumno = i
                                a = False
                    b = True
                    self_curso = ''
                    while b == True:
                        ramo = input('Ingrese la sigla del ramo: ')
                        for i in todos_cursos:
                            if ramo == i.sigla:
                                self_curso = i
                                b = False
                    self_alumno.botar_permiso(self_curso)
                    usuario.quitar_permiso(alumno)
                    if ramo in self_alumno.cursos_tomar:
                        self_alumno.botar_ramo(ramo)
                    print('Permiso eliminado')


Menu()
