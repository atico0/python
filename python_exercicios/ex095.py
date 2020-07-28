d = dict()
l = []
tudo = []
while True:
    d['nome'] = input('Nome: ')
    part= int(input(f'Quantas partidas {d["nome"]} jogou? '))
    for c in range(part):
        l.append(int(input(f'Quantos gols ele fez na partida {c+1}: ')))
    d['gols'] = l[:]
    d['total'] = sum(d['gols'])
    tudo.append(d.copy())
    l.clear()
    d.clear()
    resp = input('Quer continuar? [S/N]').upper().strip()
    while resp !='N' and resp != 'S':
        print('Não entendi')
        resp = input('Quer continuar? [S/N]').strip().upper()
    print('-='*29)
    if resp == 'N':
        break
while True:
    print('Cod nome    gols     total')
    print('-'*20)
    for c in range(len(tudo)):
       print(f'{c} {tudo[c]["nome"]}    {tudo[c]["gols"]}     {tudo[c]["total"]}')
    escolha  = int(input('Mostrar dados de qual jogador? '))
    while escolha > c:
       escolha = int(input(f'Não existe este cogido digite novamente: '))
    print(tudo[escolha])
    print(f'Levantamento do jogador {tudo[escolha]["nome"]}')

    for c in range(len(tudo[escolha]["gols"])):
       print(f'Na {c+1} partida fez {tudo[escolha]["gols"][c]}')
    resp = input('Quer continuar? [S/N]').strip().upper()
    while resp !='S' and resp != 'N':
         resp = input('Não entendi. Digite dnv: [S/N]').upper().strip()
    if resp == 'N':
        break
