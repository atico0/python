# 1)

def func(ttf='QUALQUER COISA'):
    return ttf


def func2(funcao=func()):
    return funcao


print(func2())


# 2)
def raca(ttf='BULDOG'):
    return ttf


def dados(tamanho=100, peso=50):
    return [tamanho, peso]


def cao(f1= raca, f2 =dados() ):
    print(f'Meu cachorro é da raça {f1()}, tem {f2[0]}cm e {f2[1]}Kg')


cao()

def mestre(f):
    print(f)

def f1(p1,p2,p3):
    return p1+p2+p3


def f2(p1):
    return p1

mestre(f2(4))



a = [1,2,3]
b = (3,4,5,6,a)
print(b)
a[0] = 30000
print(b)
