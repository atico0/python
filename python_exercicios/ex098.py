def contador(a,b,c):
    print('Contegem de 1 até 10 de 1 em 1: ', end=' ')
    for x in range(1, 11):
        print(x, end=' ')
    print('\nContagem de 10 até 0 de -2 em -2: ', end=' ')
    for x in range(10, -2, -2):
        print(x, end=' ')
    print('\nContagem personalizada: ')

    if (b > a and c > 0):
        for x in range(a, b + 1, c):
            print(x, end=' ')
    elif b < a and c < 0:
        for x in range(a, b - 1, c):
            print(x, end=' ')
    elif b == a:
        print(b,end=' ')
    elif b < a and c > 0:
        for x in range(a, b - 1, -1):
            print(x,end=' ')
    elif b > a and c < 0:
        for x in range(a, b + 1, 1):
            print(x,end= ' ')
    elif b > a and c == 0:
        for x in range(a, b + 1, 1):
            print(x,end=' ')
    elif b < a and c == 0:
        for x in range(a, b - 1, -1):
            print(x,end=' ')


a = int(input('Digite de onde deve começar: '))
b = int(input('Digite até onde deve ir: '))
c = int(input('Digite a largura dos passos: '))
contador(a,b,c)