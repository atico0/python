num = int(input('Escolha um número: '))
soma = 0
for c in range(1,num+1):
    soma += c/(num+1-c)
print(soma)