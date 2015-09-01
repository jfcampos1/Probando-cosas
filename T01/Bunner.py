__author__ = 'JuanFrancisco'
import Clases
def Menu():
    [todos_cursos,lista_personas,lista_alumnos]=Clases.Archivos()
    print('Bienvenido a bummer')
    hora=input('Ingrese hora actual: ')
    hora=hora.split(':')
    hora=[int(hora[0]),int(hora[1])]
    log_in=''
    correcto=False
    while correcto!=True:
        log_in=input('Ingrese usuario o 0 para salir: ')
        if log_in=='0':
            correcto=True
        else:
            clave=input('Ingrese clave: ')
            for i in range(len(lista_personas)):
                if log_in==lista_personas[i].usuario and clave==lista_personas[i].contrasena:
                    correcto=True
                    usuario=lista_personas[i] # el self del usuario
            if correcto==False:
                print('Asegurese de ocupar las mayusculas en la clave y el usuario correctamente')
    if log_in=='0':
        print('Saliste con exito')
    else:
        if usuario.alumno=='SI':
            print('Ingresaste como alumno')
            #agregar restriccion por grupo
            numero=0
            while numero!=5:
                print('1: Inscribir ramo: \n'
                      '2: Botar ramo:\n'
                      '3: Generar Horario:\n'
                      '4: Ver Evaluaciones: \n'
                      '5: Salir: ')
                numero=int(input('Escoga que hacer: '))
                if numero==5:
                    print('Saliste con exito')
                elif numero==1:
                    ramo=input('Ingrese nrc del ramo a tomar:')
                    tomado=1
                    for i in range(len(todos_cursos)):
                        if todos_cursos[i].NRC==ramo:
                            resultado=todos_cursos[i].inscribir_ramo(ramo,usuario)
                            if resultado=='bien':
                                print('Curso inscrito correctamente')
                            else:
                                print('Curso no cumple {}'.format(resultado))
                    #terminar el metodo, es bien largo
                elif numero==2:

                    ramos_actuales=[]
                    for i in usuario.cursos_tomar:
                        ramos_actuales.append(i.sigla)
                    print('Ramos actuales:',ramos_actuales)
                    sigla=input('Ingrese sigla del ramo a botar: ')
                    usuario.botar_ramo(sigla)
                    for i in usuario.cursos_tomar:
                        if sigla==i.sigla:
                            i.botar_ramo(usuario.nombre)
                            print('Ramo correctamente eliminado')
                elif numero==3:
                    pass
                elif numero==4:
                    pass

                lista_alumnos

        else:
            print('Ingresaste como profesor')
            lista_personas
Menu()







