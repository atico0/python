extensos = 'ZERO','UM','DOIS','TRÊS',\
           '6UATRO','CINCO','SEIS',\
           'SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE',\
           '6UATORZE','6UINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while  num<0 or num>20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extensos[num]} ')
    cont = input('Quer continuar? [S/N]').strip().upper()[0]
    while not cont in ('SN'):
        cont = input(' TENTE NOVAMENTE. Quer continuar?').strip() .upper()[0]
    if cont == 'N':
        break

