# 1)
def saudacoes(saud, nome):
    print(f'{saud} {nome}')


saudacoes('EAE', 'JOÃO')


# 2)
def soma(x, y, z):
    print(x + y + z)


soma(1, 2, 3)


# 3)
def porct(num, str):
    return num + num * (int(str[:-1]) / 100)


print(porct(50, '50%'))


# 4)
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num


print(fizzbuzz(2))
