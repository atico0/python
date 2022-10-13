# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 14:49:42 2022

@author: luisg
"""

#Questões
#https://www.udemy.com/course/100-days-of-code-data-scientist-challenge/learn/quiz/5601168#overview

#Exercise 1 Check if all elements from the
#following arrays return the logical value True:

import numpy as np


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

?np.all
#minha solução
#testando se todos os elementos dos vetores são diferentes de False
print(np.all(A))
print(np.all(B))
print(np.all(C))
print(np.all(D))

#solução do exercicio
#fazendo o mesmo que o código acima mas com um loop
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.all(array)}')



#Exercise 2 Check if all elements from the following arrays
#return the logical value True along the axis with index 1:

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])

#testando se
#testando se cada elemento dos vetores são diferentes de False
#para cada linha (ESSA É A SOLUÇÃO)
print(np.all(A, axis=1))
print(np.all(B, axis=1))
print(np.all(C, axis=1))

#testando se cada elemento dos vetores são diferentes de False
#para cada coluna
print(np.all(A, axis=0))
print(np.all(B, axis=0))
print(np.all(C, axis=0))
#testando se cada elemento dos vetores são diferentes de False
print(np.all(A))
print(np.all(B))
print(np.all(C))

#solução do exercicio
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.all(array, axis=1)}')


#Exercise 3 Check if any element of the
#following arrays returns the logical value True:


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

?np.any
#testando se algum elemento do array tem valor True
print(np.any(A))
print(np.any(B))
print(np.any(C))
print(np.any(D))

#solução do exercicio
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')




A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

#testando se algum elemento do array tem valor True
#para cada coluna (ESSA É A SOLUÇÃO)
print(np.any(A, axis=0))
print(np.any(B, axis=0))
print(np.any(C, axis=0))
print(np.any(D, axis=0))

#testando se algum elemento do array tem valor True
#para cada linha
print(np.any(A, axis=1))
print(np.any(B, axis=1))
print(np.any(C, axis=1))
print(np.any(D, axis=1))



#testando se algum elemento do array tem valor True
print(np.any(A))
print(np.any(B))
print(np.any(C))
print(np.any(D))

#solução do exercicio
for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}, {np.any(array, axis=0)}')



















































































