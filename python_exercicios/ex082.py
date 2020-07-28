lista = []
impar = []
par = []
while True:
    lista.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar? [S/N]')).strip().upper()
    while not cont[0] in 'SN':
        print('Não entendi')
        cont=str(input('Deseja continuar? [S/N]').strip().upper())
    if cont[0] == 'N':
        break
for c in lista:
    if c%2==0:
        par.append(c)
    elif c%2==1:
        impar.append(c)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')