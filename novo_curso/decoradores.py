def a(funcao):
    def f_da_f(*args,**kwargs):
        print(f'Parte adicionada')
        funcao(*args,**kwargs)
    return f_da_f

@a
def c():
    print('parte da função original')
@a
def outra(num):
    print(f'ssó outra função pra ser decorada mas eu printo {num}')
#c = a(c)
#c()
outra(3)