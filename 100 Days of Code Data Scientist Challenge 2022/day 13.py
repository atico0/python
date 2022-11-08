# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:29:29 2022

@author: luisg
"""

import numpy as np


#Exercise 1
#The following array is given:

image = np.random.randint(low=0, high=256, size=(200, 300), dtype=np.uint8)

#Sort this array along the rows in ascending order
#and assign to the variable image_sorted.

image = np.random.randint(
    low=0, high=256, size=(200, 300), dtype=np.uint8
)
image_sorted = np.sort(image)





#Exercise 2
#The following array is given:

A = np.array([[4, 2, 1],
              [6, 4, 2]])

#Expand this array by one dimension (add a new dimension at the beginning).
#Expected shape of the output array: (1, 2, 3).

#In response, print array to the console.

A = np.array([[4, 2, 1],
              [6, 4, 2]])
print(np.expand_dims(A, axis=0))





#Exercise 3
#Using Numpy create a three-dimensional array called image with shape
#(200, 300, 3) filled with random values from 0 to 255 (inclusive)
#and data type np.uint8. Set random seed to 42.

#In response, print array to the console.

np.random.seed(42)


image = np.random.randint(0,256, size=(200,300,3), dtype=np.uint8)
print(image)




#Exercise 4
#The following array is given:

image = np.random.randint(low=0, high=256, size=(200, 300, 3),
                          dtype=np.uint8)

#Extend this array by one dimension (add a new dimension at the beginning)
#and assign to image_extended variable.
#Expected shape of this array is (1, 200, 300, 3).

#Tip: Use the np.expand_dims() function.




image_extended = np.expand_dims(image, axis=0)
















































