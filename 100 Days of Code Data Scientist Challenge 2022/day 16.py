# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:53:28 2022

@author: luisg
"""

import numpy as np



#Exercise 1
#The following arrays are given:

A = np.array([[3, 4, 5],
              [8, 3, 1]])
B = np.array([[0, 5, 2],
              [4, 2, 1]])

#Concatenate these arrays as follows:

#array([[3, 4, 5],
       #[8, 3, 1],
       #0, 5, 2],
       #[4, 2, 1]])

#In response, print this array to the console.
?np.concatenate
print(np.concatenate((A,B), axis=0))




#Exercise 2
#The following arrays are given:

data = np.array([[4.3, 4.2],
                 [3.1, 3.6]])
target = np.array([[0],
                   [1]])

#Concatenate these arrays into one as shown below:

#array([[4.3, 4.2, 0. ],
       #[3.1, 3.6, 1. ]])

#In response, print this array to the console.


print(np.concatenate((data, target), axis=1))



#Exercise 3
#The following three one-dimensional arrays are given:

feature1 = np.array([1.6, 0.9, 2.2])
feature2 = np.array([0.4, 1.3, 3.2])
feature3 = np.array([1.4, 0.3, 1.2])


#Transform each of these arrays into a column and concatenate them into one
#array as shown below. In response, print this array to the console.

?np.column_stack

print(np.column_stack((feature1, feature2, feature3)))








































