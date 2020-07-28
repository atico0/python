dicio = {}
divisores = []
lista = []
for c in range(2, 10001):
    divisores = []
    for k in range(c,0,-1):
        if c % k == 0 and c != k:
            divisores.append(k)
    if sum(divisores) in dicio:
        dicio[sum(divisores)] += [c]
    else:
        dicio[sum(divisores)] = [c]
print(dicio)
duplas = []
n = []
for c in dicio.keys():
    for k in dicio[c]:
        if dicio.get(k, 0) != 0:
            n = dicio.get(k)
            for v in n:
                if v == c:
                    duplas.append((v,k))
print(duplas)
soma = 0
for c in duplas:
    soma += sum(c)
print(soma)
#incompleta