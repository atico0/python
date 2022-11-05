# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 18:09:42 2022

@author: luisg
"""

#LISTAS




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





#Exercise 11
#The following list is given:

techs = ['python', 'django', 'sql', 'html', 'c++', 'git', 'css']

#Using the del statement remove all items from the
#techs list except the first and last.
#In response, print the techs list to the console.


del(techs[1:-1])
print(techs)


#Exercise 12
#The following list is given:

record = ['01302', 'esmartdata', ['python', 'sql', 'git', 'css'], 30000]

#Iterate through the record list. If the object in the list
#is an instance of the list class, remove all of its items. In response,
#print the contents of the record list to the console.

for i in range(len(record)):
    if type(record[i]) == type(list()):
        record[i] = []
        #item.clear() Solução do exercicio

print(record)


#Exercise 13
#The following list is given:

cities = [
    'Istanbul',
    'Moscow',
    'London',
    'Saint Petersburg',
    'Berlin',
    'Madrid',
]

#Find the index for 'Berlin' city using the appropriate method. Then,
#using this index remove all elements to the end of the list,
#including the city named 'Berlin'.

#In response, print the cities list to the console.

index = cities.index('Berlin')
del(cities[index:])
print(cities)




#Exercise 14
#The following list is given:

countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

#Use the appropriate method to find the number of occurrences of the
#word 'Russia' and print it on the console.

print(countries.count('Russia'))




#Exercise 15
#The following lists are given:

countries_top_10 = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]
 
countries_next_5 = [
    'Austria',
    'Germany',
    'Romania',
    'Poland',
    'Hungary'
]

#Using the list.copy() method, make a shallow copy of the
#countries_top_10 list and assign it to the countries variable.
#Then, using the appropriate method, extend the
#countries list with the elements from the countries_next_5 list.

#In response, print the countries list to the console.

countries = countries_top_10.copy()
countries.extend(countries_next_5)
print(countries)




#Exercise 16
#The following list is given:

countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

#Using the appropriate method, make a shallow copy of the
#countries list and assign it to the countries_copy variable.
#Then, using the appropriate method, reverse the order of elements in the
#countries_copy list. In response, print the index for the country
#named 'Italy' (countries_copy list) to the console.


countries_copy = countries.copy()
countries_copy.reverse()
print(countries_copy.index('Italy'))



#Exercise 17
#The following list is given:

countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]


#Using the appropriate method, sort the elements of the countries
#list in ascending order.

#In response, print the first three items of the list to the console.


countries.sort()
print(countries[:3])









#Exercise 18
#The following list is given:

countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]

#Convert this list to the form below:

#['SPA', 'ITA', 'FRA', 'UNI', 'BEL', 'TUR', 'GER', 'UKR', 'RUS', 'RUS']

#and assign to codes variable. (first three capital letters of
#the country name).

#Then sort in ascending order according to the last letter of the country
#code. In response, print this sorted list to the console.

codes = []
for c in countries:
    codes.append(c[:3].upper())
codes.sort(key=lambda x:x[-1])
print(codes)


#Exercise 19
#The following list is given:

population = [
    ('Istanbul', 'Turkey', 15462452),
    ('Moscow', 'Russia', 12195221),
    ('London', 'United Kingdom', 9126366),
    ('Saint Petersburg', 'Russia', 5383890),
    ('Berlin', 'Germany', 3748148),
    ('Madrid', 'Spain', 3223334),
    ('Kyiv', 'Ukraine', 2950800),
    ('Rome', 'Italy', 2844750),
    ('Paris', 'France', 2140526),
    ('Minsk', 'Belarus', 1982444),
]

#Each item is a tuple that contains three pieces of information:
#city, country, and population.

#Sort the population list alphabetically by country name.
#Then, using a for loop, print each item to the console as shown below.


population.sort(key=lambda x:x[1])
for c in population:
    print(c)





#Exercise 20
#The following list is given:

population = [
    ('Istanbul', 'Turkey', 15462452),
    ('Moscow', 'Russia', 12195221),
    ('London', 'United Kingdom', 9126366),
    ('Saint Petersburg', 'Russia', 5383890),
    ('Berlin', 'Germany', 3748148),
    ('Madrid', 'Spain', 3223334),
    ('Kyiv', 'Ukraine', 2950800),
    ('Rome', 'Italy', 2844750),
    ('Paris', 'France', 2140526),
    ('Minsk', 'Belarus', 1982444),
]

#Each item is a tuple that contains three pieces of information:
#city, country, and population.

#Using filter(), select all rows for the country named 'Russia'
#and assign it to the russia variable. In response,
#print this variable to the console.


russia = []
for c in filter(lambda x:x[1]=='Russia', population):
    russia.append(c)

print(russia)


















































