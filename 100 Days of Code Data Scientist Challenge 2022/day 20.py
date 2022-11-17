# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:02:00 2022

@author: luisg
"""

import numpy as np


#Exercise 1
#The following arrays are given:

A = np.linspace(0, np.pi / 2, 20)
B = np.full(shape=(20,), fill_value=1, dtype='float')

#Check the Pythagorean formula for sines and cosines on the A array and
#then compare the result with the B array.
#Use the np.allclose() function in this exercise.

#In response, print result to the console.

A
B


print(np.allclose((np.sin(A)**2)+ (np.cos(A)**2), B))


#Exercise 2
#The following arrays are given:

A = np.array([[2, 3],
              [-4, 2],
              [5, 0]])
B = np.array([[4, 3, 2],
              [-1, 0, 2]])

#Shapes of these arrays:

#A - 3x2

#B - 2x3

#Perform matrix multiplication A x B and print result to the console.


print(np.dot(A, B))
print(A.dot(B))#solução do exercicio




#Exercise 3
#The following array (square matrix) is given:

A = np.array([[-2, 0, 4],
              [5, 2, -1],
              [-4, 2, 4]])

#Calculate the determinant of this matrix and print it to the console.




print(np.linalg.det(A))
























































