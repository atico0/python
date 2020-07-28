mid = mmi = nh = 0
while True:
    cont = sex = 'a'
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    id = int( input('Idade: '))
    while sex not in 'MF':
        sex = str(input('Sexo: [F/M] ')).upper().strip()[0]
    print('-' * 30)
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if id > 18:
        mid +=1
    if sex in 'M':
        nh +=1
    if sex in 'F' and id < 20:
        mmi +=1
    if cont in 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {mid}
Ao todo temos {nh} homem(ns) cadastrado(s)
E temos {mmi} mulher(es) com menos de 20 anos''')



