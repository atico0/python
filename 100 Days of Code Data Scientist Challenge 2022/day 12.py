# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:47:25 2022

@author: luisg
"""





import numpy as np
#Exercise 1
#The following array is given:


A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])


#Using Numpy create an array of the same shape and data type as the
#given array and fill it with a constant value = 9.99.
#Print this array to the console.


print(np.full_like(A, 9.99))



#Exercise 2
#Using Numpy create a two-dimensional array (lower triangular matrix):

print(np.tri(5,5,0))
print(np.tri(5))


#Using Numpy create any 3-dimensional array with shape
#(2, 3, 4) and assign to variable A.





A = np.array([[[4, 5, 4, 2],
           [6, 3, 5, 1],
           [5, 2, 1, 2]],
 
          [[7, 2, 3, 1],
           [6, 2, 0, 9],
           [0, 1, 9, 1]]])


print(A)




#Exercise 4
#Using Numpy create a two-dimensional array with shape of (200, 300)
#filled with random values from 0 to 255 (inclusive) with data
#type np.uint8 and assign to the variable image.



image = np.random.randint(0, 255, 200*300, dtype=np.uint8).reshape(200,300)

image = np.random.randint(
    low=0, high=256, size=(200, 300), dtype=np.uint8
)


