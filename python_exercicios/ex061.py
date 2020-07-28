c=0
print('GERADOR DE PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razao  = int(input('Razão: '))
while c!=10:
    print('{} -> '.format(primeiro),end='')
    primeiro+=razao
    c+=1
print('FIM')