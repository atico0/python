man=  0
men= 99**9990
peso=0
for c in range (1,6):
    peso=float(input('Peso da {} pessoa: '.format(c)))
    if peso>man :
        man=peso
    if peso<=men:
        men=peso
print('O maior peso lido foi de {:.2f}Kg'.format(man))
print('O menor peso lido foi de {:.2f}Kg'.format(men))