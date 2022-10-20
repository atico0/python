# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:05:53 2022

@author: luisg
"""
import numpy as np


#Exercise 1: Using Numpy create and convert the following
#array into the list:

#array([[ 0,  1,  2,  3],
       #[ 4,  5,  6,  7],
       #[ 8,  9, 10, 11]])
#In response, print list to the console.

#definindo vetor
vetor = np.array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
#printando o vetor convertido para lista
print(vetor.tolist())


#Exercise 2: The following array is given:

#array([[ 0,  1,  2,  3],
 #      [ 4,  5,  6,  7],
  #     [ 8,  9, 10, 11]])
  
#Using the slice operator, transform this array into the following:
    
#array([[ 8,  9, 10, 11],
 #      [ 4,  5,  6,  7],
  #     [ 0,  1,  2,  3]])
#In response, print transformed array to the console.

#criando um vetor de 0 a 11 e colocando ele para dimensões 3x4
vetor = np.arange(12).reshape(3, -1)
vetor

#mostrando esse vetor numa outra ordem
print(vetor[[2,1,0]])
#mostrando esse vetor na ordem contrária
print(vetor[::-1])


#The following array:

#array([[1., 1., 1., 1.],
       #[1., 1., 1., 1.],
       #[1., 1., 1., 1.],
       #[1., 1., 1., 1.]])

#transform to this array:

#array([[0., 0., 0., 0., 0., 0.],
       #[0., 1., 1., 1., 1., 0.],
       #[0., 1., 1., 1., 1., 0.],
       #[0., 1., 1., 1., 1., 0.],
       #[0., 1., 1., 1., 1., 0.],
       #[0., 0., 0., 0., 0., 0.]])
#In response, print transformed array to the console.

#criando matriz 4x4 de uns
vetor = np.ones(shape=(4,4))
?np.pad

#faz um vetor com n dimensões (nas linhas e nas colunas) 
#em que os elementos extras são zeros
#n=1
print(np.pad(vetor, 1))
#n=2
print(np.pad(vetor, 2))
#n=3
print(np.pad(vetor, 3))








































