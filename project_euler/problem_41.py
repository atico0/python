for c in range(8765431,1,-1):
    pandigital = None
    pandigital_primo = None
    vrf = []
    vrf2 = []
    tamanho = len(str(c))
    print(c)
    vrf = [x for x in range(1, tamanho+1)]
    for k in vrf:
        if str(k) in str(c):
            vrf2.append(k)
    if len(vrf2) == len(vrf):
        pandigital = True
        vrf = []
        for v in range(2, c):
            if c % v == 0:
                vrf.append(1)
        if not vrf:
            pandigital_primo = True
    if pandigital_primo and pandigital:
        resul = c
        break
print('Resoltado:',resul)