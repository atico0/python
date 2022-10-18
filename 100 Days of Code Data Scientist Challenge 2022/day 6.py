# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:15:19 2022

@author: luisg
"""

import numpy as np



#Exercise The following array is given:
#Iterate through this array and print each element to the console.

A = np.array([[1, 4, 3],
              [5, 2, 6]])
?np.nditer

#iterando sobre A
for c in np.nditer(A):
    print(c)


#Exercise 2 Using Numpy create a one-dimensional array
#(vector) consisting of eleven equally
#distributed numbers from the [0,1] interval.


#criando um vetor igualmente espaçado de 0 a 1 com 11 elementos
print(np.linspace(start=0, stop=1, num=11))



#Exercise 3 Using Numpy create a one-dimensional array (vector)
#containing the possible result from the Big Lotto game.
#Set the random seed to 42. Print result to the console.


?np.random.randint
#escolhendo 6 números aleatórios de 1 a 50 (tem repetição)
print(np.random.randint(low=1, high=49, size=6))

?np.random.choice
#escolhendo 6 números aleatórios de 1 a 50 sem repetição
print(np.random.choice(range(1,50), size=6, replace=False))








