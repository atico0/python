from blackjack_utilidades import *
from itertools import tee

dicio = {}
grana = 5000
baralhos = [baralho('Paus', 'Copas', 'Espadas', 'Valetes'), baralho('Paus', 'Copas', 'Espadas', 'Valetes'),
            baralho('Paus', 'Copas', 'Espadas', 'Valetes'), baralho('Paus', 'Copas', 'Espadas', 'Valetes')]
cartas = []
mao1 = mao()
mao2 = mao()
mao3 = mao()
mao4 = mao()
mao5 = mao()
maos = [mao1, mao2, mao3, mao4, mao5]
for c in baralhos:
    cartas += c.cartas
for c in range(5):
    resposta = input('Quer registar algum jogador? [S/N]').strip().upper()
    while resposta != 'N' and resposta != 'S':
        print('Não entendi digite novamente')
        resposta = input('Quer registar algum jogador? [S/N]').strip().upper()
    if resposta == 'N':
        break
    a = input('Digite seu nome: ')
    print(f'Jogador {a} registrado.')
    dicio[a] = []
    dicio[a].append(grana)
    dicio[a].append(0)
    dicio[a].append(maos[c])
    dicio[a].append(0)
if len(dicio) == 0:
    print('Sem jogadores registrados')
else:
    while True:
        sumario(dicio)
        for c in dicio.keys():
            if dicio[c][0] > 0:
                dicio[c][1] = input(f'Quanto você quer apostar {c}? R$')
                while not dicio[c][1].isnumeric and  dicio[c][1] > dicio[c][0]:
                    dicio[c][1] = input(f'Valor invalido. Digite novamente {c}')
                dicio[c][1] = int(dicio[c][1])
                dicio[c][0] = dicio[c][0] - dicio[c][1]
            else:
                print(f'O jogador {c} não tem mais dinheiro pra apostar')
        for k in dicio.keys():
            escolhas = 0
            if dicio[k][1] < 0:
                while escolhas != 2:
                    print(f'Sua vez {k} escolha:')
                    escolhas = input('[1] PEGAR\n[2] RECUSAR')
                    while (not escolhas.isnumeric()) and (escolhas != '1' and escolhas != '2'):
                        print('Valor invalido.')
                        escolhas = input('[1] PEGAR\n[2] RECUSAR')
                        escolhas = int(escolhas)
                        if escolhas == 1:
                            dicio[k][2].pegar(cartas, dicio[k][2].mao_da_mao)
                            print(f'{k} recebeu a carta: {dicio[k][2].mao_da_mao[-1][0]} de {dicio[k][2].mao_da_mao[-1][1]}')
                            print('Sua mão é:')
                            mostrar(dicio[k][2].mao_da_mao)
                        dicio[k][-1] = contador(dicio[k][2].mao_da_mao)
                        if dicio[k][-1] == 21:
                            print(f'O jogador {k} completou 21 pontos')
                        elif dicio[k][-1] > 21:
                            print(f'O jogador {k} estorou')
    dealer_mao = mao()
    dealer = [dealer_mao, 0]
    while dealer[1] < 21:
        dealer[0].pegar
        dealer[1] = contador(dealer[0].mao_da_mao)
    for c in dicio.keys():
        resultado = comparar(dicio[c][3],dealer[1])
        print(f'{c} {resultado}')
        if resultado == 'GANHOU':
            dicio[c][0] += dicio[c][1]*2
            dicio[c][1] = 0
        if resultado == 'EMPATOU':
            dicio[c][0] += dicio[c][1]
            dicio[c][1] = 0
        if resultado == 'PERDEU':
            dicio[c][1] = 0