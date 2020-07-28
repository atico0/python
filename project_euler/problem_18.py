string = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
# Transformando está DISGRAÇA em  algo util
lista = string.split('\n')
l_reserva = []
print(lista)
for x in range(len(lista)):
    lista[x] = lista[x].split()
print(lista)
for x in range(len(lista)):
    l_reserva = []
    for y in lista[x]:
        l_reserva.append(int(y))
    lista[x] = l_reserva
print(lista)

# navegando

lista_caminho = []
lista_posicoes = []
maior = 0
for x in range(len(lista)):
    maior = 0
    for y in range(len(lista[x])):
        if len(lista_posicoes) == 0:
            maior = lista[x][y]
        else:
            if y == lista_posicoes[-1] or y - 1 == lista_posicoes[-1]:
                if lista[x][y] == 64 and len(lista_caminho) == 1:
                    maior = lista[x][y]
                elif lista[x][y] > maior:
                    maior = lista[x][y]
    if maior != 0:
        lista_caminho.append(maior)
        if lista[x].count(maior) > 1:
            lista_posicoes.append(lista[x][lista[x].index(maior)+1:].index(maior))
        else:
            lista_posicoes.append(lista[x].index(maior))

print(lista_caminho)
print(lista_posicoes)
print(sum(lista_caminho))
#incompleta