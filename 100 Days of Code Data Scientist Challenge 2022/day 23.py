import numpy as np

#Exercise 1
#Calculate the roots of the following polynomials:
#Q(x) = 2x^3 + 4x^2 - 5x +1
#R(x) = 2x^3 - 5x +1
#In response print these roots to the console as shown below.
Q = [2,4,-5,1]
R = [2,0,-5,1]
print(help(np.roots))
print(np.roots(Q))
print(np.roots(R))

#Exercise 2
#The following polynomials are given:
#W(x) = 4x^2 + 5x + 1
#Q(x) = 2x^3 + 4x^2 - 5x + 1
#Perform the following operations and print results to the console as shown below:
#W + Q
#W - Q
#W * Q
#W + 2Q

W = np.array([4, 5, 1])
Q = np.array([2, 4, -5, 1])
print(help(np.polyadd))
print(help(np.polysub))
print(help(np.polymul))
print(help(np.polydiv))
print(np.polyadd(W, Q))
print(np.polysub(W, Q))
print(np.polymul(W, Q))
print(np.polyadd(W, 2*Q))



#Exercise 3
#The following array is given:

A = np.array([[-4, 3, 0, 1, -5],
              [6, -4, -2, 1, 3]])

#Use the sign function for this array.

#Reminder: The sign function works as follows: returns -1 for negative values,
#zero for zero, and 1 for positive values.
print(np.sign(A))
