# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:03:47 2022

@author: luisg
"""

#questões
#https://www.udemy.com/course/100-days-of-code-data-scientist-challenge/learn/quiz/5601174#overview


#Exercise 1 Check if the following array has missing data (np.nan):

import numpy as np
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

?np.isnan

#checando se A tem algum elemento nulo
print(np.isnan(A))


#Exercise 2 Check if the following arrays are equal (element-wise):

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

?np.allclose

#checando se (dentro de uma tolerância) A e B são iguais
print(np.allclose(A, B))


#Exercise 3 Check if the following arrays are equal (element-wise):

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])

#testando se os elementos de A e B são iguais
print(A == B)
print(np.equal(A, B))












