l = []
while True:
    l.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N]').strip().upper()
    while resp != 'S' and resp != 'N':
        print('Não entendi. Digite novamente')
        resp = input('Quer continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
l.sort()
l.reverse()
if 5 in l:
    print('Você digitou o valor 5')
else:
    print('Você não digitou o valor 5')
print(f'Foram digitados {len(l)} valores , lista em ordem decrescente:{l} ')

