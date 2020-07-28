def metade(p, ):
    return (p / 2)


def dobro(p, ):
    return p * 2


def aumentar(p, q):
    return (p * (1 + (q / 100)))


def diminuir(p, q):
    return (p * (1 - (q / 100)))


def moeda(v):
    n_v = (f'%1.2f' % (v)).replace('.', ',')
    return n_v


def resumo(v, a, r):
    print('-'*20)
    print('RESUMO DO VALOR')
    print('-'*20)
    print(f'preço analisado:   R${moeda(v)}')
    print(f'dobro do preço:    R${moeda(dobro(v))}')
    print(f'metade do preço:   R${moeda(metade(v))}')
    print(f'{a}% de aumento:   R${moeda(aumentar(v,a))} ')
    print(f'{r}% de redução:   R${moeda(diminuir(v,r))}')
