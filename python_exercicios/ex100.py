from random import randint


def sorteio(lista):
    lista = list(lista)
    print('Sorteando os valores: ',end='')
    for c in range(5):
        lista.append(randint(-99**2,99**2))
        print(f'{lista[c]}',end=' ')
    print('\n')
    return lista

def soma(lista):
    cont  = 0
    lista = list(lista)
    for c in lista:
        if c%2==0:
            cont+= c
    return cont

l = []
l = sorteio(l)
print(f'A soma dos valores pares é: {soma(l)}')
