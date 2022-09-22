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




























































































































