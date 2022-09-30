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


#6. Write a Python program to add 'ing' at the end of a
#given string (length should be at least 3). If the given
#string already ends with 'ing' then add 'ly' instead. If the string
#length of the given string is less than 3, leave it unchanged.

string1 = 'asdaffgs'
string2 = 'ab'
string3 = 'abcing'

def add_ing(string):
 
    if len(string) < 3: #testando se tem menos que caracteres
        resultado = string
    else:
        if string[-3:] == 'ing': #testando se termina com ing
            resultado = string + 'ly' #adicionando 'ly'
        else:
            resultado = string + 'ing' #adicionando 'ing'
    return resultado

add_ing(string1)
add_ing(string2)
add_ing(string3)

#7. Write a Python program to find the first
#appearance of the substring 'not' and 'poor' from a given
#string, if 'not' follows the 'poor', replace the whole
#'not'...'poor' substring with 'good'. Return the resulting string.



def not_poor(string):
    not_ = string.find('not')
    poor_ = string.find('poor')
    if (not_ >= 0 and poor_ > 0) and not_ < poor_:
        resultado = string.replace(string[not_: poor_ + 4], 'good')
    else: 
        resultado = string
    return resultado

string1 = 'The lyrics is not that poor!'
string2 = 'The lyrics is poor'

not_poor(string1)
not_poor(string2)
not_poor('not poor')
not_poor('asdnot rigthif askfhjjes adkfns poor kkkkkkk')




#8. Write a Python function that takes a list of words and return the
#longest word and the length of the longest one.


lista = ['mamão', 'varizes', 'papagaiada', 'sol']

def maior_tamanho(lista):
    maior = 0
    maior_palavra = ''
    for c in lista:
        # vendo se o tamanho da atual palavra é maior que o tamanho da 
        # maior palavra até então
        if len(c) > maior:
            #reatribuindo o tamanho da maior palavra e seu tamanho
            #caso a condição seja cumprida
            maior = len(c)
            maior_palavra = c
    return (maior_palavra, maior)

print(maior_tamanho(lista))


#9. Write a Python program to remove the nth index
#character from a nonempty string.

string = 'string com n valores'

def apaga_n(string, n):
    resultado = string[:n] + string[n+1:]
    return resultado

apaga_n(string, 1)
apaga_n(string, 0)


#10. Write a Python program to change a given string to a new string
#where the first and last chars have been exchanged.

string = 'string com n valores'
string2 = 'abcde'
def mudanca(string):
    resultado = string[-1] + string[1:-1] + string[0]
    return resultado

mudanca(string)
mudanca(string2)























































































