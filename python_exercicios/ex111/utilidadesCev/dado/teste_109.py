from ex111.utilidadesCev.moeda import ex109

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {ex109.metade(p, True)}')
print(f'O dobro de {p} é {ex109.dobro(p, False)}')
print(f'O aumento em 25% é {ex109.aumentar(p, 25, False)}')
print(f'Reduzindo em 30% temos {ex109.diminuir(p, 30, True)}')
