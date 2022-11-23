# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:07:37 2022

@author: luisg
"""




import numpy as np

#Exercise 1
#The following array is given:

A = np.array([['#summer#time#mood'],
              ['#sport#time']])

#Replace all # characters with spaces and then strip all unnecessary white
#characters around the text as shown below. In response,
#print this array to the console.

#Tip: Use np.char.replace() and np.char.strip() function.

?np.char.replace
?np.char.strip

print(np.char.strip(np.char.replace(A, '#', ' ')))




#Exercise 2
#The following array is given:

A = np.array(
    [
        ['#summer#time#mood', '#vibe'],
        ['#sport#time', '#good#time'],
        ['#event#summer', '#fast#move'],
        ])

#Count the number of occurrences of the word 'time'
#in each element of this array.

#Tip: Use the np.char.count() function.

?np.char.count
print(np.char.count(A, 'time'))





#Exercise 3
#The following text is given:

text = """ALIOR    PLALIOR00045    88 860 000    1 386 216 000    0,891    2,16    14
CCC    PLCCC0000016    27 918 000    1 292 603 400    0,831    5,28    42
CDPROJEKT    PLOPTTC00011    67 348 000    22 864 646 000    14,702    7,39    7
CYFRPLSAT    PLCFRPT00013    275 301 000    6 854 994 900    4,408    1,17    14
DINOPL    PLDINPL00011    47 937 000    8 916 282 000    5,733    9,13    12
JSW    PLJSW0000015    52 636 000    716 902 320    0,461    1,51    24
KGHM    PLKGHM000017    136 410 000    9 881 540 400    6,354    4,78    8
LOTOS    PLLOTOS00025    86 543 000    5 609 717 260    3,607    2,91    16
LPP    PLLPP0000011    1 306 000    7 444 200 000    4,787    1,43    19
MBANK    PLBRE0000012    12 997 000    2 830 746 600    1,820    0,42    24
ORANGEPL    PLTLKPL00017    647 357 000    4 285 503 340    2,756    1,16    13
PEKAO    PLPEKAO00016    176 379 000    9 619 710 660    6,185    5,27    9
PGE    PLPGER000010    796 776 000    3 561 588 720    2,290    2,88    18
PGNIG    PLPGNIG00014    1 624 608 000    6 072 784 704    3,905    1,56    12
PKNORLEN    PLPKN0000018    289 049 000    17 701 360 760    11,382    12,44    8
PKOBP    PLPKO0000016    857 593 000    18 807 014 490    12,093    10,49    9
PLAY    LU1642887738    114 151 000    3 696 209 380    2,377    1,47    16
PZU    PLPZU0000011    568 305 000    17 515 160 100    11,262    6,64    6
SANPL    PLBZ00000044    33 207 000    5 213 499 000    3,352    1,91    18
TAURONPE    PLTAURN00011    1 043 590 000    1 252 308 000    0,805    1,21    33"""

#Columns mean:

#Instrument | ISIN code | Package | Package (PLN) | Share in portfolio (%) |
#Share in trading shares and PDAs per session (%) |
#Average spread per session

#Split text into lines. Then split each line by the tab character \t and
#create an array (without headers) containing the following data as shown
#below. Assign this array to the result variable and print it to the console.



lines = text.splitlines()
lines
lines = [line.split('\t') for line in lines]
result = np.array(lines, dtype=np.str)
print(result)

