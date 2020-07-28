sexo=input('Informe seu sexo: [M/F] ').upper().strip()[0]
while sexo!='M' and sexo!='F':
    erro=input('Dados inválidos. Por favor informe seu sexo: ').strip().upper()[0]
    sexo= erro
print('Sexo {} registrado com sucesso'.format(sexo.upper()))
