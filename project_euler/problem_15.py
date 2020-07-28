from random import randint

cont = 0
matriz = []
escolhas = ['DIREITA', 'BAIXO']
while cont != 9099999:
    lista = []
    for k in range(20):
        lista.insert(randint(0, 1), escolhas[0])
        lista.insert(randint(0, 1), escolhas[1])
    cont += 1
    if lista not in matriz:
        matriz.append(lista)
    print(len(matriz))

