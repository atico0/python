c = 0
pi = ' '
from random import  randint

print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
while True:
    n = randint(0, 10)
    print(n)
    sn = int(input('Diga seu valor: '))
    while pi not in 'PI':
        pi = (input('par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-'*20)
    print(f'Você jogou {sn} e o computador jogou {n}. O total deu {sn+n} ',end='')
    soma= sn + n
    if soma % 2 == 0:
        num= 'P'
        nn = 'PAR'
    else:
        num = 'I'
        nn = 'Ímpar'
    print(nn)
    print('-'*20)
    if num == pi:
        print('Você VENCEU!  ')
        print('vamos jogar novamente...')
        print('-='*20)
    else:
        print('Você PERDEU!!')
        print('-=-'*20)
        break
    c += 1
    pi='a'
print(f'GAME OVER! você venceu {c} vezes')