# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:14:34 2022

@author: luisg
"""

#questões:
#https://www.w3resource.com/graphics/matplotlib/

#1. Write a Python program to draw a line with suitable
#label in the x axis, y axis and a title.

import matplotlib.pyplot as plt

import numpy as np
x = range(50)
y = [value * 3 for value in x]

x
y


plt.plot(x, y, 'b') # 'r' é a cor vermelha (red)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
plt.show()



#2. Write a Python program to draw a line using given axis 
#values with suitable label in the x axis , y axis and a title.

x = [1, 2, 3]
y = [2, 4, 1]
plt.plot(x, y, 'b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
plt.show()


#3. Write a Python program to draw a line using given axis values 
#taken from a text file, with suitable
#label in the x axis, y axis and a title
with open('E:\\cursos anotações\\python exercicios\\teste.txt') as f:
    texto = f.read()
    print(texto)

linhas = texto.split('\n')
linhas
x = [int(linha.split(' ')[0]) for linha in linhas]
y = [int(linha.split(' ')[1]) for linha in linhas]

x
y

plt.plot(x, y, 'r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('esse foi demorado')
plt.show()



#4. Write a Python program to draw line charts of the 
#financial data of Alphabet Inc. between
#October 3, 2016 to October 7, 2016. 
import pandas as pd

df = pd.read_csv('E:\\cursos anotações\\python exercicios\\fdata.csv',
                 sep = ';', parse_dates=True,index_col=0)

?pd.read_csv
df.head()

df.plot()













































