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

string = 'apaga o indice n da string'

def apaga_n(string, n):
    #cria nova string com a string original mas
    #sem o n-ésimo caractere
    resultado = string[:n] + string[n+1:]
    return resultado

#testando a função
apaga_n(string, 1)
apaga_n(string, 0)


#10. Write a Python program to change a given string to a new string
#where the first and last chars have been exchanged.

string = 'string com n valores'
string2 = 'abcde'

#definindo função
def mudanca(string):
    #definindo a resultado igual a string original
    #mas com o ultimo e os primeiro caracteres trocados
    resultado = string[-1] + string[1:-1] + string[0]
    return resultado

mudanca(string)
mudanca(string2)



#11. Write a Python program to remove the characters which have
#odd index values of a given string.

string = 'abcdefghij'
string[0::2]
string2 = 'Python'
string2[0::2]

#definindo função
def pega_par(string):
    #definindo nova string só com os elementos da string 
    #original que tem o indice par na string
    nova_string = string[0::2]
    #retornando nova_string
    return nova_string

#função da resposta
def pega_par2(string):
    #definindo nova string
    nova_string = ''
    #percorrendo a string pelos indices
    for i in range(len(string)):
        #vendo se o indice é par
        if i % 2 == 0:
            #concatenando a nova_string com a i-ésima string caso
            #a condição for True
            nova_string += string[i]
    #retornando nova_string
    return nova_string


#testando funções
pega_par(string)
pega_par(string2)
pega_par2(string)
pega_par2(string2)




#12. Write a Python program to count the occurrences
#of each word in a given sentence.

#definindo função
def conta_palavras(string):
    #definindo lista como palavras de uma string
    lista = string.lower().split()
    #definindo dicionario
    dicio = {}
    #percorrendo a lista de palavras
    for i in range(len(lista)):
        #testando se a i-ésima palavra da lista
        #é uma chave do dicionario
        if lista[i] in list(dicio.keys()):
            #incrementando 1 ao elemento do dicionario 
            #de chave lista[i]
            dicio[lista[i]] += 1
        else:
            #adicionando o elemento 1 ao dicionario 
            #com a chave lista[i] caso essa chave não conste no dicio
            dicio[lista[i]] = 1
    #retornando dicionario
    return dicio


#testando função

string = 'nova conta python news nova minha cabra CABRA'

conta_palavras(string)
conta_palavras('the quick brown fox jumps over the lazy dog.')




#13. Write a Python script that takes input from the user
#and displays that input back in upper and lower cases.

#pegando input da string
string = input('Digite o input: ')
#printando string em maiuscula
print(f'EM LETRA MAIUSCULA: {string.upper()}')
#printando string em minuscula
print(f'EM LETRA MINUSCULA: {string.lower()}')





#14. Write a Python program that accepts a comma separated sequence
#of words as input and prints the unique words in
#sorted form (alphanumerically).

string = 'red, white, black, red, green, black'

#definindo função
def ordena_string(string):
    #definindo a lista como os elementos da string divididos por ', '
    lista = string.split(', ')
    #ordenando a lista
    lista.sort()
    #criando string que é composta pelos elementos da lista ordenada
    #separados por ', '
    nova_string = ', '.join(lista)
    #retornando nova string
    return nova_string
#testando função
ordena_string(string)    


#15. Write a Python function to create the HTML string
#with tags around the word(s).

#definindo função
def add_tags(char, string):
    #criando nova string em formato de tag
    nova_string = '<'+char+'>'+string+'<'+char+'>'
    #retornando nova_string
    return nova_string

add_tags('i', 'Python')
add_tags('b', 'Python Tutorial')


















































