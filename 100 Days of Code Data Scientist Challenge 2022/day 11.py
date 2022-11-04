# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:53:54 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following array is given:

#A = np.array([[4.99, 3.49, 9.99],
 #             [1.99, 9.99, 14.99],
  #            [14.99, 2.39, 7.29]])

#Replace elements greater than 10 with a fixed value = 10.0
#and print result to the console.



A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

np.where(A>10)
A[np.where(A>10)] = 10
print(A)



#Exercise 2
#Present the following two-dimensional array as a flattened
#one-dimensional array and print result to the console.


A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

print(np.ravel(A))



##Exercise 3
#The following array is given:

A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])

#Using Numpy create an array of the same shape and data type as the given
#array and fill it with zeros. Print this array to the console.


print(np.zeros_like(A))



























































