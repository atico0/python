man = soma =  0
c = 0
men = 999**999
resp='S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma+=num
    c += 1
    if num > man:
        man = num
    if num<men:
        men =  num
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print('Foram digitados {0} números e a media entre eles é {1}'.format(c,soma/c))
print('O maior valor digitado foi {0} e o menor foi {1}'.format(man,men))