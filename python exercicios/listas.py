#Questões
#https://www.w3resource.com/python-exercises/string/



#1. Write a Python program to calculate the length of a string.
lista = '[1,2,3,4,5]' # definindo string
len(lista) #contando tamanho da string


#2. Write a Python program to count the number of characters
#(character frequency) in a string.
lista = '[1,2,3,4,5]' # definindo string
dicio = {}
for i in lista: #percorrendo a lista
    #para cada i da lista adiciona um elemento no dicio com a chave
    #igual a i e o elemento igual a contagem de i na lista
    dicio[i] = lista.count(i)
print(dicio)


#3. Write a Python program to get a string made of the
#first 2 and the last 2 chars from a given a string. If the string
#length is less than 2,return instead of the empty string.

#definindo strings para testar
string = 'a'
string3 = 'ab'
string2 = 'abcde'

#criando a função 
def get_string(string):
    nova = '' #string a ser retornada
    #se a string original é maior igual a 2 então pega as
    #primeiras e ultimas 2 letras
    if len(string) >= 2:
        nova = string[0] + string[1] + string[-2] + string[-1]
    return nova

get_string(string2)
get_string(string)
get_string(string3)



#4. Write a Python program to get a string from a given string where
#all occurrences of its first char have been changed
#to '$', except the first char itself.



def first(string):
    primeiro = string[0]
    nova = string.replace(primeiro, '$')
    nova = primeiro + nova[1:]
    return nova

string = 'minha mãe mexe com muitas coisas'
first(string)


#5. Write a Python program to get a single string from two
#given strings, separated by a space and swap the first
#two characters of each string.

def troca(string1, string2):
    resultado = string2[0:2] + string1[2:] + ' '+ string1[0:2] + string2[2:]
    return resultado

troca('abcd', 'wxyz')


'abcde'[:-1]























































































































