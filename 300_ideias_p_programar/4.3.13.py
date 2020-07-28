carac = input('Digite uma cadeia de caracteres (até 255): ')
while len(carac)>255:
    print('Não pode ser mais de 255 caracteres')
    carac = input('Digite novamente: ')
cont_e = carac.count(' ')
cont_p = len(carac.split())
cont_A = carac.count('a') + carac.count('A')
print(f'A quantidade de espaços em branco é: {cont_e}; a quantidade de palavras é: {cont_p} e  a quantidade de letras a é {cont_A}')
