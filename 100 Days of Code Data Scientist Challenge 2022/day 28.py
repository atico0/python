# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 11:25:09 2022

@author: luisg
"""


import numpy as np


#Exercise 1
#The following string is given (WIG.GAMES index data):

wig_games_raw = """Profile    Time    Course    Change    Change%    Ref.    Open    Low    High    Volume    Turn    Share
11B (11BIT)    17 kwi 17:01    391.00    +8.00    (+2.09%)    383.00    383.50    383.00    394.00    12 784    4 994 874    19.034%
CDR (CDPROJEKT)    17 kwi 17:01    339.50    +5.30    (+1.59%)    334.20    338.30    337.00    344.20    233 059    79 245 368    39.618%
CIG (CIGAMES)    17 kwi 17:03    0.742    -0.012    (-1.59%)    0.754    0.772    0.730    0.772    1 311 078    971 459    1.855%
PLW (PLAYWAY)    17 kwi 17:03    387.50    +18.00    (+4.87%)    369.50    374.00    373.00    388.00    33 206    12 661 786    10.638%
TEN (TSGAMES)    17 kwi 17:02    349.50    +22.50    (+6.88%)    327.00    332.00    330.00    353.50    39 793    13 697 060    28.855%"""

#Create an array from this string as shown below and assign to the wig_games
#variable. In response, print this array to the console.


#solução do exercicio
lines = wig_games_raw.splitlines()
lines = [line.split('\t') for line in lines]
wig_games = np.array(lines)
wig_games = np.char.replace(wig_games, ' ', '')
print(wig_games)





#Exercise 2
#The following array is given:

wig_games = np.array(
    [
        [
            'Profile',
            'Time',
            'Course',
            'Change',
            'Change%',
            'Ref.',
            'Open',
            'Low',
            'High',
            'Volume',
            'Turn',
            'Share',
        ],
        [
            '11B(11BIT)',
            '17kwi17:01',
            '391.00',
            '+8.00',
            '(+2.09%)',
            '383.00',
            '383.50',
            '383.00',
            '394.00',
            '12784',
            '4994874',
            '19.034%',
        ],
        [
            'CDR(CDPROJEKT)',
            '17kwi17:01',
            '339.50',
            '+5.30',
            '(+1.59%)',
            '334.20',
            '338.30',
            '337.00',
            '344.20',
            '233059',
            '79245368',
            '39.618%',
        ],
        [
            'CIG(CIGAMES)',
            '17kwi17:03',
            '0.742',
            '-0.012',
            '(-1.59%)',
            '0.754',
            '0.772',
            '0.730',
            '0.772',
            '1311078',
            '971459',
            '1.855%',
        ],
        [
            'PLW(PLAYWAY)',
            '17kwi17:03',
            '387.50',
            '+18.00',
            '(+4.87%)',
            '369.50',
            '374.00',
            '373.00',
            '388.00',
            '33206',
            '12661786',
            '10.638%',
        ],
        [
            'TEN(TSGAMES)',
            '17kwi17:02',
            '349.50',
            '+22.50',
            '(+6.88%)',
            '327.00',
            '332.00',
            '330.00',
            '353.50',
            '39793',
            '13697060',
            '28.855%',
        ],
    ],
    dtype='<U14',
)

#Remove the following columns:

'Change'

'Change%'

'Ref.'

'Volume'

#In response, print transformed array to the console.

?np.delete

print(np.delete(wig_games, [3,4,5,9], axis=1))




#Exercise 3
#The following array is given:

wig_games = np.array(
    [
        [
            'Profile',
            'Time',
            'Course',
            'Open',
            'Low',
            'High',
            'Turn',
            'Share',
        ],
        [
            '11B(11BIT)',
            '17kwi17:01',
            '391.00',
            '383.50',
            '383.00',
            '394.00',
            '4994874',
            '19.034%',
        ],
        [
            'CDR(CDPROJEKT)',
            '17kwi17:01',
            '339.50',
            '338.30',
            '337.00',
            '344.20',
            '79245368',
            '39.618%',
        ],
        [
            'CIG(CIGAMES)',
            '17kwi17:03',
            '0.742',
            '0.772',
            '0.730',
            '0.772',
            '971459',
            '1.855%',
        ],
        [
            'PLW(PLAYWAY)',
            '17kwi17:03',
            '387.50',
            '374.00',
            '373.00',
            '388.00',
            '12661786',
            '10.638%',
        ],
        [
            'TEN(TSGAMES)',
            '17kwi17:02',
            '349.50',
            '332.00',
            '330.00',
            '353.50',
            '13697060',
            '28.855%',
        ],
    ],
    dtype='<U14',
)

#Save this array to the 'wig_games.csv' file. Then load the content of this
#file into the wig_games_new variable and print it to the console.

?np.savetxt

#solução do exercicio
np.savetxt(fname='wig_games.csv', X=wig_games, fmt='%s', delimiter=',')
wig_games_new = np.loadtxt(
    fname='wig_games.csv', delimiter=',', dtype=str
)
print(wig_games_new)



















