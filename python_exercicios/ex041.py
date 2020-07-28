from datetime import date
an=int(input('Digite seu ano de nascimento: '))
id=date.today().year - an
if 9>=id>0:
    print('Sua categoria é  MIRIM')
elif 14>=id>9:
    print('Sua categoria é  INFANTIL')
elif 19>=id>14:
    print('Sua categoria é JUNIOR')
elif 20>=id>19:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
print('O atleta tem {} anos'.format(id))
