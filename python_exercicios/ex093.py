d = dict()
l = []
d['nome'] = input('Nome: ')
part= int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(part):
    l.append(int(input(f'Quantos gols ele fez na partida {c+1}: ')))
d['gols'] = l
d['total'] = sum(l)
print('-='*29)
print(d)
print('-='*29)
print(f'O campo nome tem o valor {d["nome"]}')
print(f'O campo gols tem o valor {d["gols"]}')
print(f'O campo total tem o valor {d["total"]}  ')
print('-='*29)
print(f'O jogador {d["nome"]} jogou {part} partidas')
for c in range(part):
    print(f'=> Na {c+1} partida, fez {l[c]} gols.')
print(f'Foi um total de {sum(l)} gols.')