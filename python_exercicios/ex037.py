num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1]Converter para binário
[2]Converter para octal
[3]Converter para hexadecimal''')
opc=int(input('sua opçao: '))
if opc==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opc==2:
    print('{} convertido para OCTONAL é igual a {}'.format(num,oct(num)[2:]))
elif opc==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Escolha de base incorreta por favor recomece o programa')
