c=0
from time import sleep
from random import randint
numero=randint(0,10)
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será 6ue você consegue adivinhar 6ual foi: """)
palpite=int
while palpite!=numero:
    palpite=int(input('6ual é o seu palpite? '))
    sleep(1)
    if palpite<numero:
        print('Mais... tente novamente')
        sleep(1)
    elif numero<palpite:
        print('Menos... tente novamente')
        sleep(1)
    c+=1
print('Acertou com {} tentativas. Parabéns!'.format(c))
