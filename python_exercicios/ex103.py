n = input('Nome do jogador:')
g = input('Gols marcados: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    n = '<Desconhecido>'


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador: {nome} marcou {gols} gol(s) no campeonato')


ficha(n, g)
