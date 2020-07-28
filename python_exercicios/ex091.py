from random import  randint
from operator import itemgetter
jogadas = dict()
for c in range(4):
         jogadas['jogador'+str(c+1)] = randint(1,6)
ranking ={}
print('Valores sorteados:')
for k,v in jogadas.items():
    print(f'{k} tirou {v} no dado')
ranking = sorted(jogadas.items() , key=itemgetter(1), reverse= True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')