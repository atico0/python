divisores = []
cont = 0
triang = 0
while len(divisores) !=500:
    divisores = []
    triang = 0
    for c in range(cont,0,-1):
        triang += c
    print(triang)
    for c in range(triang,0,-1):
        if triang % c == 0:
            divisores.append(1)
    cont +=1
print(triang)