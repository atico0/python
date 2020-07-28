cont = 3
vrf = []
primos = [2]
while cont != 20000:
    vrf = []
    for c in range((cont) - 1, 1, -1):
        if cont % c == 0:
            vrf.append(1)
        else:
            pass
    print(cont)
    if not vrf:
        primos.append(cont)
    cont +=1
print(primos)
print(sum(primos))