# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:05:03 2022

@author: luisg
"""


import numpy as np
import pandas as pd



#Exercise 1
#Convert the first column of the companies DataFrame to index.
#In response, print companies DataFrame to the console.

data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}



companies = pd.DataFrame(data_dict)
companies.index = companies['company']
companies.drop('company', axis=1, inplace=True)
print(companies)

#Solução do exercicio
companies = companies.set_index('company')
print(companies)



#Exercise 2
#Create the DatetimeIndex object containing the yyyy-mm-dd format
#dates for all days from January 2020 and assign it to
#the date_range variable. In response, print this variable to the console.


?pd.date_range
date_range = pd.date_range(start='2020-01-01', periods=31)
print(date_range)




#Exercise 3
#Create the DatetimeIndex object containing the dates in the yyyy-mm-dd
#format for all Mondays from 2020 and assign it to the date_range variable.
#Print this variable to the console.

#SOLUÇÕES DO EXERCICIO
date_range = pd.date_range(start='2020-01-01', periods=52, freq='W-MON')
print(date_range)

date_range = pd.date_range(
    start='2020-01-01', end='2020-12-31', freq='W-MON'
)
print(date_range)






















