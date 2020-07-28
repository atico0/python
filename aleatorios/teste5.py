from random import randint

resultados = ['Cara', 'Coroa']
conts = [0, 0]
while True:
    esc = input('Lançar moeda? [S/N]').strip().upper()
    while esc not in 'SN':
        print('Não entendi')
    if esc == 'S':
        a = randint(0, 1)
        print(f'O resultado é {resultados[a]}')
        conts[a] += 1
    else:
        break
print(f'''Resultado:
Caras: {conts[0]}
Coroas: {conts[1]}''')
# lançamento de cara ou coroa
