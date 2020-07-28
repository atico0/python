def fatorial(num):
    mt = 1
    for c in range(1, num + 1):
        mt *= c
    return mt


curiosos = []
for c in range(3, 999):
    soma = 0
    for k in str(c):
        soma += fatorial(int(k))
    if soma == c:
        curiosos.append(c)
    print(c)
print(curiosos)
print(145 + 40585)
