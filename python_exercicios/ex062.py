c=0
d=10
pt=int(input('Primeiro termo: '))
razao=int(input('Razão: '))
while c!=d:
    print('{} -> '.format(pt),end='')
    pt+=razao
    c+=1
    if c==d:
        print('PAUSA')
        f=int(input('Você quer mostrar mais quantos termos? '))
        d+=f
print('PA finalizada, no total foram mostrados {} termos'.format(c))
