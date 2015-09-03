__author__ = 'JuanFrancisco'
asdf=['nombre', 'Juan Lopez']
linea=asdf[1]
linea2=asdf[0][1:-1]
qwer='hola y panchito'
a=qwer.replace('y','and')
b=[int('05'),30]
c=[int('08'),31]
b.append(c)
print(b)
print(a)
requisitos='MAT1600?'
ramos_pre=[
      "IEE2123",
      "IEE1133",
      "ICM2003",
      "ICS1113",
      "FIL188",
      "EYP1113",
      "ICS1513",
      "MAT1610",
      "FIS1513",
      "FIS1533",
      "ICE2623",
      "ING1004",
      "LET0003",
      "FIS0152",
      "ICH2304",
      "IIC2764",
      "IEE2103",
      "ICT2223",
      "IEE2483",
      "MAT1203",
      "FIS0151",
      "IIQ2642",
      "ICS2123",
      "MAT1630",
      "MAT1620",
      "ING2030",
      "MAT1640",
      "ICE2630",
      "QIM100A",
      "IIC1103",
      "FIS0153",
      "ICC2414",
      "IRB2001",
      "FIS1523",
      "ICC2954",
      "MAT1600"
    ]
a = 0
b=len(requisitos)
lista1 = []
curso=''
while a != len(requisitos):
    if requisitos[a] == '(' and requisitos[a+1]!='c':
        lista = []
        curso = ''
        a+=1
        while requisitos[a] != ')':
            if requisitos[a] == 'o':
                lista.append(curso)
                lista.append('o')
                curso = ''
            elif requisitos[a] == 'y':
                lista.append(curso)
                lista.append('y')
                curso = ''
            elif requisitos[a]=='(':
                a+=2

            elif requisitos[a]==' ':
                pass
            else:
                curso += requisitos[a]
            a += 1
        if requisitos[a] == ')':
            lista.append(curso)
        lista1.append(lista)
        curso=''
    elif requisitos[a] == 'y':
        if curso!='':
            lista1.append(curso)
        lista1.append('y')
        curso = ''
    elif requisitos[a] == 'o':
        if curso!='' and curso!=')':
            lista1.append(curso)
        lista1.append('o')
        curso = ''
    elif requisitos[a] == '?':
        if curso!='':
            lista1.append(curso)
    elif requisitos[a]==' ':
        pass
    elif requisitos[a]=='(':
        a+=2
    else:
        curso += requisitos[a]
    a += 1
lista2=[]
for i in range(len(lista1)):
    b=lista1[i]
    if type(b) == type([]):
        nueva = []
        for n in range(len(b) - 1):
            if n % 2 != 0:
                if b[n] == 'o':
                    if b[n - 1] in ramos_pre or b[n + 1] in ramos_pre:
                        a = True
                        if n>=3:
                            nueva.append('o')
                    else:
                        a=False
                        if n>=3:
                            nueva.append('o')
                    nueva.append(a)
                elif b[n] == 'y':
                    if b[n - 1] in ramos_pre and b[n + 1] in ramos_pre:
                        a = True
                        if n>=3:
                            nueva.append('y')
                    else:
                        a=False
                        if n>=3:
                            nueva.append('y')
                    nueva.append(a)
        lista2.append(nueva)
    elif b=='o':
        lista2.append('o')
    elif b=='y':
        lista2.append('y')
    else:
        if b in ramos_pre:
            a=True
            lista2.append(a)
        else:
            a=False
            lista2.append(a)
lista3=lista2
for i in range(len(lista3)):
    listita=lista3[i]
    if type(listita) == type([]):
        if len(listita)>=3:
            for n in range(1,len(listita),2):
                if listita[n]=='o':
                    listita[n+1]=listita[n-1] or listita[n+1]
                else:
                    listita[n+1]=listita[n-1] and listita[n+1]
            lista3[i]=listita[n+1]
        else:
            lista3[i]=listita[0]
ramo=lista3[0]
for i in range(1,len(lista3),2):
    if lista3[i]=='o':
        ramo=ramo or lista3[i+1]
    else:
        ramo=ramo and lista3[i+1]
algo=ramo


print(lista1)
print(lista2)
print(lista3)
print(algo)
print(b)


print(9%2)
