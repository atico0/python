from ex111.utilidadesCev.moeda import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O aumento em 25% é {moeda.moeda(moeda.aumentar(p, 25))}')
print(f'Reduzindo em 30% temos {moeda.moeda(moeda.diminuir(p, 30))}')