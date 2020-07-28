i = []
p = []
l = [i,p]
for c in range (7):
    n = int(input(f'Digite o {c+1} valor: '))
    if n%2 == 0:
        p.append(n)
    else:
        i.append(n)
print('-='*30)
print(f'Os valores impares digitados foram: {sorted(i)}')
print(f'Os valores pares digitados foram: {sorted(p)}')