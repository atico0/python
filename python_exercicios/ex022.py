from time import sleep
nome=input('Digite seu nome completo: ')
p=(nome.replace(' ','' ))
s=nome.split()
print('Analisando seu nome',end='')
print('.',end='')
print('.',end='')
print('.')
sleep(3)
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras ao todo'.format(len(p)))
print('Seu primeiro nome é {} e ele tem letras'.format(s[0]),len(s[0]))

