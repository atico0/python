def moeda(v):
    n_v = (f'%1.2f' % (v)).replace('.', ',')
    return n_v


def metade(p, r=False):
    if r:
        return moeda(p / 2)
    else:
        return (p / 2)


def dobro(p, r=False):
    if r:
        return moeda(p * 2)
    else:
        return p * 2


def aumentar(p, q, r=False):
    if r:
        return moeda(p * (1 + (q / 100)))
    else:
        return p * (1 + (q / 100))


def diminuir(p, q, r=False):
    if r:
        return moeda(p * (1 - (q / 100)))
    else:
        return p * (1 - (q / 100))
