l1 = []
l2 = []
l3 = []
matrix = [l1,l2,l3]
for c in range(3):
    for x in range(3):
        matrix[c].append(input(f'Digite o valor para [{c,x}]'))
print(matrix)
for c in matrix:
    for x in c:
        print(f'[{x:^5}]',end=' ')
    print('')