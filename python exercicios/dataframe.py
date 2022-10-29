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
df
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


#26. Write a Pandas program to add one row in an existing DataFrame.

#definindo dicionario
d = {'col1': [1, 4, 3, 4, 5],
     'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

#definindo dataframe
df = pd.DataFrame(data=d)
df
#adicionando linha a mais (não da pra usar o iloc)
df.loc[5] = [10, 11, 12]
df
#definindo outro dicionario
d2 = {'col1': 11, 'col2': 12, 'col3': 13}
#adicionando o dicionario d2
df = df.append(d2, ignore_index=True)
df
#definindo dicionario de listas
d3 = {'col1': [12, 13] , 'col2': [12, 13], 'col3': [12, 13]}
#adicionando as listas ao dataframe
df.append(d3, ignore_index=True)



#27. Write a Pandas program to write a DataFrame to
#CSV file using tab separator.

df
#exportando dataframe com separador \t
df.to_csv('C:\\Users\\luisg\\OneDrive\\Documentos\\GitHub\\python\\python exercicios\\ex27.csv',
          sep='\t', index=False)
#importando dataframe
df = pd.read_csv('C:\\Users\\luisg\\OneDrive\\Documentos\\GitHub\\python\\python exercicios\\ex27.csv')
df


#28. Write a Pandas program to count city wise number of people
#from a given of data set (city, name of the person).

#definindo dataframe
df1 = pd.DataFrame(
    {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
              'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 
         'California', 'California', 'Los Angeles', 'Los Angeles',
         'Georgia', 'Georgia', 'Los Angeles']})
df1
#agrupando os elementos por cidades
cidades = df1.groupby('city')
#contando os agrupamentos
cidades.count()
#resolução do site
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
g1



#29. Write a Pandas program to delete DataFrame row(s)
#based on given column value.

#definindo dataframe
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8],
     'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
df
#apagando linha 3 e 4
df.drop([3,4], axis=0, inplace=True)
df

#definindo dataframe
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8],
     'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
#reatribuindo o dataframe mas só com as linhas 1 e 2
#(na prática o mesmo de antes)
df = df.iloc[[1,2], :]
df
#ATÉ AQUI TAVA FAZENDO ERRADO MAS VOU DEIXAR SÓ PRA PODER VER DPS

#definindo dataframe
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8],
     'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

#pegando os elementos onde o valor da coluna 2 e diferente de 5
#mas de varios jeitos diferentes
df[df['col2'] !=5]
df[df.col2 !=5]
df[df.loc[:, 'col2'] !=5]
df[df.iloc[:, 2] !=5]



#30. Write a Pandas program to widen output
#display to see more columns.

#definindo dataframe
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8],
     'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

#não faço idéia doque isso faz
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print("Original DataFrame")
print(df)





#31. Write a Pandas program to select a row of
#series/dataframe by given integer index.



#definindo o df
d = {'col1': [1, 4, 3, 4, 5],
     'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

#escolhendo a linha
row = int(input('Digite a linha do df: '))
#mostrando a linha
df.iloc[[row]] #desse jeito mostra na horizontal
df.iloc[row]


#32. Write a Pandas program to replace all the NaN values with
#Zero's in a column of a dataframe.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes',
                    'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

#substituindo os Nan por 0
df.fillna(0, inplace=True)
df


#33. Write a Pandas program to convert
#index in a column of the given dataframe.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
                    'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

#Transpondo o dataframe
#(não era isso que era pra fazer mas foi oque eu interpretei)

#df = pd.DataFrame(data=df.values.reshape(df.shape[1], df.shape[0]),
#                  index=df.columns, columns=df.index)
df

#colocando o index como uma coluna extra
df.reset_index(level=0, inplace=True)
df
print(df.to_string(index=False))



#34. Write a Pandas program to set a given value for particular
#cell in  DataFrame using index value.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

#mudando valor da linha 8 e ultima coluna
df.iloc[8, -1] = 10.2

#essa função não funciona mais mas fazia o mesmo que a linha acima
df.set_value(8, 'score', 10.2)

#versão nova da função acima (funciona como um iloc)
df.at[8, 'score'] 
df.at[8, 'score'] = 10.2
df




#35. Write a Pandas program to count the NaN values in
#one or more columns in DataFrame.


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no',
                    'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
#calculando o total de valores NaN

#em cada coluna
df.isna().sum()
#no df todo
df.isna().sum().sum()
#resposta do Exercicio
print(df.isnull().values.sum())


#36. Write a Pandas program to drop a list
#of rows from a specified DataFrame.


d = {'col1': [1, 4, 3, 4, 5],
     'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
df
df.drop(labels=[2,4], axis=0, inplace=True)
df
#resposta do exercicio
df = df.drop(df.index[[2,4]])


#37. Write a Pandas program to reset index in a given DataFrame.

#definindo dataframe
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no',
                    'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)
df
#apagando linhas
df.drop(labels=[0,1], axis=0, inplace=True)
df
#resetando linhas
df.reset_index(inplace=True)
df



#38. Write a Pandas program to divide a DataFrame in a given ratio.

#definindo df
df = pd.DataFrame(np.random.randn(10,2))
df

#pegando uma amostra de 70% do dataframe
part_70 = df.sample(frac=0.7, random_state=10)
part_70

#pegando as partes do datafrane que não pertencem a amostra de 70%
part_30 = df.drop(labels=part_70.index, axis=0)
part_30



#39. Write a Pandas program to combining two series into a DataFrame.

#definindo series
serie1 = pd.Series(['100', '200', 'python', '300.12', '400'])
serie1
serie2 = pd.Series(['10', '20', 'php', '30.12', '40'])
serie2

#criando dataframe como junção das series como colunas
df = pd.DataFrame(pd.concat([serie1, serie2], axis=1))
df


#40. Write a Pandas program to shuffle a given DataFrame rows.

#definindo df
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
                      'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes',
                    'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

#pegando amostra igual ao tamanho do df (em ordem aleatória)
df.sample(len(df))
#resposta do exercicio
df.sample(frac=1)



#41. Write a Pandas program to convert DataFrame column
#type from string to datetime.

#definindo serie
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])

#definindo df
df = pd.to_datetime(s)
df


#42. Write a Pandas program to rename a specific
#column name in a given DataFrame.

#definindo dataframe
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data=d)
df
#mudando o nome das colunas
df.rename(columns={'col2':'COL2'}, inplace=True)
df


#43. Write a Pandas program to get a list of a
#specified column of a DataFrame.

d = {'col1': [1, 2, 3], 'COL2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data=d)

#pegando colunas especificas
#NÃO ERA ISSO QUE ERA PRA FAZER MAS VOU DEIXAR AQUI
df[['COL2', 'col1']]
df.loc[:, ['COL2', 'col1']]
df.iloc[:, [1,0]]

#pegando a coluna 3 convertida pra lista
df['col3'].tolist()


#44. Write a Pandas program to create a DataFrame from a Numpy array
#and specify the index column and column headers.










