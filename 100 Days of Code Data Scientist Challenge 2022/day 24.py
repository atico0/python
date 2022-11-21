

import numpy as np


#Exercise 1
#Using the np.arange() function, generate the following array:

    #'2021-01-01',
    #até
    #'2021-01-31'

#In response print this array to the console.


print(np.arange('2021-01-01', '2021-02-01', dtype='datetime64'))
#SOLUÇÃO DO EXERCICIO
print(np.arange('2021-01-01', '2021-02-01', dtype='datetime64[D]'))




#Exercise 2
#Using the np.arange() function, generate the following array:

#[['2021-01' '2021-02' '2021-03']
# ['2021-04' '2021-05' '2021-06']
# ['2021-07' '2021-08' '2021-09']
# ['2021-10' '2021-11' '2021-12']]

#In response, print this array to the console.

print(np.arange('2021-01', '2022-01', dtype='datetime64').reshape(4,-1))
#SOLUÇÃO DO EXERCICIO
A = np.arange('2021-01', '2022-01', dtype='datetime64[M]')
A = A.reshape(-1, 3)
print(A



#Exercise 3
#Using the np.datetime64() function,
#generate today's date and print result to the console.

?np.datetime64

print(np.datetime64('today'))



