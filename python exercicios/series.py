# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 08:27:05 2022

@author: luisg
"""


#https://www.w3resource.com/python-exercises/pandas/index-data-series.php 
#(fonte dos exercicios)
import numpy as np
import pandas as pd

#Q1
serie = pd.Series(range(10))
print(serie )
#?pd.Series
#?pd.DataFrame


#Q2
print(serie.tolist(), type(serie), type(serie.tolist()))

#Q3
serie1 =  pd.Series( [2, 4, 6, 8, 10])
serie2 = pd.Series([1, 3, 5, 7, 9])
print(serie1+serie2)
print(serie1-serie2)
print(serie1*serie2)
print(serie1/serie2)

#Q4asd
serie1 = pd.Series([2, 4, 6, 8, 10])
serie2 = pd.Series([1, 3, 5, 7, 10])
print(serie1 == serie2)
print(serie1 < serie2)
print(serie1 > serie2)

#Q5
dicio = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(dicio)
serie = pd.Series(dicio)
print(serie)

#Q6
vetor = np.array([10, 20, 30, 40, 50])
print(vetor)
serie = pd.Series(vetor)
print(serie)


#Q7
serie = pd.Series([100, 200, 'python', 300.12, 400])
#poderia ter feito uma serie só com strings
print(serie)
serie2 = pd.to_numeric(serie, errors='coerce')
print(serie2)

#Q8
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0],
     'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
serie = pd.Series(df['col1'])
print(serie)

#Q9
serie = pd.Series([100, 200, 'python', 300.12, 400])
vetor1 = np.array(list(serie))
print(vetor1)
vetor2 = np.array(serie.values.tolist())
print(vetor2)
print(serie.values.tolist())


#Q10
serie1 = pd.Series([['red', 'green', 'white'], ['red', 'black'], ['yellow']])
print(serie1)

serie2 = serie1.apply(pd.Series).stack().reset_index(drop=True)
print(serie2)
serie2 = serie1.apply(pd.Series).stack()
print(serie2)

#?stack

#Q11
serie1 = pd.Series(['200', 'python', '300.12', '400'])
print(serie1)
serie1.sort_values()


#Q12
serie1 = pd.Series(['200', 'python', '300.12', '400'])
serie1[4] = '500'
serie1[5] = 'php'
#método alternativo
serie1 = serie1.append(pd.Series(['4', 'php']))


print(serie1)


#Q13
serie1 = pd.Series(range(11))
serie1
serie1[serie1<=5]

#Q14
serie = pd.Series(data=range(1, 6), index = 'A B C D E'.split())
serie
serie.index = 'B A C D E'.split()
serie
#método alternativo
seire = serie.reindex(index = 'B A C D E'.split())


#Q15
a = list(range(1,10))
a.extend([5,3])
print(a)
serie = pd.Series(data = a)
serie.mean()
serie.std()



#Q16


sr1 = pd.Series(list(range(1,6)))
sr2 = pd.Series(list(range(2,11,2)))
sr1
sr1[~sr1.isin(sr2)]












































