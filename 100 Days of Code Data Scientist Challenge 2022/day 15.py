# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:03:44 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following array is given:

#array([[ 0,  1,  2,  3],
       #[ 4,  5,  6,  7],
       #[ 8,  9, 10, 11]])

#Using the slice operator, transform this array into the following:

#array([[ 3,  2,  1,  0],
       #[ 7,  6,  5,  4],
       #[11, 10,  9,  8]])

#In response, print transformed array to the console.


A = np.arange(12, dtype='int').reshape(-1, 4)

print(A[0::, ::-1])




#Exercise 2
#The following  array is given:

#array([[ 0,  1,  2,  3],
       #[ 4,  5,  6,  7],
       #[ 8,  9, 10, 11]])

#Using the slice operator, transform this array into the following:

#array([[11, 10,  9,  8],
       #[ 7,  6,  5,  4],
       #[ 3,  2,  1,  0]])

#In response, print transformed array to the console.

A = np.arange(12, dtype='int').reshape(-1, 4)

print(A[::-1, ::-1])






#Exercise 3
#Random seed is set to 42. The following array is given:

np.random.seed(42)
image = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8)

#Extract the first channel (index 0) of this image array
#and print it to the console.


image[:, :, 0]




#Exercise 4
#The following array is given:

image = np.random.randint(
    low=0, high=256, size=(10, 10, 3), dtype=np.uint8
)


#Extract any array of shape (5, 5, 3) from this
#array and assign to the result variable.



image[:5, :5, :3]














