e = 1
d = 0
b = 0
c = 0
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
a = int(input('Quantos termos  você quer mostrar? '))
print('~~'*30)
while c!=a:
    b += d
    print(' {} -> '.format(b),end='')
    d = e
    e = b
    c += 1
print('FIM')
print('~~'*30)
