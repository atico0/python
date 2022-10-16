# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:04:37 2022

@author: luisg
"""

#questões
#https://www.w3resource.com/python-exercises/python-basic-exercises.php


#1. Write a Python program to print the
#following string in a specific format

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



#13. Write a Python program to print the following 'here document'.



with open('here doc.txt') as f:
    texto = f.read()
    print(texto)


print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')



#14. Write a Python program to calculate
#number of days between two dates.


data1 = (2014, 7, 2)
data2 = (2014, 7, 11)

dif = abs((data1[0] - data2[0]) * 365 + (data1[1] - data2[1]) * 30 + 
      (data1[2] - data2[2])) 
#esse jeito tá errado pq nem todo mês tem 30 dias

import datetime

data1 = datetime.date(2010, 7, 2)
data2 = datetime.date(2014, 7, 11)

dif = abs(data1 - data2)
print(dif)


#15. Write a Python program to get the
#volume of a sphere with radius 6.

from math import pi

#inputando o raio da esfera
raio = float(input('Digite o raio da esfera: '))
#calculando o volume
vol = (3/4)*pi*raio**3
#pritando o volume
print(vol)

#fazendo a mesma coisa acima como uma função
def vol_esfera(raio):
    volume = (3/4)*pi*raio**3
    return volume

#testando a função
vol_esfera(1)


#16. Write a Python program to get the difference between
#a given number and 17, if the number is greater than 17 return
#double the absolute difference.

#pegando o input de um número real
num = float(input('Digite um número: '))

#calculando a diferença entre num é 17
dif = num - 17

#checando se um número é maior que 17
if num > 17:
    #retornando 2 vezes a difenrença entre num e 17
    dif = 2 * dif
else:
    #calculando o valor absoluto da diferença entre num e 17
    dif = abs(dif)
print(dif)

#fazendo a mesma coisa que acima mas como uma função
def dif_17(num):
    dif = num - 17
    if num > 17:
        result = 2 * dif
    else:
        result = abs(dif)
    return result

dif_17(1)
dif_17(17)
dif_17(18)
dif_17(20)


#17. Write a Python program to test whether a number
#is within 100 of 1000 or 2000.

def proximo(n):
    #testando se a distância entre 1000 ou
    #2000 e n é menor igual que 100
    teste = abs(1000-n) <=100 or abs(2000-n) <=100  
    #retornando o resultado do teste
    return teste

proximo(1000)
proximo(1100)
proximo(1200)
proximo(2000)
proximo(1900)


#18. Write a Python program to calculate the sum of
#three given numbers, if the values are equal then
#return three times of their sum.

#pegando números
n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))

#vendo se são iguais
if n1 == n2 == n3:
    #calculando o triplo da soma 
    print(3 * (n1 + n2 + n3))
else:
    #calculando a soma
    print(n1 + n2 + n3)
    
    
    
#19. Write a Python program to get a new string from a 
#given string where "Is" has been added to the front. 
#If the given string already begins with  "Is" then return
#the string unchanged. Go to the editor


def add_is(string):
    #vendo se a string começa com 'Is'
    if string[:2] == 'Is':
        #retornando a string
        return string
    #adicionando 'Is no começo da string
    return 'Is' + string
#testando função
add_is('asdasd')
add_is('Isasdasdsa')
add_is('Is')
add_is('B')
'B'[:2]


#20. Write a Python program to get a string which is n
#(non-negative integer) copies of a given string.


def n_string(string, n):
    #testtando se o número é não negativo
    if n<0:
        print('Não aceitamos valores negativos')
        return ''
    #retornando a string repetida n vezes
    return string * n

#testtando a função
n_string('string', 3)
n_string('string', 0)
n_string('string', -1)



#21. Write a Python program to find whether
#a given number (accept from the user) is even or
#odd, print out an appropriate message to the user.


def par_impar(num):
    #testando se o resto da divisão entre num e 2 é diferente de 0
    if num % 2:
        print('é impar')
    else:
        print('é par')

#testando a função
par_impar(1)
par_impar(-1)
par_impar(2)
par_impar(-2)
par_impar(0)


#22. Write a Python program to count the
#number 4 in a given list.

#definindo lista
lista = [1,2,3,4,5,6,4,1,3]

#contando a quantidade de 4's (jeito mais rapido)
lista.count(4)

def contar(lista, num):
    #definindo contador
    cont = 0
    #percorrendo a lista
    for i in lista:
        #testando se o i-ésimo número da lista é igual a num
        if i == num:
            #incrementando o contador
            cont += 1
    return cont
contar(lista, 4)

contar([1,1,1,4,5,6,1,1], 1)


#23. Write a Python program to get the n (non-negative integer)
#copies of the first 2 characters of a given string.
#Return the n copies of the whole string if the length is less than 2.

def string_copias(string, n):
    #vendo se a string é maior igual a 2
    if len(string) >= 2:
        #retornando os 2 primeiros chars da string repetidas n vezes
        return string[:2] * n
    #retornando a string repetida n vezes
    return string * n
    
#testando função
string_copias('abc', 2)
string_copias('abc', 3)
string_copias('a', 4)


#24. Write a Python program to test
#whether a passed letter is a vowel or not.

def is_vowel(vowel):    
    #testando se vowel é uma vogal
    teste = vowel in 'aeiouAEIOU'
    return teste

def is_vowel2(vowel):    
    vogais = 'aeiouAEIOU'
    #percorrendo a lista de vogais
    for i in vogais:
        #testando se a i-ésima vogal é igual
        if vowel == i:
            return True
    return False


#testando a função
is_vowel('a')
is_vowel('A')
is_vowel('b')
is_vowel('U')
is_vowel2('a')
is_vowel2('A')
is_vowel2('b')
is_vowel2('U')

#25. Write a Python program to check whether a
#specified value is contained in a group of values.

def is_in_lista(lista, val):
    #testando se o valor está na lista
    teste = val in lista
    #retornando o teste
    return teste


#testando função
is_in_lista([1, 2, 3, 5], 5)
is_in_lista([1, 2, 3, 5], 6)



#26. Write a Python program to create a histogram
#from a given list of integers.

import matplotlib.pyplot as plt
#fazendo um histograma
plt.hist([1,2,2,3,3,3])

#definindo função
def histograma(char, lista):
    #pegando os elementos unicos da lista e ordenando
    unicos = sorted(list(set(lista)))
    #percorrendo os elementos unicos 
    for i in range(len(unicos)):
        #contando quantas vezes cada elemento da lista aparece
        quantidade = lista.count(unicos[i])
        #printando o elemento da lista unicos e o char multiplicado
        #pela quantidade de vzs que o esse elemento
        #do unicos aparece na lista
        print(unicos[i], char*quantidade)

#testando a função
histograma('#', [1,2,2,3,3,3, 2.1, 2.1, 2.1, 2.1, 2.1])
histograma('JK', [1,2,2,3,3,3, 2.1, 21, 2.1, 2.1, 65, 22, -1])

#Solução do exercicio (TA COMPLETAMENTE DIFERENTE
#DO MEU MAS EU CREIO QUE EU SOU O CERTO DA HISTORIA)
def histogram( items ):
    #percorrendo a lista de intens
    for n in items:
        #criando output
        output = ''
        #definindo o times como o n-ésimo item da lista times
        times = n
        #criando um loop enquanto o times é positivo
        while( times > 0 ):
          #adicionando '*' ao output
          output += '*'
          #decrementando a variável times
          times = times - 1
        #printando o output
        print(output)

histogram([2, 3, 6, 5])
histogram([2, 3, 6, 5, 19])


#27. Write a Python program to concatenate all elements
#in a list into a string and return it.


def concatena(lista):
    #definindo string vazia
    string = ''
    #percorrendo lista
    for c in lista:
        #incrementando string com o elemento c da 
        #lista convertido para uma string
        string += str(c)
    #retornando string
    return string

#testando função
concatena([1,2,3,'a','b','c'])
concatena([1,2,'asdads', {11:'a'}])

#não deu pra fazer usando essa função pq ela só serve para listas de strs
'#'.join(['1','2','3'])



#28. Write a Python program to print all even numbers
#from a given numbers list in the same order and
#stop the printing if any numbers that come
#after 237 in the sequence.

def evens(lista):
    #pecorrendo a lista
    for c in lista:
        #vendo se o o elemento c da lista é 237
        if c == 237:
            #pritando o c
            print(c)
            #saindo do loop
            break
        #vendo se o elemento é par
        if c%2==0:
            #pritando caso seja
            print(c)        

#testando função
evens([1,2,3,4,5,6,7,8,9])
evens([1,2,3,4,5,33,228,334,237,2,6,7])

evens([386, 462, 47, 418, 907, 344, 236, 375, 823,
       566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826,
    248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767,
    553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527])



#29. Write a Python program to print out a set containing all the
#colors from color_list_1 which are not present in color_list_2.


#definindo função
def cores_lista(l1, l2):
    #definindo lista_final
    lista_final = []
    #percorrendo a l1
    for c in l1:
        #checando se c não está em l2 e nem na lista final
        if (not c in l2) and (not c in lista_final):
            #adicionando c a lista_final caso seja verdade
            lista_final.append(c)
    #retornando a lista final
    return lista_final

#testando função
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

cores_lista(color_list_1, color_list_2)

not 3 > 5



#30. Write a Python program that will accept the base and height
#of a triangle and compute the area. Go to the editor

#definindo função
def area_tri(base, altura):
    #retornando área do triângulo
    return base*altura/2

#testando função
area_tri(3, 5)
area_tri(3, 2)














































































































