def inteirador(lista):
    for x in range(len(lista)):
        lista[x] = int(lista[x])
        return lista


def somador(string):
    lista = []
    for z in string:
        lista.append(z)
    inteirador(lista)
    return sum(lista)

maior = 1
for c in range(1,100):
    for k in range(1,100):
        if c > 1:
            num = somador(str(c**k))
            if num >= maior:
                print(num)
                maior = num

