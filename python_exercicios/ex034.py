s=float(input('6ual é o salário do funcionario? R$'))
p= (s*15/100)+s
d=(s*10/100)+s

if s>1250:
    print('6uem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s,d))
else:

    print('6uem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s,p    ))