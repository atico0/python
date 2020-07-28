def leiaint():
    try:
        z = int(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        print('Valor não digitado')
        z = 0
    except:
        print('Ocorreu um erro. Digite novamente. ')
        while True:
            try:
                z = int(input('Digite um número inteiro: '))
            except KeyboardInterrupt:
                print('Valor não digitado')
                z = 0
                break
            else:
                break
    try:
        r = float(input('Digite um número real: '))
    except KeyboardInterrupt:
        print('Valor não digitado')
        r = 0
    except:
        print('Ocorreu um erro. Digite novamente. ')
        while True:
            try:
                r = float(input('Digite um número real: '))
            except KeyboardInterrupt:
                print('Valor não digitado')
                r = 0
                break
            else:
                break
    print(f'Você digitou os valores: {z} inteiro e {r} real')


leiaint()