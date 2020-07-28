while True:
    x = 'x'
    print(x)
    co = int(input('Quantas casas vc quer andar na vertical: '))
    x = ('\n'*co) + x
    print(x)
    resp = input('Quer continuar: [S/N]').upper()
    while resp not in 'SN':
        resp = input('Não entendi. Digite novamente: [S/N]').upper()
    if resp == 'N':
        break