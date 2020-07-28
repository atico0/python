def leia_din():
    v = input('Digite um valor: R$')
    while not v.isnumeric():
        v = input('Valor invalido digite novamente: R$')
    return int(v)