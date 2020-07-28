l1 = []
l2 = []
l3 = []
matrix = [l1,l2,l3]
for c in range(3):
    for x in range(3):
        matrix[c].append(int(input(f'Digite o valor para [{c,x}]:')))
print(matrix)
for c in matrix:
    for x in c:
        print(f'[{x}]',end=' ')
    print('')
soma = 0
for c in matrix:
    for x in c:
        if x%2 == 0:
            soma += x
soma2 = matrix[0][2] + matrix[1][2] + matrix[2][2]
for c in range(len(l2)):
    if c == 0:
        maior = l2[c]
    else:
        if l2[c] >= maior:
            maior = l2[c]
print('=-'*30)
print(f'''A soma de todos os valores pares é {soma}
A soma de todos os valores da terceira coluna é {soma2}
O maior valor da segunda linha é {maior}
''')