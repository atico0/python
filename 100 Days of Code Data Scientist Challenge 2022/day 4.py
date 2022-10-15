# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:53:19 2022

@author: luisg
"""

import numpy as np


#Exercise 1 Using Numpy create a one-dimensional array of all
#two-digit numbers and print this array
#to the console as shown below.

?np.arange

#criando um array  com elementos de 10 até 100 [10,100)
print(np.arange(10,100))



#Exercise 2 Using Numpy create the following array:

#[[10 11 12 13 14 15 16 17 18 19]
 #[20 21 22 23 24 25 26 27 28 29]
 #[30 31 32 33 34 35 36 37 38 39]
 #[40 41 42 43 44 45 46 47 48 49]
 #[50 51 52 53 54 55 56 57 58 59]
 #[60 61 62 63 64 65 66 67 68 69]
 #[70 71 72 73 74 75 76 77 78 79]
 #[80 81 82 83 84 85 86 87 88 89]
 #[90 91 92 93 94 95 96 97 98 99]]
#Note that the shape of this array is (9, 10).
#In response, print array to the console.    



?np.matrix

#criando um vetor de 10 até 100 [10, 100) e mudando a
#forma do vetor para ter dimensões 9x10
vetor = np.arange(10,100).reshape(9, 10)
vetor
#criando uma matriz de 10 até 100 [10, 100) e mudando a
#forma do vetor para ter dimensões 9x10

matriz = np.matrix(np.arange(10,100))
matriz
matriz.reshape(9, 10)

#fazendo a mesma coisa acima mas dessa
#vez definindo o número de colunas e deixando ele adivinhar o 
#número de linhas
matriz.reshape(-1, 10)



#Exercise 3 Using Numpy create a 6x6 two-dimensional array - identity
#matrix with int data type. Print this array
#to the console as shown below.

#criando uma matriz identidade 6x6 com elementos do tipo int32
print(np.eye(6, 6, dtype='int32'))







































