#Encontre o número inteiro positivo único cujo quadrado possui o formato 1_2_3_4_5_6_7_8_9_0,
#onde cada "_" é um único dígito
from random import randint
while True:
    numero = int(f'1{randint(0,9)}2{randint(0,9)}3{randint(0,9)}4{randint(0,9)}5{randint(0,9)}6{randint(0,9)}' \
             f'7{randint(0,9)}8{randint(0,9)}9{randint(0,9)}0')
    numero_int = int(numero)
    numero_Tint = numero_int ** 0.5
    print(numero_int,numero_Tint)

    if numero_Tint == int(numero_Tint):
        break

print(f'É O NÚMERO: {numero_Tint} ')
print(numero_Tint**2)
print(numero)

a = 1.00
print(a == int(a))