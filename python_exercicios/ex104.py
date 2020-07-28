def leiaINT(num):
    n = input(num)
    while not n.isnumeric():
        n = input('Numero invalido digite outro: ')
    print(f'Vc acabou de digitar o número {n}: ')


leiaINT('Digita ai o numero: ')
