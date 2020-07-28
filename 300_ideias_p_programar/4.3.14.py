carac = input('Digite uma cadeia de caracteres (até 255): ')
while len(carac)>255:
    print('Não pode ser mais de 255 caracteres')
    carac = input('Digite novamente: ')
cont_e = carac.count(' ')
cont_p = len(carac.split())
cont_A = carac.count('a') + carac.count('A')
cont_v = 0
for c in carac.upper():
    if c in 'AÁÀÃÂEÉÈÊIÍÌOÓÒÕÔUÚÙÛ':
        cont_v += 1
print(f'A quantidade de espaços em branco é: {cont_e}; a quantidade de palavras é: {cont_p};  a quantidade de letras a é {cont_A} e a quantidade de vogais é {cont_v}')