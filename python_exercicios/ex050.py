cont=0
vv=0
for c in range (1,7):
     vd=int(input('Digite o {} número: '.format(c)))
     if vd%2==0:
        vv+=vd
        cont+=1
print('Você me informou {}  números pares e a soma entre eles foi {}'.format(cont,vv))


