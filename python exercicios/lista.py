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











































































































