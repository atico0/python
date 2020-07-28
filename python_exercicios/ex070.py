men = soma = c = d = 0

print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
while True:
    cont = '  '
    nome = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    d += 1
    soma += preço
    while cont not in ('NS'):
        cont = input('Quer continuar? [S/N]').strip().upper() [0]
    if d == 1 or preço < men:
        men = preço
        nmen = nome
    if preço > 1000:
        c += 1
    if cont in ('N'):
        break
print(f'''O total da compra foi R${soma:.2F}
Temos {c} produto custando mais de 1000 reais
O produto mais barato foi {nmen} que custa R${men:.2f} ''')



