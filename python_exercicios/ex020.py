import random
n=input('Primeiro aluno: ')
s=input('Segundo aluno: ')
t=input('Terceiro aluno: ')
u=input('Quarto aluno: ')
lista=[n,u,t,s]
random.shuffle(lista)
print('A ordem de apresentção sera:')
print(lista)
