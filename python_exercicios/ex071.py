print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
tot1 = 0
while True:
    if total >= ced:
        total -= ced
        tot1 += 1
    else:
        if tot1 > 0:
            print(f'Total de {tot1} cédulas de R${ced}')
        if ced == 50:
            ced = 20
            tot1 = 0
        elif ced == 20:
            ced = 10
            tot1 = 0
        elif ced == 10:
            tot1 = 0
            ced = 1
        if total == 0:
            break
print('=-'*30)
print('{:^30}'.format('VOLTE SEMPRE'))
print('-='*30)



