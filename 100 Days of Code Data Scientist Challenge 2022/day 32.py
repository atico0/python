# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:40:21 2022

@author: luisg
"""


import numpy as np
import pandas as pd

#Exercise 1
#The following Series is given (quotations variable):

#PLW    387.0
#CDR    339.5
#TEN    349.5
#11B    391.0
#dtype: float64

#Convert the quotations to the DataFrame and set the column name to 'price'.
#In response, print this DataFrame to the console.

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)

quotations = pd.DataFrame(quotations, columns=['price'])
print(quotations)



#Exercise 2
#Using the numpy and pandas create the following Series:

#101    10.0
#102    20.0
#103    30.0
#104    40.0
#105    50.0
#106    60.0
#107    70.0
#108    80.0
#109    90.0
#dtype: float64

#In response, print this Series to the console.


index = np.arange(101, 110)
valor = np.arange(10, 100, 10)
print(pd.Series(valor, index=index))



#Exercise 3
#The following Series is given:

series = pd.Series(['001', '002', '003', '004'], list('abcd'))

#Convert its type to int and print this Series to the console.

series = pd.Series(series, dtype='int')
print(series)

#SOLUÇÃO DO EXERCICIO
series = pd.to_numeric(series)
print(series)






