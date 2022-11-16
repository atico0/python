# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:13:54 2022

@author: luisg
"""


import numpy as np

#Exercise 1
#The following array is given:

A = np.random.randn(8, 4)
A
#Remove the third column and print this array to the console.


?np.delete
print(np.delete(A, 2, axis=1))




#Exercise 2
#A one-dimensional array v (vector) is given:

v = np.array([3, 4, -2])

#Calculate the norm of this vector and print result to the console.
?np.linalg.norm
print(np.linalg.norm(v))



#Exercise 3
#The following array is given:

A = np.random.randint(10, size=(100, 30))

#Set the Numpy option to print only ten edge elements
#and then print this array to the console.

?np.set_printoptions
np.set_printoptions(edgeitems=10)
print(A)


































































