from random import randint
n1 = randint(0,100)
n2 = randint(0,100)
n3 = randint(0,100)
n4 = randint(0,100)
n5 = randint(0,100)
tupla = n1 , n2 , n3 ,n4, n5
print(f'Os valores sorteados foram :',end='')
for c in tupla:
    print(f'{c} ',end='')
print(f'\nO maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')