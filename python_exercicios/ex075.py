n1 = int(input('Digite um número: '))
n2 = int(input('Outro número: '))
n3 = int(input('Outro número: '))
n4 = int(input('Ulimo número: '))
num= n1,n2,n3,n4
print(f' Você digitou os números: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if num[0] == 3 or num[1] == 3 or num[2] ==3 or num[3] == 3:
    print(f'O valor 3 foi digitado na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digtados foram ',end='')
for c in num:
    if c%2 == 0:
        print(c,end=' ')


