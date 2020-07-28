import random
from time import sleep
lista=['tesoura','pedra','papel']
decisao=random.choice(lista)
print("""SUAS OPÇÕES:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
dj=str
jogador=int(input('Faça sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if jogador==1:
    dj='pedra'
elif jogador==2:
    dj='papel'
else:
    dj='tesoura'
print('-='*20)
print('O COMPUTADOR JOGOU: {}'.format(decisao.upper()))
print('O JOGADOR JOGOU: {}'.format(dj.upper()))
print('-='*20)
if jogador==1 and decisao=='tesoura' or jogador==2 and decisao=='pedra' or jogador==3 and decisao=='papel':
    print('jogador VENCEU!!!! parabens')
elif dj==decisao:
    print('EMPATE!!')
else:
    print('O computador venceu. Mais sorte na proxima')
