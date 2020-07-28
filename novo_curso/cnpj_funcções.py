def ajeitador(string):
    numeros = ''
    for c in string:
        if c.isnumeric():
            numeros += c
    return numeros


def listador(string):
    lista = []
    for c in string:
        lista.append(c)
    return lista


def reversador(lista):
    lista = listador(lista)
    nova_lista = []
    for c in lista:
        nova_lista.insert(0, c)
    return nova_lista


def stringador(lista):
    string = ''
    for c in lista:
        string += c
    return string


def inteirador(lista):
    nova_lista = []
    for c in lista:
        nova_lista.append(int(c))
    return nova_lista


def multiplicador(lista):
    lista_reversa = reversador(lista[:])
    for c in range(len(lista) + 1, 1, -1):
        lista[c - 2] = (lista_reversa[(c - 2)] * c)
    return reversador(lista)


def somador(string):
    soma = 0
    for c in string:
        soma += c
    return 11 - (soma % 11)


def novos_digito(num):
    if num > 9:
        return 0
    return num


def calculo(lista):
    lista = inteirador(listador(lista))
    multiplicados = multiplicador(lista[:-8]) + multiplicador(lista[-8:])
    soma = somador(multiplicados)
    return novos_digito(soma)


def validador(string):
    seq = [1]
    numeros_org = inteirador(listador(ajeitador(string)))
    for c in range(len(numeros_org)):
        if c != 0:
            if numeros_org[c - 1] == numeros_org[c]:
                seq.append(1)
    if seq == len(numeros_org):
        return False
    try:
        print(numeros_org)
        novos_numeros = numeros_org[:-2]
        print(novos_numeros)
        novos_numeros.append(calculo(novos_numeros))
        novos_numeros.append(calculo(novos_numeros))
        novos_numeros = inteirador(novos_numeros)
    except:
        return False
    if novos_numeros == numeros_org:
        print(novos_numeros)
        return True
    else:
        print(novos_numeros)
        print(numeros_org)
        return False
