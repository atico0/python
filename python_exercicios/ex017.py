import math
n=float(input('Digite o comprimento do cateto oposto: '))
s=float(input('Digite o comprimento do cateto adjacente: '))
d=n**2+s**2
m=math.sqrt(d)
print('O comprimento da hipotenusa é: {:.2f} '.format(m))