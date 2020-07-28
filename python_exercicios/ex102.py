n = int(input('número: '))


def fato(num, show=False):
    a = ''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            a += (f'{c} x ')
    a = a[:len(a)-2]
    if show:
        return f'{a} = {f}'
    else:
        return f


print(fato(n,True))
