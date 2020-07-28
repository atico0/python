d = 0
a='-='*40
times = 'Flamengo','Fuminese','Atlético-MG','Cornthians',\
        'Palmeiras','Sport','América-MG','São Paulo','Grêmio','Vasco',\
        'Internacional','Botafogo','Cruzeiro','Vitória','Santos',\
        'Chapecoense','Atlético-PR','Bahia','Ceará','Paraná'
print(a)
print(f'Lista de times do brasileirão: {times}')
print(a)
print(f'Os primeiros colocados 5 são: {times[0:5]}')
print(a)
print(f'Os 4 ultimos colocados são: {times[-1:-5:-1]} ')
print(a)
print(f'Times em ordem alfabetica {sorted(times)}')
print(a)
for c in times:
    d +=1
    if c == 'Chapecoense':
        break
print(f'O Chapecoense está na {d} posição ')