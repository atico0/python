from datetime import datetime
d = {}
d['nome'] = input('Nome: ')
d['ano'] = int(input('Data de nascimento: '))
d['idade'] = datetime.now().year-d['ano']
d['ctps'] = int(input('ctps (Se não tiver coloque 0): '))
if d['ctps'] !=0:
    d['contratação'] = int(input('Ano de contratação: '))
    d['salario'] = float(input('Digite seu salário: R$'))
    d['aposentadoria'] = d['idade']+(d['contratação']+35) - datetime.now().year
print('-='*31)
print(d)
print(f'O nome é: {d["nome"]}')
print(f'A idade é: {d["idade"]}')
if d['ctps'] != 0:
    print(f'O ctps é: {d["ctps"]}')
    print(f'A contratação é do ano: {d["contratação"]}')
    print(f'O salário é de: R${d["salario"]}')
    print(f'A aposentadoria vira com {d["aposentadoria"]} anos')

