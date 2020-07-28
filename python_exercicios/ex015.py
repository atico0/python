n=float(input('\033[4;37mQuantos dias alugados?\033[m '))
s=float(input('\033[4;37mQuantos KM rodados?\033[m '))
m=n*60
d=s*0.15
print('\033[33mO toltal a pagar e de R${}'.format(m+d))