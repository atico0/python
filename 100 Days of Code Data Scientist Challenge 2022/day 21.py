# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 09:40:46 2022

@author: luisg
"""



import numpy as np

#Exercise 1
#The following array (square matrix) is given:

A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])

#Calculate eigenvalues and their corresponding eigenvectors of this matrix
#and print to the console as shown below.


autovalores, autovetores = np.linalg.eig(A)
print(autovalores)
print(autovetores)




#Exercise 2
#The following array (square matrix) is given:

A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])

#Find the inverse matrix to this matrix and print it to the console.


print(np.linalg.inv(A))



#Exercise 3
#The following array (square matrix) is given:

A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])

#Find the trace of this matrix (sum of elements on the main diagonal)
#and print result to the console.


print(np.trace(A))

print(np.sum(np.linalg.eig(A)[0]))
#matematicamente devia ter dado o mesmo mas deu uma pequena diferença




#Exercise 4
#The following arrays are given:

A = np.array([[2, 0],
              [4, 2],
              [5, 3],
              [4, 2]])
B = np.array([[4, 0, 2, 1, 1, 0, 2, 9]])

#Shapes of these arrays:

#A - 4x2

#B - 1x8

#Transform B array to perform the matrix multiplication A x B.
#Then perform this multiplication and print result to the console.




B = B.reshape(-1,4)

print(np.dot(A, B))





















v








