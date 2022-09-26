# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:14:34 2022

@author: luisg
"""

#questões:
#https://www.w3resource.com/graphics/matplotlib/

#1. Write a Python program to draw a line with suitable
#label in the x axis, y axis and a title.

import matplotlib.pyplot as plt #importando blbliotecas
import pandas as pd
import numpy as np


x = range(50) #criando valores para x e y
y = [value * 3 for value in x] #definindo y = 3*x
print(x)
print(y)


#definindo primeiro grafico
plt.plot(x, y, 'b') # 'r' é a cor vermelha (red)
#colocando as legendas nos eixos e titulo
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
#mostrando gráfico
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
with open('C:\\Users\\luisg\\OneDrive\\Documentos\\GitHub\\python\\python exercicios\\teste.txt') as f:
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

#5. Write a Python program to plot two or more lines on same
#plot with suitable legends of each line.


#definindo x e y1 = 3*x + 10 e y2 = x**2
x = np.array(list(range(100)))
y1 =  3*x + 10
y2 = x**2
y1
y2

#definindo os 2 gráficos 
plt.plot(x, y1, label='linha1')
plt.plot(x, y2, label='linha2')
#colocando as legendas nos gráficos
plt.legend()
#mostrando gráfico
plt.show()


#6. Write a Python program to plot two or more lines with legends,
#different widths and colors.

#definindo x e y1 = 3*x + 10 e y2 = x**2
x = np.array(list(range(100)))
y1 =  3*x + 10
y2 = x**2
print(y1)
print(y2)

#definindo os graficos com diferentes cores e espessuras
plt.plot(x, y1, label='linha1 - width 5', 
         linewidth  = 5, color = 'black')
plt.plot(x, y2, label='linha2 - width 10', 
         linewidth  = 10, color = 'red')
#titulo e nomes dos eixos e 
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('ESPESSURA')
plt.legend()
plt.show()


#7. Write a Python program to plot two or more
#lines with different styles.


#definindo x e y1 = 3*x + 10 e y2 = x**2
x = np.array(list(range(100)))
y1 =  3*x + 10
y2 = x**2
print(y1)
print(y2)

#definindo os graficos com diferentes estilos
plt.plot(x, y1, label='dois pontos', 
         linewidth=3, linestyle=':')
plt.plot(x, y2, label='traços ponto', 
         linewidth=3,  linestyle='-.')
plt.title('ESTILOS')
plt.show()


#8. Write a Python program to plot two or more lines
#and set the line markers.

#definindo x e y1 = 3*x + 10 e y2 = x**2
x = [10, 20, 30]
y1 =  [3*i + 10 for i in x]
y2 = [i**2 for i in x]
print(y1)
print(y2)

#definindo os graficos com diferentes cores e espessuras
plt.plot(x, y1, label='linha1', linestyle=':', 
         linewidth  = 3, marker='o',
         markerfacecolor='green', markersize=10)
plt.plot(x, y2, label='linha2', linestyle='-.', 
         linewidth  = 3, marker='o',
         markerfacecolor='green', markersize=10)
#titulo e nomes dos eixos e 
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('MARCADORES')
#adicionando legendas
plt.legend()
#mostrando gráficos
plt.show()





#9. Write a Python program to display the current
#axis limits values and set new axis values.





x = [10, 20, 30]
y1 =  [3*i + 10 for i in x]
y2 = [i**2 for i in x]
print(y1)
print(y2)

#definindo os graficos
plt.plot(x, y1, label='linha1')
plt.plot(x, y2, label='linha2')
#colocando limites nos eixos (os dois primeiros são para o y1)
plt.axis([0, 300, 0, 500])
#titulo e nomes dos eixos e 
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('LIMITES')
#adicionando legendas
plt.legend()
#mostrando gráficos
plt.show()












