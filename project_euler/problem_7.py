primos = [2]
cont = 3
vrf = []
while len(primos) != 10001:
    vrf = []
    for c in range(cont-1, 1, -1):
        if cont % c == 0:
            vrf.append(1)
        else:
            pass
    if not vrf:
        print(cont)
        primos.append(cont)
    cont += 1
print(primos)