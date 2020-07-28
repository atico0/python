from datetime import datetime

a = int(input('Digite seu ano de nascimento: '))


def voto(b):
    b = datetime.now().year - b
    if 16<b<=18:
        return (f'Idade: {b}, voto: Proibido')
    elif 18 <= b < 65:
        return (f'Idade: {b}, voto: Obrigatorio')
    elif 18>b>=16 or 65<=b:
        return (f'Idade: {b}, voto: Opicional')


print(voto(a))
