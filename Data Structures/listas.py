# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:09:42 2022

@author: luisg
"""

#LSITAS




#Exercise 1
#Create a list containing the given elements:
#3, 10, 5, 28, 63 and assign to the result variable.
#In response, print the contents of this variable to the console.

result = [3, 10, 5, 28, 63]
print(result)



#Exercise 2
#In Python list can store different types of objects.
#Create a list containing the given elements:
#3, 'spark', True, 0.5, None, 63 and assign to result variable.
#In response, print this variable to the console.


result = [3, 'spark', True, 0.5, None, 63]
print(result)



#Exercise 3
#Create an empty list named result. Then, using the
#list.append() method, add the following elements to the list:
#34 1.5 True 'report.csv'
#In response, print this list to the console.


result = []
result.append(34)
result.append(1.5)
result.append(True)
result.append('report.csv')
print(result)



#Exercise 4
#Create an empty list named result. Then, using the list.insert() method,
#add the following elements to the list (insert each
#element at the beginning of the list):
#34 1.5 True 'report.csv'
#In response, print this list to the console.


result = []
result.insert(0, 34)
result.insert(0, 1.5)
result.insert(0, True)
result.insert(0, 'report.csv')
print(result)




#Exercise 5
#The following list is given:
#techs = ['python', 'django', 'sql', 'html', 'css']
#Perform the following operations:
#insert 'git' at position with index 1
#insert 'aws' at the end of the list
#In response, print this list to the console.



techs = ['python', 'django', 'sql', 'html', 'css']
techs.insert(1, 'git')
techs.insert(6, 'aws')#se colocar o indice -1 ele vai pra penultima pos
#techs.append('aws')
print(techs)












