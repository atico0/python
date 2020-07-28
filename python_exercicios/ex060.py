n1=int(input('Digite um número:'))
num=n1
print('Calculando {}!= {}'.format(n1,n1),end='')
while num>1:
   n1*=(num-1)
   num-=1
   print('x {} '.format(num),end='')
print('=',n1)
