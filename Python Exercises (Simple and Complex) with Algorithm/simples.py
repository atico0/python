# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:10:56 2022

@author: luisg
"""

#Problem 1:


for c in range(1,6):
    print('num, quadrado')
    print(c, '    ',c**2)



#Assignment 1:

for c in range(1,6):
    print('num, quadrado, cubo')
    print(c, '    ',c**2,'     ',c**3)



#Problem 2:

import math
raio = float(input('Digite a  área: '))
area = math.pi*raio**2
print('Área:',area)


#Assingnment 2:

l1 = float(input('LADO 1: '))
l2 = float(input('LADO 2: '))
area = l1*l2
print('Área:',area)




#Problem 3:

nome = input('Digite o nome: ')
idade = int(input('Digite sua idade: '))

print(f'Oi {nome}, sua idade é {idade}')



#Assignment 3:

marks = input('marks: ')
ende = input('Endereço: ')

print(f'Seu endereço e {ende} e sua marks é {marks}')







#Problem 4:

idade = int(input("Digite sua idade: "))
if idade<16:
    print("Você não pode votar")
    print(f'você vai poder votar em {16-idade}')
    print(f'você terá que votar em {18-idade}')
elif 16<=idade<18:
    print('Você pode votar se quiser')
    print(f'você terá que votar em {18-idade} anos')
else:
    print('Você tem que votar')



#Assignment 4:


marks = int(input("marks: "))
if marks<60:
    print(f'Faltam {60-marks} pra você poder entrar na facul')
else:
    print('Parabéns, você pode entrar na facul')




#Problem 5:

v1 = float(input('variável 1: '))
v2 = float(input('variável 2: '))
print(f'soma: {v1+v2}')
print(f'subtração: {v1-v2}')
print(f'multiplicação: {v1*v2}')
print(f'divisão: {v1/v2}')


#Assignment 5:




v1 = float(input('variável 1: '))
v2 = float(input('variável 2: '))
v3 = float(input('variável 3: '))
print(f'soma: {v1+v2+v3}')
print(f'subtração: {v1-v2-v3}')
print(f'multiplicação: {v1*v2*v3}')
print(f'divisão: {v1/v2/v3}')







