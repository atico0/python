# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:50:21 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following arrays are given:

A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])

#Calculate arithmetic means of these arrays (elementwise)
#and print result to the console.


print((A+B)/2)
print(np.divide(np.add(A, B), 2))#solução do exercicio






#Exercise 2
#The following arrays are given:

A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])

#Multiply these arrays (elementwise) and print result to the console.


print(np.multiply(A, B))
print(A*B)



#Exercise 3
#The following array is given:

A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])

#Calculate the square root of each element of this
#array and print result to the console.

print(np.sqrt(A))


































































