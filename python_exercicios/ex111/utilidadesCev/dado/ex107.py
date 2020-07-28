from ex111.utilidadesCev.moeda import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'O aumento em 25% é {moeda.aumentar(p, 25)}')
print(f'Reduzindo em 30% temos {moeda.diminuir(p, 30)}')
