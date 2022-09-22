#questões
#https://www.w3resource.com/python-exercises/pandas/index.php

import numpy as np
import pandas as pd

#1. Write a Pandas program to get the powers of
#an array values element-wise.

dicio = {'X':[78,85,96,80,86],
         'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}


df = pd.DataFrame(dicio)
df

df**2

#2. Write a Pandas program to create and display a DataFrame from a
#specified dictionary data which has the index labels

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily','Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
df


#3. Write a Pandas program to display a summary of the basic
#information about a specified DataFrame and its data.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes',
            'no', 'no','yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

df.describe()
df.info()


#4. Write a Pandas program to get the
#first 3 rows of a given DataFrame.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no',
            'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

df.iloc[:3, :]


#5. Write a Pandas program to select the 'name' and
#'score' columns from the following DataFrame.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no',
            'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df[['name', 'score']]


#6. Write a Pandas program to select the specified columns and
#rows from a given data frame.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no',
            'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df

df[['score', 'qualify']].loc[['b','d','f','g']]
df.iloc[[1,4,6,8],[1,3]]


#7. Write a Pandas program to select the rows where the number
#of attempts in the examination is greater than 2.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df

df[df['attempts']>2]


#8. Write a Pandas program to count the number
#of rows and columns of a DataFrame.

print(f'rows: {df.shape[0]}, {len(df)}, {len(df.axes[0])}')
print(f'columns: {df.shape[1]}, {len(df.axes[1])}')
df.axes


#9. Write a Pandas program to select the rows where the
#score is missing, i.e. is NaN.
df[df['score'].isnull()]

#10. Write a Pandas program to select the rows the
#score is between 15 and 20 (inclusive)
df[(df['score']>=15) & (df['score']<=20)]

df[df['score'].between(15, 20)]










