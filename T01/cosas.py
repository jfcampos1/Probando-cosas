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
requisitos='(FIS1503 y MAT1203) o (MAT1202 y MAT1620(c)) o (FIS1513(c) y MAT1512(c)) o FIS1513(c) o ICE1513(c)?'
a = 0
b=len(requisitos)
lista1 = []
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
        lista1.append(curso)
    elif requisitos[a]==' ':
        pass
    elif requisitos[a]=='(':
        a+=2
    else:
        curso += requisitos[a]
    a += 1
print(lista1)



print(9%2)
