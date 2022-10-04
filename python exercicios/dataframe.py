#questões
#https://www.w3resource.com/python-exercises/pandas/index.php

import numpy as np
import pandas as pd

#1. Write a Pandas program to get the powers of
#an array values element-wise.


#definindo datagrame
dicio = {'X':[78,85,96,80,86],
         'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}


df = pd.DataFrame(dicio)
df

#elevando cada elemento do dataframe ao quadrado
df**2

#2. Write a Pandas program to create and display a DataFrame from a
#specified dictionary data which has the index labels

#definindo dataframe
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

#mostrando valores do dataframe
df
#mostrando estatísticas das colunas quantitativas do dataframe
df.describe()
#pegando informações sobre os dados do dataframe
df.info()


#4. Write a Pandas program to get the
#first 3 rows of a given DataFrame.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no',
            'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

#pegano as 3 primeiras linhas do dataframe
df.iloc[:3, :]


#5. Write a Pandas program to select the 'name' and
#'score' columns from the following DataFrame.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine',
                      'James', 'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no',
            'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)


#definindo colunas a serem selecionadas pelo dataframe
colunas = ['name', 'score']
#mostrando colunas selecionadas 
df[colunas]


#6. Write a Pandas program to select the specified columns and
#rows from a given data frame.


#definindo dataframe
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


#pegando no df as colunas score e qualify e as linhas b, d, f e g
df[['score', 'qualify']].loc[['b','d','f','g']]
#fazendo o mesmo acima mas usando só a função iloc
df.iloc[[1,4,6,8],[1,3]]


#7. Write a Pandas program to select the rows where the number
#of attempts in the examination is greater than 2.

#definindo dataframe
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

#definindo condições

#valores da coluna attempts que são maiores que 2
condicao1 = df['attempts']>2
#pegando os valores do dataframe em que a condição são cumpridas
df[condicao1]


#8. Write a Pandas program to count the number
#of rows and columns of a DataFrame.

#pegando a quantidade de linhas de um dataframe
df.shape[0]
len(df)
len(df.axes[0])
#pegando a quantidade de colunas de um dataframe
df.shape[1]
len(df.axes[1])

#tupla com array de index e colunas
df.axes


#9. Write a Pandas program to select the rows where the
#score is missing, i.e. is NaN.

#definindo condição

#valores da coluna score que são nulos
condicao1 = df['score'].isnull()
#pga os valores do dataframe que atendem a condição 1
df[condicao1]

#10. Write a Pandas program to select the rows the
#score is between 15 and 20 (inclusive)

#definindo condições

#valores da coluna score que são maior igual a 15
condicao1 = df['score']>=15
#valores da coluna score que são menor igual a 20
condicao2 = df['score']<=20
#pegando valores do dataframe que atendam as condições 1 e 2
df[(condicao1) & (condicao2)]
#fazendo o mesmo acima mas como uma função só
df[df['score'].between(15, 20)]



#11. Write a Pandas program to select the rows where number
#of attempts in the examination is
#less than 2 and score greater than 15.

#definindo dataframe
exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James',
            'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df

#definindo as condições

#valores da coluna attempts que são menores que 2
condicao1 = df['attempts'] < 2
#valores da coluna score que são maiores que 15
condicao2 = df['score'] > 15
#pegando os elementos do dataframe que atendam as condições 1 e 2
df[(condicao1) & (condicao2)]

#12. Write a Pandas program to change the score in row 'd' to 11.5.
#definindo dataframe
exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James',
            'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
df

#mudando o valor da linha d da coluna score
df['score'].loc['d'] = 11.5
df


#13. Write a Pandas program to calculate the sum of
#the examination attempts by the students.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew',
                      'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no',
            'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df
#calculando a soma da coluna attempts
df['attempts'].sum()




#14. Write a Pandas program to calculate the mean score for
#each different student in DataFrame.

#calculando a média da coluna score
df['score'].mean()


#15. Write a Pandas program to append a new row 'k' to data
#frame with given valuesfor each column. Now delete the new row
#and return the original DataFrame.


#adicionando a linha k 
#obs: array faz com que todos os dados da linha k tenham msm tipo
df.loc['k'] = np.array(['zézinho', 44.2, 0, 'no'])
df
#removendo linha k
df.drop('k',axis=0, inplace=True)
df


#16. Write a Pandas program to sort the DataFrame first by 'name'
#in descending order, then by 'score' in ascending order.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=exam_data, index=labels)
df

#adicionando elemento na linha k para comparação
df.loc['k'] = ['Dima', 443, 2, 'no']

#vendo o tipo dos dados na coluna score
#obs: fiz isso pq antes tava definindo a linha k como array e 
#isso deixa todos os elementos da linha k como strings
df['score'].apply(type)

#ordenando pela coluna name em ordem descendente
df.sort_values(by='name', ascending=False)
#ordenando pela coluna score em ordem ascendente
df.sort_values(by= 'score', ascending=True)
#ordenando primeiro pela coluna name em ordem descendente
#e depois pela coluna score em ordem ascendente
df.sort_values(by=['name', 'score'], ascending=[False, True])


#17. Write a Pandas program to replace the 'qualify' column contains
#the values 'yes' and 'no' with True and False.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=exam_data, index=labels)

#criando coluna onde se na coluna qualify tem o valor yes, o valor
#nessa coluna é True e False caso contrário
coluna_nova = df['qualify'] == 'yes'
#reatribuindo a coluna qualify como a nova_colna
df['qualify'] =  coluna_nova
df
#subistibuindo o valor True por 'yes' e o False por 'no'
#obs: esse método é melhor para casos em que existam mais de 2 vals 
df['qualify'] = df['qualify'].map({True: 'yes', False: 'no'})
df



#18. Write a Pandas program to change the name 'James' to
#'Suresh' in name column of the DataFrame.

#substituindo o valor da coluna name e linha d por 'suresh'
df['name'].loc['d'] = 'Suresh'
df

#19. Write a Pandas program to delete the 
#'attempts' column from the DataFrame.


#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=exam_data, index=labels)
df

#apagando coluna 'attempts'
df.drop('attempts', axis=1, inplace=True)
df
#apagando coluna 'name'
df.pop('name')
df

#20. Write a Pandas program to insert
#a new column in existing DataFrame.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura',
                      'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
            'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=exam_data, index=labels)
df

#adicionando coluna "nova" só com valores nulos
df['nova'] = np.nan
df



#21. Write a Pandas program to iterate over rows in a DataFrame.

exam_data = [{'name':'Anastasia', 'score':12.5},
             {'name':'Dima','score':9},
             {'name':'Katherine','score':16.5}]

df = pd.DataFrame(exam_data)
df

#percorrendo as linhas do dataframe
for i in range(df.shape[1]):
    print(df.iloc[i, :])

for index, row in df.iterrows(): #resposta do site
    print(row['name'], row['score'], index)

for index, row in df.iteritems():
    print(row,  index)



#22. Write a Pandas program to get list from DataFrame column headers.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James',
                      'Emily', 'Michael',
                      'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no',
            'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
df
#mostrando as colunas do dataframe
df.columns
df.axes[1]


#23. Write a Pandas program to rename columns of a given DataFrame.

#renomeando algumas linhas e colunas do dataframe
df.rename(index = {'a':'aa', 'd':'ddd', 'b':'b2'},
          columns={'name': 'NAME', 'score': 'SCORE'}, inplace=True)
df


#24. Write a Pandas program to select rows from a given DataFrame
#based on values in some columns.

#condição:
#valores da coluna attempts que são iguais a 3
cond = df['attempts'] == 3
#pegando valores do dataframes que atendem a condição 1
df[cond]


#25. Write a Pandas program to change the
#order of a DataFrame columns.

#reatribuindo o dataframe com a ordem das colunas trocadas
df = df.iloc[:, [1,0,2,3]]
df





































































































































































































