from time import sleep
cont = 0
menor = 0
vrf = []
while len(vrf) != 20 :
    cont += 1
    vrf = []
    print(cont)
    for c in range(1, 21):
        if cont % c == 0:
            vrf.append(c)
    menor = cont
print(menor)
