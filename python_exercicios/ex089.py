geral = []
notas = []
alunos = []
media = []
while True:
    alunos.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    geral.append(alunos[:])
    notas.clear()
    alunos.clear()
    resp = input('Quer continuar? [S/N] ').strip().upper()
    while resp != 'S' and resp != 'N':
        print('Não entendi')
        resp = input('Quer continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
for c in geral:
    media.append((c[1][0]+c[1][1])/2)
print('-='*30)
print('No. Nome      Media')
print('-'*18)
for c in range(len(geral)):
    print(f'{c}  {geral[c][0]}        {media[c]}')
while True:
    n=int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if n == 999:
        break
    while n> len(geral)-1:
        print('Número não existente digite outro',end='')
        n=int(input(''))
    print(f'As notas de {geral[n][0]} são {geral[n][1][0]} e {geral[n][1][1]}')
