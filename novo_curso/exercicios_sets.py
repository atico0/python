from random import randint
lista_d_lista_d_int = []

for c in range(10):
    lista_d_lista_d_int.append([])
    for k in range(10):
        lista_d_lista_d_int[c].append(randint(1,10))


def duplicados(lista):
    ocorrencias = []
    for k in lista:
        if k in ocorrencias:
            return k
        else:
            ocorrencias.append(k)
    return -1


for c in lista_d_lista_d_int:
    print(c)
    print(duplicados(c))
