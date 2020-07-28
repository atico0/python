from random import choice
p=input('Primeiro aluno: ')
s=input('Segundo aluno: ')
t=input('Terceiro aluno: ')
u=input('Quarto aluno: ')
j=p,s,t,u
print('O aluno escolhido foi: {}'.format(choice(j)))