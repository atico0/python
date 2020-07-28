c = 1
while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if tabuada < 0:
        break
    while c <= 10:
        tab = tabuada * c
        print(f'{c} x {tabuada} = {tab}')
        c += 1
    print('-'*30)
    c -= 10
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE')