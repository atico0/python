# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:50:02 2022

@author: luisg
"""

import numpy as np



#Exercise 1: The following array:
#array([[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0],
       #[0, 0, 0, 0, 0, 0]])
#transform to the following:
#array([[10,  0, 10,  0, 10,  0],
       #[ 5,  0,  5,  0,  5,  0],
       #[10,  0, 10,  0, 10,  0],
       #[ 5,  0,  5,  0,  5,  0],
       #[10,  0, 10,  0, 10,  0],
       #[ 5,  0,  5,  0,  5,  0]])
#In response, print transformed array to the console.




#criando matriz 6x6 de uns
matriz = np.zeros(shape=(6,6))
matriz

#reatribuindo valores
matriz[0::2] = [10, 0, 10, 0, 10, 0]
matriz

matriz[1::2] = [5, 0, 5, 0, 5, 0]
matriz

#solução do exercicio
A = np.zeros(shape=(6, 6), dtype='int')
A[::2, ::2] = 10
A[1::2, ::2] = 5
 
 
print(A)



#Exercise 2: Combine the following arrays
#into one as shown below and print it to the console.

#A = np.arange(12).reshape(-1, 4)
#B = np.array([[4, 3, 7, 2],
              #[0, 5, 2, 6]])

#definindo vetor A e B
A = np.arange(12).reshape(-1, 4)
A
B = np.array([[4, 3, 7, 2],
              [0, 5, 2, 6]])
B

#criando um array que junta A e B
print(np.append(A, B,axis=0))
print(np.append(A, B)).reshape(-1, 4)




#Exercise 3: 
#The following arrays are given:
#A = np.arange(8).reshape(-1, 4)
#B = np.array([[9, 10, 11, 3],
              #[2, 8, 0, 9]])      

#Extract the same elements (intersection) of the arrays as
#a list and print result to the console.

#definindo A e B
A = np.arange(8).reshape(-1, 4)
B = np.array([[9, 10, 11, 3],
              [2, 8, 0, 9]])
#pegando a intersecção entre A e B
print(np.intersect1d(A, B))












