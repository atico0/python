print('='*40)
print(' '*10,'10 TERMOS DE UMA PA')
print('='*40)
pt=int(input('Primeiro termo: '))
razao=(int(input('Razão: ')))
for c in range (0,10):
    # print(pt,end='->')
    print('{}->'.format(pt), end='')
    pt+=razao
print('Acabou')