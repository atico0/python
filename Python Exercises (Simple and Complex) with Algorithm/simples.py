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




#Problem 6

A = {3, 2, 4, 5, 6, 7, 8}
B = {4, 12, 5, 1, 6, 8}
A.union(B)



#Assignment 6

A = {5, 12, 52, 0, 8}
B = {2, 5, 1, 9, 8}
C = {4, 5, 6, 0, 10}

A.union(B, C)



#Problem 7

A = {5, 2, 4, 6, 7, 1}
B = {5, 3, 11}
A.intersection(B)


#Assignment 7

A = {5, 2, 4, 6, 7, 1}
B = {5, 3, 11}
C = {4, 5, 12, 2, 1, 0}
A.intersection(B, C)


#Problem 8

A = {1, 12, 2, 6, 7, 8}
B = {10, 0, 1, 3, 6}
A.difference(B)
B.difference(A)


#assignment 8

A = {12, 2, 0, 3, 8}
B = {15, 10, 12, 3, 6}
A.symmetric_difference(B)



#Problem 9

num = int(input("NUM: "))

for c in range(11):
    print(f'{num}X{c} = {num*c}')



#Assignment 9


n1 = int(input('N1: '))
n2 = int(input('N2: '))

for c in range(11):
    print(f'{n1}X{c} = {n1*c}, {n2}X{c} = {n2*c}')



#Problem 10

marks = []
for c in range(1,7):
    marks.append(float(input(f'Digite a mark {c}: ')))

print(f'Total: {sum(marks)}'
print(f'Média: {sum(marks)/len(marks)}')


#Assignment 10


marks = []
for c in range(1,7):
    marks.append(float(input(f'Digite a mark {c}: ')))
total = sum(marks)
avg = total/len(marks)
print(f'Total: {total}')
print(f'Média: {avg}')

for c in marks:
    print(f'{c} representa {round((c/total)*100, 2)}% do total')








