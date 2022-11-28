# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:30:25 2022

@author: luisg
"""

import pandas as pd

#Exercise 1
#Using pandas, from the list below:

stocks = ['PLW', 'CDR', '11B', 'TEN']

#create a Series object and print it to the console.

print(pd.Series(stocks))
#SOLUÇÃO DO EXERCICIO
print(pd.Series(data=stocks))



#Exercise 2
#Using pandas, from the dictionary below:

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}

#create a Series object and assign it to the quotations variable.
#In response, print quotations variable to the console.

quotations = pd.Series(stocks)
print(quotations )
#SOLUÇÃO DO EXERCICIO
quotations = pd.Series(data=stocks)
print(quotations)





#Exercise 3
#The following Series is given (quotations variable):

#PLW    387.0
#CDR    339.5
#TEN    349.5
#11B    391.0
#dtype: float64

#Convert quotations to the list and print it to the console.

stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)
print(list(quotations))

#SOLUÇÃO DO EXERCICIO
quotations = quotations.tolist()
print(quotations)





