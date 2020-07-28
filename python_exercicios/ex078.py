d = [int(input('Digite um valor para a posição 0: ')),
     int(input('Digite um valor para a posição 1: ')),
     int(input('Digite um valor para a posição 2: ')),
     int(input('Digite um valor para a posição 3: ')),
     int(input('Digite um valor para a posição 4: '))]
mv = men = d[0]
for c in d:
     if c>mv:
          mv=c
     if men>c:
          men=c
print(f'você digitou os valores{d}')
print(f'O maior valor digitado foi {mv} nas posições ',end='')
for i,v in enumerate(d):
     if v== mv:
          print(f'{i}',end='...')
print(f'\nO menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(d):
     if v== men:
          print(i,end='...')








