# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:16:23 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following array is given:

A = np.array([['id', 'price'],
              ['001', 14.99],
              ['002', 4.99],
              ['003', 7.99],
              ['004', 2.49],
              ['005', 1.49]])

#Starting with the second row of this array, randomly shuffle the
#rows and print result to the console.

?np.random.shuffle

np.random.shuffle(A[1:, :])
print(A)




#Exercise 2
#The following array is given:

A = np.array([0.2, 0.15, 0.1, 0.3, 0.2, 0.05])

#Return a list of indexes that sorts this array in ascending order
#and print it to the console.

?np.argsort
print(np.argsort(A))




#Exercise 3
#The following array is given:

A = np.random.randn(10, 8)

#Round the values of this array to three decimal places
#and print result to the console.

print(np.round(A, 3))




#Exercise 4
#Calculate  the roots of the following polynomial:

# w(x) = 4x^2 + 5x + 1

#In response, print these roots to the console.


?np.roots

print(np.roots([4, 5, 1]))






