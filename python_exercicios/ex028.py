from random import randint
from time  import sleep
s= randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
c=int(input('Em 6ue número pensei? '))
print('PROCESSANDO...')
sleep(1)
if c==s:
    print('Você acertou, parabéns!!!')
else:
    print("""Você errou, O número em 6ue pensei foi {} e não {}, tente de novo """.format(s,c))
