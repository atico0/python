cpf =  input('Digite seu CPF: ')
cpf_nums= []
for c in cpf:
    if c.isnumeric():
        cpf_nums.append(int(c))
cpf_nums_V = cpf_nums[:-2]
for c in range(2):
    soma = 0
    for indice, valor in enumerate(reversed(cpf_nums_V)):
        soma += (indice+2)*valor
    cpf_nums_V.append(0 if 9<11-(soma%11) else 11-(soma%11))
    print(cpf_nums_V)
if cpf_nums  == cpf_nums_V:
    print('CPF VALIDO')
else:
    print('CPF INVALIDO')