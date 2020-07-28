import re
#1 questão

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

num = input('Digite um número: ')
if is_int(num):
    if int(num)%2 == 0:
        print('É par')
    else:
        print('É impar')
else:
    print('Você não digitou um número inteiro')


# 2 questão
hr = input('Que horas são: ')
if is_int(hr):
    hr = int(hr)
    if hr<0 or hr>23:
        print('Hora invalida')
    else:
        if hr <= 11:
            print('Bom dia')
        elif 12<=hr<=17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('VOCE NÃO DIGITOU UM NÚMERO INTEIRO')



#3 questão


nome = input('Digite seu nome: ')
if not nome.isspace():
    tam = len(nome.strip())
    if tam <= 4:
        print('Seu nome é muito curto')
    elif 5<=tam<=6:
        print('Seu nome tem tamano normal')
    else:
        print('NOME GRANDE DAPORRA')

