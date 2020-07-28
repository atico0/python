a = 600851475143
d = 13195
b = 0
primo = []
for c in range(a, 0, -1):
    primo = []
    print(c)
    for k in range(c, 2, -1):
        if (c % (k-1)) != 0:
            pass
        else:
            primo.append(1)
    if len(primo) == 0:
        if c != d:
            if d % c == 0:
                b = c
                break
if b != 0:
    print(f'O maior fator primo de {d} é {b}')
