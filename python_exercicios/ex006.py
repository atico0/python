n=int(input('\33[4;37mDigite sua primeira nota:'))
s=int(input('Digite sua segunda nota:\033[m'))
d=(n+s)/2
print('\033[30mA média entre suas notas é: \033[7;30m{}\033[m'.format(d))
