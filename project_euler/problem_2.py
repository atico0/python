a = 1
b = 0
soma = cont = 0
while True:
    if a > 4000000:
        break
    print(a)
    soma += a
    a = a + b
    b = a - b
print()
print(f'A soma é: {soma}')
