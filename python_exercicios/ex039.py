from datetime import date

an = int(input('Digite seu ano de nascimento: '))
dt = date.today().year
id = dt - an
al = int
print('Quem nasceu em {} tem {} anos em {}'.format(an, id, dt))
if id == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif id > 18:
    al = id - 18
    print('Você deveria ter se alistado há {} anos'.format(al))
    print('seu alistamento foi em {}'.format(dt-al))
else:
    al=18-id
    print('Você ainda não tem 18 anos ainda faltam {} anos para o seu alistamento'.format(al))
    print('Seu alistamento sera em {}'.format(dt+al))
