# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:34:25 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following two-dimensional array is given:

A = np.random.randint(low=0, high=7, size=(5, 8))
A[:, :2] = 0
A[:, -2:] = 1
A

#Split this array into three parts:

#the first two columns assign to the A1 variable

#the next four columns assign to the A2 variable

#the last two columns assign to the A3 variable

#In response, print these arrays to the console as shown below.

?np.split

A1, A2, A3 = np.split(A, [2, 6], axis=1)
print(A1)
print(A2)
print(A3)


#Exercise 2
#The following array is given:

A = np.random.randint(low=0, high=2, size=(10, 6))

#Calculate the total number of non-zero elements in this
#array and print it to the console.



print(np.count_nonzero(A))



#Exercise 3
#The following array is given below:

A = np.random.randn(10, 4)

#Set the Numpy option to print arrays with specified precision.
#Set precision to 4 and print this array

A
?np.set_printoptions
np.set_printoptions(precision=4)
print(A)




#Exercise 4
#The following array is given:

A = np.array([1.2e-6, 1.7e-7])

#Set the precision to 8 and also set the appropriate Numpy option to suppress
#mathematical notation and print this array to the console.


np.set_printoptions(precision=8, suppress=True)
print(A)












