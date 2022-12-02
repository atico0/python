# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:52:06 2022

@author: luisg
"""

import numpy as np
import pandas as pd

#Exercise 1
#The following quotations Series is given:

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)

#Add two elements to this Series:

#key: 'BBT', value: 25.5

#key: 'F51', value: 19.2

#In response, print quotations Series to the console.

quotations['BBT'] = 25.5
quotations['F51'] = 19.2
print(quotations)
#SOLUÇÃO DO EXERCICIO
quotations = quotations.append(pd.Series({'BBT': 25.5, 'F51': 19.2}))
print(quotations)


#Exercise 2
#Convert the following quotations Series:

stocks = {
    'PLW': 387.00,
    'CDR': 339.5,
    'TEN': 349.5,
    '11B': 391.0,
    'BBT': 25.5,
    'F51': 19.2,
}
quotations = pd.Series(data=stocks)

#to DataFrame. Reset the index and name the columns 'ticker'
#and 'price' respectively.

#In response, print this DataFrame to the console.


quotations = pd.DataFrame(quotations)

quotations = quotations.reset_index()
quotations.columns  = ['ticker', 'price']
print(quotations)




#Exercise 3
#Create the following DataFrame object and assign it
#to the companies variable:

#     company   price   ticker
#0     Amazon  2375.0  AMZN.US
#1  Microsoft   178.6  MSFT.US
#2   Facebook   179.2    FB.US

#In response, print companies DataFrame to the console.


dicio = {'company':['Amazon', 'Microsoft', 'Facebook'],
         'price':[2375.0, 178.6, 179.2],
         'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']}

companies = pd.DataFrame(dicio)
print(companies)


#conta que tia catita pediu pra fz
28.70 + 15 + 26.43 + 16 +7.27

