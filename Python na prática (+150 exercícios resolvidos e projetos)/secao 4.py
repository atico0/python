# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:55:15 2022

@author: luisg
"""

#Exercício 1
#Escreva um programa que mostre a mensagem 'Hello World!' na tela.

print('Hello World!')




#Exercício 2
#Faça um programa que solicite um número do usuário e apresente
#a seguinte mensagem na tela:
#"O número digitado foi [número]".

num = input('Digite um npumero: ')
print("O número digitado foi", num)



#Exercício 3
#Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final
#o programa deverá apresentar o nome completo do usuário na tela.

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print('Seu nome completo é:', nome, sobrenome)






#Exercício 4
#Faça um programa que solicite três números
#inteiros do usuário e imprima a soma destes.

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
print('A soma é:',n1+n2+n3)





#Exercício 5
#Escreva um programa que solicite duas notas do usuário e apresente
#a média na tela da seguinte forma:

#"A média das notas [nota1] e [nota2] é [média]"

n1 = int(input('n1: '))
n2 = int(input('n2: '))
media = (n1+n2)/2
print(f'A média das notas {n1} e {n2} é {media}')

#Exercício 6
#Faça um programa que calcule a raiz quadrada de um número. O usuário
#deve inserir um número e o programa deve mostrar na tela o
#resultado da raiz quadrada do número inserido.

n = int(input('n: '))
raiz = n**0.5
print(raiz)



#Exercício 7
#Faça um programa que peça 5 números de ponto flutuante do usuário
#e apresente no final a média dos números digitados.

soma = 0
for c in range(1,6):
    soma += float(input(f"Digite n{c}: "))
print(f'A média é: {soma/5}')



#Exercício 8
#Escreva um programa que faça a conversão de um dado
#valor de metro para quilômetro.


metros = float(input("Digite os metros: "))
print(f'{metros/1000}KM')




#Exercício 9
#Escreva um programa que calcule a área de uma circunferência.
#O usuário deve digitar o valor do raio e ao final o programa deverá
#mostrar na tela a área da circunferência.

#Use a fórmula: área=pi*r²,
#em que pi é uma constante e r o raio da circunferência.

#Dica: você pode usar a biblioteca math para pegar a constante pi.


from math import pi
raio = float(input('Digite o raio: '))
area = pi*raio**2
print(f'Área: {area}')



#Exercício 10
#Faça um programa que peça uma temperatura em Fahrenheit (F) e converta
#esta temperatura para grau Celsius (C),
#mostrando o resultado da conversão na tela.

#Use a fórmula: C = 5 * ((F-32) / 9).


f = float(input('Digite a temperatura em Fahrenheit: '))
c = 5 * ((f-32) / 9)

print(f'A temp em celsius é: {c} C')








































