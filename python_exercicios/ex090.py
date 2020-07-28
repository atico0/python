situ = {}
situ ['nome'] = input('Nome: ')
situ['media'] = float(input('Media: '))
if situ['media']>=7:
    situ['situção'] = 'Aprovado'
elif 5<situ['media']<7:
    situ['situação'] = 'Em recuperação'
else:
    situ['situação'] = 'Reprovado'
print(situ)