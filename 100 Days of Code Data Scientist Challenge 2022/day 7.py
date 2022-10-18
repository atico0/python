# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:26:51 2022

@author: luisg
"""

import numpy as np


#Exercise 1 Using Numpy create the following two-dimensional array:
#[[0 0 0 0 0 0]
 #[0 1 0 0 0 0]
 #[0 0 2 0 0 0]
 #[0 0 0 3 0 0]
 #[0 0 0 0 4 0]
 #[0 0 0 0 0 5]]
#Print result to the console as shown below.

#criando uma matriz diagonal com a diagonal principal de 0 a 5
print(np.diag(range(6)))
print(np.diag(np.arange(6)))

#acima da diagonal princial
np.diag(range(3), k=1)
#abaixo da diagonal principal
np.diag(range(3), k=-3)



#Using Numpy create the following array:
#array([[ 0,  1,  2,  3],
#      [ 4,  5,  6,  7],
#     [ 8,  9, 10, 11]])
#Save this array to a binary file named 'array.npy' and then load that file
#back into another variable. Print this variable to the console.

#definindo vetor que vai de 0 a 11 e dps mudando sua dimensão para 3x4
vetor = np.arange(12).reshape(-1,4)
vetor
#salvando o vetor com o nome array.npy
#eu já coloquei a IDE na pasta do github então foi pra lá automaticamente
np.save('array.npy', vetor)
vetor2 = np.load('array.npy')
print(vetor2)







#Using Numpy create the following array:
#array([[ 0,  1,  2,  3],
       #[ 4,  5,  6,  7],
       #[ 8,  9, 10, 11]])
#Save this array to a text file named 'array.txt' with two decimal places
#and then load this file back into another variable.
#Print this variable to the


#definindo array
vetor = np.array([[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 10, 11]], dtype='float32')
vetor
#salvando numpy como um txt com duas casas decimais
np.savetxt('array.txt', vetor, fmt='%0.2f')
#pegando o vetor salvo como txt
vetor2 = np.loadtxt('array.txt')
vetor2


#resposta do quesito
import numpy as np
 
A = np.arange(12, dtype='int').reshape(-1, 4)
np.savetxt(fname='array.txt', X=A, fmt='%0.2f')
B = np.loadtxt('array.txt')
 
 
print(B)

























