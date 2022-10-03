#Questões
#https://www.w3resource.com/python-exercises/list/

#1. Write a Python program to sum all the items in a list.


def soma_lista(lista):
    #definindo soma
    soma = 0
    #percorrendo a lista
    for c in lista:
        #incrementando a soma com os valores da lista
        soma += c
    #retornando soma
    return soma

#testando função
soma_lista([1,27,-3])
soma_lista([6.5,43,2])
sum([1,27,-3])
sum([6.5,43,2])

#2. Write a Python program to multiply all the items in a list.+

def prod_lista(lista):
    #definindo a soma
    prod = 1
    #percorrendo a lista
    for c in lista:
        #incrementando o produto com os valores da lista
        prod *= c
    #retornando produto
    return prod
#testando função
prod_lista([1,27,-3])
prod_lista([6.5,43,2])


#3. Write a Python program to get the largest number from a list.
#4. Write a Python program to get the smallest number from a list.

def maior_menor(lista):
    #definindo o 
    maior = menor = lista[0]
    for c in lista[1:]:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    return (maior, menor)

#testando função
maior_menor([1,2,3,4])
max([1,2,3,4])
min([1,2,3,4])
maior_menor([1,2,33,4, -1])
max([1,2,33,4, -1])
min([1,2,33,4, -1])



#5. Write a Python program to count the number of strings where
#the string length is 2 or more and the first
#and last character are same from a given list of strings.


def conta_igual(lista):
    #definindo contador
    cont = 0
    #percorrendo lista de strings
    for c in lista:
        #vendo se cada string tem tamanho >=2 e 
        #se os primeiro e ultimo caracteres são iguais
        if len(c) >= 2 and c[0] == c[-1]:
            #incrementando contandor
            cont += 1
    #retornando contador
    return cont

def tam_maior_igual(lista, n):
    #definindo contador
    cont = 0
    #percorrendo lista
    for c in lista:
        #incrementando contador
        cont += 1
        #vendo se o contador é maior igual a n
        if cont >= n :
            #retornando True
            return True
    #retornando False
    return False
#testando função
tam_maior_igual([1,2,3], 0)
tam_maior_igual([1,2,3], 1)
tam_maior_igual([1,2,3], 2)
tam_maior_igual([1,2,3], 3)
tam_maior_igual([1,2,3], 4)

def conta_igual2(lista):
    #definindo contandor
    cont = 0
    for c in lista:
        #vendo se cada string tem tamanho >=2 e 
        #se os primeiro e ultimo caracteres são iguais
        if tam_maior_igual(c, 2) and c[0] == c[-1]:
            #incrementando o contador
            cont += 1
    #retornando o contador
    return cont

#testando funções
conta_igual(['abc', 'xyz', 'aba', '1221'])
conta_igual2(['abc', 'xyz', 'aba', '1221'])




#6. Write a Python program to get a list,
#sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.


#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

a = [3,2,4,5]
sorted(a)
a.reverse()
a.sort()
a
dicio = {1:'a', 2:'b'}
dicio[2]
dicio[3] = '3'
dicio

def organiza_tuplas(lista):
    #definindo dicionario que vai guardar
    #os maiores valores e seus index
    dicio = {}
    #definindo a lista final a ser retornada
    lista_final = []
    #percorrendo a lista de tuplas
    for i in range(len(lista)):
        #adicionando elementos no dicionario com a chave igual
        #ao ultimo elemento da tupla no indice i e valor igual
        #ao indice i
        dicio[lista[i][-1]] = i
    #definindo a lista de maiores como os as chaves do dicionario
    #ordenadas em ordem crescente
    maiores = sorted(list(dicio.keys()))
    #percorrendo a lista de maiores
    for i in maiores:
        #adicionando a lista final o elemento da lista (tupla)
        #que está no indice que está dentro do dicio com a chave i
        lista_final.append(lista[dicio[i]])
    return lista_final
    

#função da resposta
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

#testrando funções
organiza_tuplas([(2, 5,9), (1, 2,0,0,0), (4, 4), (2, 3), (2, 1)])
sort_list_last([(2, 5,9), (1, 2,0,0,0), (4, 4), (2, 3), (2, 1)])



#7. Write a Python program to remove duplicates from a list.

def remove_duplicatas(lista):
    #definindo lista final
    lista_final = []
    #percorrendo a lista
    for c in lista:
        #verificando se o elemento c pertence a lista final
        if c in lista_final:
            pass
        else:
            #adicionando o elemento c caso ele não pertença
            lista_final.append(c)
    return lista_final

def remove_duplicatas2(lista):
    return list(set(lista))

remove_duplicatas([1,2,2,5,8,0,5])
remove_duplicatas2([1,2,2,5,8,0,5])




#8. Write a Python program to check a list is empty or not.

bool([0])


def vazia(lista):
    #checando se a lista tem elementos
    if lista:
        print('Não vazia')
    else:
        print('Vazia')

#testando função
vazia([])
vazia([4])
vazia(0)
vazia(1)


#9. Write a Python program to clone or copy a list.

def copia(lista):
    #definindo copia
    copia = []
    #percorrendo os elementos da lista
    for c in lista:
        #adicionando os elementos da lista original na cópia
        copia.append(c)
    return copia

def copia2(lista):
    #retornando cópia da lista
    return list(lista)


#testando função
copia([1,2,3,4,3])
copia2([1,2,3,4,3])




#10. Write a Python program to find the list of words that are
#longer than n from a given list of words.


def longo_n(lista, n):
    #definindo lista final
    lista_final = []
    #percorrendo os elementos da lista
    for c in lista:
        #testano se o elemento c tem tamanho maior que n
        if len(c) > n:
            #adicionando o elemento c a lista final
            lista_final.append(c)
    return lista_final



def longo_n2(string, n):
    #define lista como o split das string original
    lista = string.split()
    #definindo lista final
    lista_final = []
    #percorrendo os elementos da lista
    for c in lista:
        #testano se o elemento c tem tamanho maior que n
        if len(c) > n:
            #adicionando o elemento c a lista final
            lista_final.append(c)
    return lista_final


#testando funções
longo_n(['sdfgfdsfgf', 'zdaf', 'top', 'a', 'b', 'ldkfgjfdf', 'aaaaa'],
        2)

longo_n(['sdfgfdsfgf', 'zdaf', 'top', 'a', 'b', 'ldkfgjfdf', 'aaaaa'],
        3)
longo_n(['sdfgfdsfgf', 'zdaf', 'top', 'a', 'b', 'ldkfgjfdf', 'aaaaa'],
        4)
longo_n2('sdfgfdsfgf zdaf  top a  b ldkfgjfdf aaaaa',2)
longo_n2('sdfgfdsfgf zdaf  top a  b ldkfgjfdf aaaaa',3)
longo_n2('sdfgfdsfgf zdaf  top a  b ldkfgjfdf aaaaa',4)






























































