def divisor(n1, n2):
    try:
        n1 / n2
    except:
        raise ZeroDivisionError


def divisor2(n1, n2):
    return n1 / n2

def divisor3(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0\n')
    return n1 / n2


try:
    divisor2(1, )
except ValueError as error:
    a = error

    print(f'O erro {error} ainda está aqui')
print(a)
