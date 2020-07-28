lista = []
expr = input('Digite sua expressão matemática: ')
for c in expr:
    if c == '(':
         lista.append(c)
    elif c==')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)== 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão NÃO é valida!')
