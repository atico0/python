# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:35:22 2022

@author: luisg
"""


import numpy as np

#xercise 1
#The following array is given:

result = np.array(
    [['ALIOR', 'PLALIOR00045', '88 860 000', '1 386 216 000',
                    '0,891', '2,16', '14'],
       ['CCC', 'PLCCC0000016', '27 918 000', '1 292 603 400', '0,831',
        '5,28', '42'],
       ['CDPROJEKT', 'PLOPTTC00011', '67 348 000', '22 864 646 000', '14,702',
        '7,39', '7'],
       ['CYFRPLSAT', 'PLCFRPT00013', '275 301 000', '6 854 994 900', '4,408',
        '1,17', '14'],
       ['DINOPL', 'PLDINPL00011', '47 937 000', '8 916 282 000', '5,733',
        '9,13', '12'],
       ['JSW', 'PLJSW0000015', '52 636 000', '716 902 320', '0,461',
        '1,51', '24'],
       ['KGHM', 'PLKGHM000017', '136 410 000', '9 881 540 400', '6,354',
        '4,78', '8'],
       ['LOTOS', 'PLLOTOS00025', '86 543 000', '5 609 717 260', '3,607',
        '2,91', '16'],
       ['LPP', 'PLLPP0000011', '1 306 000', '7 444 200 000', '4,787',
        '1,43', '19'],
       ['MBANK', 'PLBRE0000012', '12 997 000', '2 830 746 600', '1,820',
        '0,42', '24'],
       ['ORANGEPL', 'PLTLKPL00017', '647 357 000', '4 285 503 340', '2,756',
        '1,16', '13'],
       ['PEKAO', 'PLPEKAO00016', '176 379 000', '9 619 710 660', '6,185',
        '5,27', '9'],
       ['PGE', 'PLPGER000010', '796 776 000', '3 561 588 720', '2,290',
        '2,88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1 624 608 000', '6 072 784 704', '3,905',
        '1,56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289 049 000', '17 701 360 760',
        '11,382', '12,44', '8'],
       ['PKOBP', 'PLPKO0000016', '857 593 000', '18 807 014 490', '12,093',
        '10,49', '9'],
       ['PLAY', 'LU1642887738', '114 151 000', '3 696 209 380', '2,377',
        '1,47', '16'],
       ['PZU', 'PLPZU0000011', '568 305 000', '17 515 160 100', '11,262',
        '6,64', '6'],
       ['SANPL', 'PLBZ00000044', '33 207 000', '5 213 499 000', '3,352',
        '1,91', '18'],
       ['TAURONPE', 'PLTAURN00011', '1 043 590 000', '1 252 308 000',
        '0,805', '1,21', '33']], dtype='<U14')

#Remove all spaces in the text and replace all commas with periods.
#In response, print this array to the console.



result

print(np.char.replace(np.char.replace(result, ' ', ''), ',', '.'))



#Exercise 2
#The following array is given:

result = np.array([['ALIOR', 'PLALIOR00045', '88860000', '1386216000',
                    '0.891', '2.16', '14'],
       ['CCC', 'PLCCC0000016', '27918000', '1292603400',
        '0.831', '5.28', '42'],
       ['CDPROJEKT', 'PLOPTTC00011', '67348000', '22864646000',
        '14.702', '7.39', '7'],
       ['CYFRPLSAT', 'PLCFRPT00013', '275301000', '6854994900',
        '4.408', '1.17', '14'],
       ['DINOPL', 'PLDINPL00011', '47937000', '8916282000',
        '5.733', '9.13', '12'],
       ['JSW', 'PLJSW0000015', '52636000', '716902320', '0.461', '1.51', '24'],
       ['KGHM', 'PLKGHM000017', '136410000', '9881540400', '6.354', '4.78', '8'],
       ['LOTOS', 'PLLOTOS00025', '86543000', '5609717260', '3.607', '2.91', '16'],
       ['LPP', 'PLLPP0000011', '1306000', '7444200000', '4.787', '1.43', '19'],
       ['MBANK', 'PLBRE0000012', '12997000', '2830746600', '1.820', '0.42', '24'],
       ['ORANGEPL', 'PLTLKPL00017', '647357000', '4285503340', '2.756', '1.16', '13'],
       ['PEKAO', 'PLPEKAO00016', '176379000', '9619710660', '6.185', '5.27', '9'],
       ['PGE', 'PLPGER000010', '796776000', '3561588720', '2.290', '2.88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1624608000', '6072784704', '3.905', '1.56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289049000', '17701360760', '11.382', '12.44', '8'],
       ['PKOBP', 'PLPKO0000016', '857593000', '18807014490', '12.093', '10.49', '9'],
       ['PLAY', 'LU1642887738', '114151000', '3696209380', '2.377', '1.47', '16'],
       ['PZU', 'PLPZU0000011', '568305000', '17515160100', '11.262', '6.64', '6'],
       ['SANPL', 'PLBZ00000044', '33207000', '5213499000', '3.352', '1.91', '18'],
       ['TAURONPE', 'PLTAURN00011', '1043590000', '1252308000', '0.805', '1.21', '33']], dtype='<U12')

#Extract all rows with the company name starting with the letter 'P'
#and assign to the stocks_startswith_P variable. In response,
#print stocks_startswith_P variable to the console.



?np.char.startswith

primeira_linha_comeca_p = np.char.startswith(result[:,0], 'P', start=0)
stocks_startswith_P = result[primeira_linha_comeca_p, :]
print(stocks_startswith_P)



#Exercise 3
#The following array is given:

stocks_startswith_P = np.array([['PEKAO', 'PLPEKAO00016', '176379000', '9619710660', '6.185', '5.27', '9'],
       ['PGE', 'PLPGER000010', '796776000', '3561588720', '2.290', '2.88', '18'],
       ['PGNIG', 'PLPGNIG00014', '1624608000', '6072784704', '3.905', '1.56', '12'],
       ['PKNORLEN', 'PLPKN0000018', '289049000', '17701360760', '11.382', '12.44', '8'],
       ['PKOBP', 'PLPKO0000016', '857593000', '18807014490', '12.093', '10.49', '9'],
       ['PLAY', 'LU1642887738', '114151000', '3696209380', '2.377', '1.47', '16'],
       ['PZU', 'PLPZU0000011', '568305000', '17515160100', '11.262', '6.64', '6']], dtype='<U12')


#Calculate the total share of companies whose name starts with the
#letter 'P'. Round the result to two decimal places and
#print it to the console.

result = round(sum(np.float32((stocks_startswith_P[np.char.startswith(stocks_startswith_P[:,0],
                                       'P', start=0), -3]))), 2)
print(result)

#RESPOSTA DO EXERCICIO
print(np.round(stocks_startswith_P[:, 4].astype(float).sum(), 2))

























