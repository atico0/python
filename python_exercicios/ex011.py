h=int(input('\033[4;36mDigite a altura da parede:'))
l=int(input('Digite a largura da parede:\033[m'))
n=h*l
print('\033[1;31mA parede tem uma área de {} metros quadrados e serão necessarios {} litros de tinta para pinta-la'.format(n,n/2))