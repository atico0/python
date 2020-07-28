d=float(input('6ual é a distância da sua viagem? '))
if d<= 200:
    m=d*0.50
else:
    m=d*0.45
print('Você está prestes  começar uma viagem de {}km '.format(d))
print('E o preço da sua passagem será de R${:.2f}'.format(m))