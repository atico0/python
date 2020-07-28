pes = []
dados = []
cont = 0
resp = str()
# cria a lista com as pessoas e pesos
while True:
    pes.append(input('Digite seu nome: '))
    pes.append(float(input('Digite seu peso: ')))
    dados.append(pes[:])
    pes.clear()
    cont += 1
    resp = input('Deseja continuar? [S/N]').strip().upper()
    while resp != 'S' and resp != 'N':
        print('Não entendi')
        resp = input('Deseja continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
#verifica qual o maior e menor peso das pessoas
maior = menor = 0
for c in range(len(dados)):
    if c == 0:
        maior = menor = dados[c][1]
    elif c != 0:
        if dados[c][1] >= maior:
            maior = dados[c][1]
        if dados[c][1] <= menor:
            menor = dados[c][1]
# ve quais pessoas possuem o maior e menor peso
l_maior = []
l_menor = []
for c in range(len(dados)):
    if dados[c][1] == maior:
        l_maior.append(dados[c][0])
    if dados[c][1] == menor:
        l_menor.append(dados[c][0])
print('-='*30)
#prints
print(f'Você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de: ')
for c in l_maior:
    print(c,end=',')
print('')
print(f'O menor peso foi de {menor}Kg. Peso de: ')
for c in l_menor:
    print(c,end=',')

