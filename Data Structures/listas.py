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


#Exercise 6

#The following list is given:
#techs = ['python', 'django', 'sql', 'html', 'css']

#Using the appropriate method pop
#the last element out and assign it to the result variable.

#In response, print the result and techs variables to
#the console as shown below.


techs = ['python', 'django', 'sql', 'html', 'css']
result = techs.pop()
print(result)
print(techs)


#Exercise 7
#The following list is given:

#techs = ['python', 'django', 'sql', 'html', 'css']

#Using the appropriate method pop the item with index 1
#out from the list and assign it to the result variable.

#In response, print the result and techs variables
#to the console as shown below.


techs = ['python', 'django', 'sql', 'html', 'css']
result = techs.pop(1)
print(result)
print(techs)










#Exercise 8
#The following list is given:

#user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']

#Using the appropriate method, delete the first encountered element '0101'.

#In response, print the techs variable to the console.

user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']
user_ids.pop(user_ids.index('0101'))
#user_ids.remove('0101') SOLUÇÃO DO EXERCICIO
print(user_ids)



#Exercise 9
#The following list is given:

#user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']

#and the user_id variable:

#user_id = '1040'

#When using the list.remove() method, attempting
#to remove a value that is not in the
#list results in a ValueError.

#Try to remove the user_id value from the user_ids list using the
#list.remove() method. If the value is not in the list, print
#the following message to the console: 
#"User with id '1040' is not in the list."


user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']

user_id = '1040'

try:
    user_ids.remove(user_id)
except:
    print("User with id '1040' is not in the list.")






#Exercise 10
#The following list is given:

#techs = ['python', 'django', 'sql', 'html', 'css']

#Use the del statement to remove penultimate item from the techs list.

#In response, print the techs list to the console.



techs = ['python', 'django', 'sql', 'html', 'css']
del(techs[-2])
print(techs)






















































