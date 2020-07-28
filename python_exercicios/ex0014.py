n=float(input('\033[1mInforme a temperatura em celsius:'))
s=n/5
d=s*9+32
print('\033[30mA temperatura de {}C corresponde a \033[1;31m{:.2f} F'.format(n,d))
