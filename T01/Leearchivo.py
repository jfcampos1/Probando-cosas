__author__ = 'JuanFrancisco'

with open('prueba.txt', mode='r') as arch:
    arch.readline()
    principio = True
    lista = []
    linea1 = arch.readline().strip()
    while principio == True:
        if linea1 == ']':
            principio = False
        elif linea1 == '{':
            linea1 = arch.readline().strip()
            diccionario = {}
            termina = True
            while termina == True:
                linea = linea1.split(':')
                ultimos_dos = linea1[-2:]
                ultimo = linea1[-1:]
                tag = linea[0]
                tag_limpio = tag[1:-1]

                if ultimos_dos == '],':
                    diccionario[tag_limpio] = []
                elif ultimos_dos == '",':
                    if len(linea)==3:
                        valor=linea[1]+':'+linea[2]
                        valor_con2=valor[2:-2]
                    else:
                        valor = linea[-1]
                        valor_con2 = valor[2:-2]
                    diccionario[tag_limpio] = valor_con2
                elif ultimo == '"':
                    if len(linea)==3:
                        valor=linea[1]+':'+linea[2]
                        valor_con1=valor[2:-1]
                    else:
                        valor = linea[-1]
                        valor_con1 = valor[2:-1]
                    diccionario[tag_limpio] = valor_con1
                elif ultimo == '}' or ultimos_dos == '},':
                    termina = False
                    lista.append(diccionario)
                elif ultimo == '[':
                    lista_termina = True
                    listita = []
                    while lista_termina == True:
                        linea2 = arch.readline().strip()
                        ultimo=linea2[-1:]
                        ultimos_dos=linea2[-2:]
                        if linea2 == ']':
                            lista_termina = False
                        elif ultimo=='"':
                            nombre=linea2[1:-1]
                            listita.append(nombre)
                        elif ultimos_dos=='",':
                            nombre=linea2[1:-2]
                            listita.append(nombre)
                            print(nombre)
                    diccionario[tag_limpio]=listita
                elif ultimo==',':
                    if len(linea)==3:
                        valor=linea[1]+':'+linea[2]
                        valor_con1=valor[1:-1]
                    else:
                        valor = linea[-1]
                        valor_con1 = valor[1:-1]
                    diccionario[tag_limpio] = int(valor_con1)
                linea1 = arch.readline().strip()

    print(lista)


