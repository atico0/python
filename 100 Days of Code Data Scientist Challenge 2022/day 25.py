# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:53:15 2022

@author: luisg
"""

import numpy as np

#Exercise 1
#The following arrays are given:

A = np.array(['001', '002', '003'], dtype=np.str)
B = np.array(['XC', 'YC', 'ZC'], dtype=np.str)

#Merge them together as shown below and print result to the console.

?np.char.add
print(np.char.add(A,B))




#Exercise 2
#The following array is given:

A = np.array(['1', '2', '3'], dtype=np.str)


#Add '000' (3 zeros) at the beginning of each element of this
#array as shown below and print result to the console.



print(np.char.add('000',A))

?np.char.rjust
print(np.char.rjust(A, 4, '0'))

?np.char.zfill
print(np.char.zfill(A,4))



#Exercise 3
#The following array is given:

A = np.array([['PLW CDR 11B TEN', 'AMC LPP'],
              ['CDR PKO KGH', 'CCC QMK']], dtype=np.str)

#Split each element of this array by space character as shown below.

?np.char.split

print(np.char.split(A, ' '))
print(np.char.split(A))#Soulção do ex
