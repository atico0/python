# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 15:03:50 2023

@author: luisg
"""

import numpy as np
import pandas as pd



#Exercise 1
#Create the DatetimeIndex object containing the dates in the
#format yyyy-mm-dd hh: mm: ss for January 1, 2021 with a time
#interval of 1h and assign to the variable date_range.
#In response, print this variable to the console.

?pd.date_range

date_range = pd.date_range(start='2021-01-01 01:00:00',
                           end='2021-01-01 23:59:59',freq='1H')

print(data_range)

#SOLUÇÃO DO EXERCÍCIO (NÃO SEI PQ O MEU TÁ DANDO COMO DIFERENTE)
date_range = pd.date_range(start='2021-01-01', periods=24, freq='H')
print(data_range)




#Exercise 2
#Create the following DataFrame object and print it to the console.

c1 = pd.date_range(start='2021-03-01', periods=31)
c2 = np.arange(60, 91)
print(pd.DataFrame({'day':c1, 'day_of_year':c2}))

#SOLUÇÃO DO EXERCÍCIO
date_range = pd.date_range(start='2021-03-01', periods=31)
df = pd.DataFrame(data=date_range, columns=['day'])
df['day_of_year'] = df['day'].dt.dayofyear
print(df)






#Exercise 3
#The following dictionary is given:

data_dict = {
    'normal': np.random.normal(loc=0, scale=1, size=1000),
    'uniform': np.random.uniform(low=0, high=1, size=1000),
    'binomial': np.random.binomial(n=1, p=0.2, size=1000)
}


#Create the DateFrame object from this dictionary and assign it to
#the df variable. As an index, add a dates from 2020-01-01 as shown below.
#In response print this DataFrame to the console.


date_range = pd.date_range(start='2020-01-01', end='2022-09-26')

df = pd.DataFrame(data=data_dict, index=date_range)
print(df)

#SOLUÇÃO DO EXERCICIO
df = pd.DataFrame(
    data=data_dict, index=pd.date_range('2020-01-01', periods=1000)
)
print(df)
