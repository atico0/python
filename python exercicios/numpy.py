# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:26:52 2022

@author: luisg
"""
#questões
#https://www.w3resource.com/python-exercises/numpy/index.php

#1.Write a NumPy program to get the numpy version and
#show numpy build configuration

import numpy as np

print(np.__version__)
print(np.show_config())

#2. Write a NumPy program to  get help on the add function
?np.add #isso só funciona no spyder
print(np.info(np.add))


np.add(1,2)
np.add([1,2],[3,4])


#3. Write a NumPy program to test whether
#none of the elements of a given array is zero.

vetor = np.array([1,2,3,0])
vetor
vetor==0

vetor = np.array([1,2,3])

if np.sum(vetor==0):
    print('tem 0')
else:
    print('não tem zero')
np.all(vetor) #resposta dada



#4. Write a NumPy program to test whether any of the 
#elements of a given array is non-zero.

vetor = np.array([1,2,3,0])
vetor
vetor==0

vetor = np.array([1,2,3])
vetor = np.zeros(5)
vetor
if np.sum(vetor!=0):
    print('tem um não 0')
else:
    print('não tem um não 0')
print(np.any(vetor)) #resposta dada


#5. Write a NumPy program to test a given array element-wise
#for finiteness (not infinity or not a Number)

infinito =np.array(1)/np.array(0)
nada = np.nan

np.isfinite(1)
np.isfinite(infinito)
np.isfinite(nada)

vetor = [[1,infinito, nada]]
np.isfinite(vetor)

np.isinf(1)
np.isinf(infinito)
np.isinf(nada)

np.isinf(vetor)
#essa é a função que eu tenho que usar
#pq a outra retorna o mesmo boleano para inf e nan e essa retorna
# o mesmo boleano para um num e nan

np.isinf(vetor)==False #


#6. Write a NumPy program to test element-wise
#for positive or negative infinity.


infinito =np.array(1)/np.array(0)
m_infinito =np.array(-1)/np.array(0)

infinito >0
m_infinito > 0

np.array([infinito,m_infinito])>0


#7. Write a NumPy program to test element-wise
#for NaN of a given array.
vetor = np.array([1,2,-3,infinito, m_infinito, np.nan])
vetor
vetor2 = np.array([1+1j, 1+0j,1,2,-3,infinito, m_infinito, np.nan])
vetor2
np.isnan(vetor)



#8. Write a NumPy program to test element-wise for complex number,
#real number of a given array. Also test whether
#a given number is a scalar type or not.

np.iscomplex(vetor)
np.isreal(vetor)
np.iscomplex(vetor2)
np.isreal(vetor2)


np.isscalar(vetor)
np.isscalar(1)
    


#9. Write a NumPy program to test whether two arrays
#are element-wise equal within a tolerance.


tolerance = 2

abs(np.array([1,2,3,4]) - np.array([1,2,0,0])) <=tolerance


print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))

?np.allclose

print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))
print(np.allclose([1.0, np.nan], [1.0, np.nan]))
print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))



#10. Write a NumPy program to create an element-wise comparison
#(greater, greater_equal, less and less_equal) of two given arrays.

np.greater([1e10,1e-7, 5], [1.00001e10,1e-8, 5])
np.greater_equal([1e10,1e-7, 5], [1.00001e10,1e-8, 5])
np.less([1e10,1e-7, 5], [1.00001e10,1e-8, 5])
np.less_equal([1e10,1e-7, 5], [1.00001e10,1e-8, 5])



#11. Write a NumPy program to create an element-wise comparison
#(equal, equal within a tolerance) of two given arrays.


x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

np.equal(x, y)
np.allclose(x, y)
?np.allclose

#12. Write a NumPy program to create an array with the values
#1, 7, 13, 105 and determine the size of the
#memory occupied by the array.
  
x = np.array([1, 7, 13, 105])
x.size
x.itemsize
x.size * x.itemsize
np.size(x)
?np.size

?x.itemsize

#13. Write a NumPy program to create an array of
#10 zeros,10 ones, 10 fives.

np.array(([0]*10 + [1]*10 + [5]*10))


#14. Write a NumPy program to create an array
#of the integers from 30 to 70.

np.arange(30, 71)


#15. Write a NumPy program to create an array of 
#all the even integers from 30 to 70.

np.arange(30, 71, 2)



#16. Write a NumPy program to create a 3x3 identity matrix.

#criando matriz identidade 3x3
np.eye(3)

#17. Write a NumPy program to generate
#a random number between 0 and 1.

?np.random.random
#pegando um vetor com 3 valores aleatórios entre 0 e 1
np.random.random(3)

?np.random.rand
#pegando um vetor de dim 3x2x4 com valores aleatórios entre 0 e 1
np.random.rand(3,2,4)
#na primeira função nós só controlamos a quant de elementos
#já na segunda nós controlamos as dimensões


?np.random.random_integers
#pegando um vetor com 3 valores aleatórios
#entre 0 e 1 seguindo uma distribuição uniforme discreta
np.random.random_integers(size = 3, low=0, high=1)

?np.random.normal
#pegando um vetor com 3 valores aleatórios
#entre 0 e 1 seguindo uma distribuição normal com média 0 e  var 1
np.random.normal(0,1,3) #essa foi a função da resposta

#18. Write a NumPy program to generate an array of 15 random numbers
#from a standard normal distribution.

?np.random.randn
#pegando uma matrix 3x2 com valores aleatórios entre 0 e 1
np.random.randn(3,5,2)
np.random.normal(0,1,15)
#Na primeira função nos podemos escolher as dimensões e a quantidade 
#mas não os parâmetros das funções já na segunda nos podemos
#escolher os parâmentros e a quant de elementos mas não as dimensões 



#19. Write a NumPy program to create a vector with values ranging
#from 15 to 55 and print all values except the first and last.

vetor = np.random.random_integers(size = 55, low=15, high=55)
vetor
vetor[1:-1]

veotor = np.arange(15,55)
vetor[1:-1]





#20. Write a NumPy program to create a 3X4
#array using and iterate over it.

#criando matriz 3x4 de valores aleatórios| Xij~N(0,1)
matriz = np.random.randn(3,4)
matriz
#iterando sobre as linhas
for i in range(matriz.shape[0]):
    #iterando sobre as colunas
    for j in range(matriz.shape[1]):
        #mostrando elemento da linha i e coluna j
        print(matriz[i,j])































































