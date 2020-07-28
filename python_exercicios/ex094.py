d = {}
l = []
while True:
    d['nome'] = input('Nome:')
    d['sexo'] = input('Sexo [M/F]: ').upper().strip()
    while d['sexo'] != 'M' and d['sexo'] != 'F':
        print('Não entendi')
        d['sexo'] = input('Sexo [M/F]: ').strip().upper()
    d['idade'] = int(input('Idade: '))
    l.append(d.copy())
    resp = input('Quer continuar? [S/N]').upper().strip()
    while resp != 'S' and resp != 'N':
        print('Não entendi')
        resp = input('Quer continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
print(f'O número de pessoas cadastradas foi {len(l)}')
# Media
media = 0
for c in l:
    media += c['idade']
media = media / len(l)
print(f'A media de idade é {media}')
# Lista de mulheres
l_mu = []
for c in l:
    if c['sexo'] == 'F':
        l_mu.append(c['nome'])
print(f'lista de mulheres:',end=' ')
for c in l_mu:
    print(c,end=' ')
print()
# Lista de pessoas com idade acima da média
l_ac = []
for c in l:
    if c['idade']>media:
        l_ac.append(c.copy())
print(f'Lista de pessoas com idade acima da média: ',end='')
for x in l_ac:
    for k,v in x.items():
        print(f'{k} = {v}',end='; ')
    print('')