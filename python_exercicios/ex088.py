from random import randint
from time import  sleep
n = int(input('Quantos palpites você quer? '))
l = []
for c in range(n):
    jogo = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    while jogo in l:
        jogo = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    for x in range(len(jogo)):
        while jogo[x] in jogo[x+1:]:
            jogo = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    l.append(jogo[:])
    jogo.clear()
for c in range(n):
    print(f'{c+1} palpite: {l[c]}')
    sleep(2)
