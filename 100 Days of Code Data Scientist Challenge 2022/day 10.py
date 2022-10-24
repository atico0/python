# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:33:00 2022

@author: luisg
"""


import numpy as np

#EXCERCISE 1:
#The following array is given:
#A = np.array([[5, 1, 2, 1, 2],
              #[9, 1, 9, 7, 5],
              #[4, 1, 5, 7, 9]])
#Extract all unique values of this array as a
#list and print it to the console.


A = np.array([[5, 1, 2, 1, 2],
              [9, 1, 9, 7, 5],
              [4, 1, 5, 7, 9]])
#pegando os valores unicos do array
lista = np.unique(A).tolist()
print(lista)

#SOLUÇÃO do exercicio
np.random.seed(10)
A = np.random.randint(low=1, high=10, size=(3, 5))
 
 
print(np.unique(A))






#EXCERCISE 2:
#The following array is given:
#A = np.array([[0.4, 0.3, 0.3],
              #[0.1, 0.1, 0.8],
              #[0.2, 0.5, 0.3]])
#Return a list of indexes with maximum values
#for each row from this array and print it to the console.

A = np.array([[0.4, 0.3, 0.3],
              [0.1, 0.1, 0.8],
              [0.2, 0.5, 0.3],
              [1.0, 2.0, 3.0]])

?np.argmax
#pegando o indice de maior valor do array
np.argmax(A)

#adicionando os indices do maior valor de cada linha numa lista
lista = []
for i in range(A.shape[0]):
    lista.append(np.argmax(A[i]))
print(lista)
#pegando os indices de maior valor de cada coluna
print(np.argmax(A, axis=0))
#Solução do exercicio    
print(np.argmax(A, axis=1))




#EXCERCISE 3:
#The following array is given:
#A = np.array([[4.99, 3.49, 9.99],
              #[1.99, 9.99, 4.99],
              #[14.99, 2.39, 7.29]])
#Sort this array:
#by row (ascending)
#by column (ascending)
#And print result to the console as shown below.


A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])
?np.sort

#colocando o array em ordem crescente por linha (o padrão é axis=1)
print(np.sort(A))
#colocando o array em ordem crescente por coluna
print(np.sort(A, axis=0))
##colocando o array em ordem crescente por linha
print(np.sort(A, axis=1))



#EXCERCISE 4:
#Extract all elements from the following array with
#a value greater than 8 and print result to the console.
#A = np.array([[4.99, 3.49, 9.99],
              #[1.99, 9.99, 4.99],
              #[14.99, 2.39, 7.29]])

A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])

#pegando valores do array maior que 8
print(A[A > 8])






























