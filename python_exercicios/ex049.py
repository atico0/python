from time import sleep
muti=int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11):
    print('{} x {} = {}'.format(muti,c,muti*c))
    sleep(0.5)