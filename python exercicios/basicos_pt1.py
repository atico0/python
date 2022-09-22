# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:04:37 2022

@author: luisg
"""

#questões
#https://www.w3resource.com/python-exercises/python-basic-exercises.php


#1. Write a Python program to print the following string in a specific format

print( '''
      Twinkle, twinkle, little star,
          How I wonder what you are!
              Up above the world so high,
              Like a diamond in the sky.
      Twinkle, twinkle, little star,
      How I wonder what you are''')

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


#2. Write a Python program to get the Python version you are using.

import sys
print("Python version")
print(sys.version)
print("python info")
print(sys.version_info)

#3. Write a Python program to display the current date and time.
import datetime

print('current date and time')
print(datetime.datetime.now())




#4. Write a Python program which accepts the radius of a circle
#from the user and compute the area
import math


raio = float(input('Digite o raio do circula: '))
area = math.pi*raio**2
print(f'a área desse circulo é: {area}')


#5. Write a Python program which accepts the user's first and last
#name and print them in reverse order with a space between them.


prim, ult = input('Digite o seu primeiro e ultimo nome: ').split()

print(f'Olá, {ult} {prim}')

print('Olá, ' + ult,prim)



#6. Write a Python program which accepts a sequence of comma-separated
#numbers from user and generate a list and a tuple with those numbers.

numeros = list(input('Digite um conjunto de números: ').split(','))
tupla = tuple(numeros)
numeros
tupla

#7. Write a Python program to accept a filename
#from the user and print the extension of that.


arquivo = input('Digite o nome do arquivo: ').split('.')
arquivo[1]


#8. Write a Python program to display the first and last
#colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
color_list[0]
color_list[-1]


#9. Write a Python program to display the examination schedule.
#(extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
print(f'''The examination will start from:
      {exam_st_date[0]}/ {exam_st_date[1]}/ {exam_st_date[2]}''')


#10. Write a Python program that accepts an
#integer (n) and computes the value of n+nn+nnn.
n = input('Digite um número: ')
print(int(n) + int(n + n) + int(n + n + n))


#11. Write a Python program to print the documents 
#(syntax, description etc.) of Python built-in function(s).

print(help(abs))
print(abs.__doc__)


#12. Write a Python program to print the calendar
#of a given month and year. Note : Use 'calendar' module.

import calendar
    
calendar.Calendar().yeardatescalendar(year=2022)
calendar.Calendar().monthdatescalendar(2022, 5)

ano = int(input('Digite ano: '))
mes= int(input('Digite mês: '))
print(calendar.month(ano,mes))









