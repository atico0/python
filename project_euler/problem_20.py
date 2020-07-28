from functools import reduce


def somador(string):
    soma = 0
    for c in string:
        soma += int(c)
    return soma
#completa


print(somador(str((reduce(lambda x, y: x * y, [x for x in range(1,101)])))))