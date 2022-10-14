# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:00:13 2022

@author: luisg
"""

import numpy as np

#Exercise 1 Check which numbers (element-wise) from the
#A array are greater than numbers from the B array
#and print result to the console as shown below.

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

#testando se cada elemento de A é maior que o elemento de B
print(A > B)
print(np.greater(A, B))


#Exercise 2 Using Numpy create a 4x4 array filled with zeros
#(set data type to int). In response print this array to the console.

?np.zeros
#pritando uma matrix 4x4 de zeros do tipo inteiro
np.zeros(shape=(4,4), dtype='int8')


#Exercise 3 Using Numpy, create an array 10x10 filled with number 255
#and set the data type to float. Print this array
#to the console as shown below.

#criando uma matriz 10x10 de 1's e multiplicando por 255 cada elemento
np.ones(shape=(10,10)) * 255
#criando uma matriz 10x10 de 0's e somando 255 em cada elemento
np.zeros(shape=(10,10)) + 255

?np.full
#criando uma matriz 10x10 de 255's
#nesse caso como kda elemento da matriz tem 8 bits
#então eles não tem o elemento 255
np.full(shape=(10,10), fill_value=255, dtype='int8')
np.full(shape=(10,10), fill_value=255, dtype='int64')
np.full(shape=(10,10), fill_value=255)
np.full(shape=(10,10), fill_value=255, dtype='float')









