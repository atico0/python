# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:08:32 2022

@author: luisg
"""
import numpy as np

#Exercise 1
#Two randomly generated arrays are given:

image1 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)
image2 = np.random.randint(
    low=0, high=256, size=(200, 300, 3), dtype=np.uint8
)


#Expand each of these arrays by adding one dimension at the beginning
#and then combine these arrays into one called images.
#Expected shape of images array: (2, 200, 300, 3).

image1 = np.expand_dims(image1, axis=0)
image2 = np.expand_dims(image2, axis=0)
image1.shape

images = np.append(image1, image2, axis=0)


#Exercise 2
#The following array is given:

A = np.array([[[1, 2, 3],
               [6, 3, 2]]])

#Shape of this array is (1, 2, 3). Remove the unnecessary first dimension
#and extract (2, 3) array and print it to the console as shown below.



?np.squeeze

print(np.squeeze(A, axis=0))



#Exercise 3
#The following array is given:

A = np.array([[0.4],
              [0.9],
              [0.5],
              [0.6]])


#Shape of this array is (4, 1). Remove the unnecessary dimension and extract
#(4, ) array and print result to the console.



print(np.squeeze(A, axis=1))




























