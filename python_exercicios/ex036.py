vc=float(input('Valor da casa: R$'))
s=float(input('Seu salário: R$'))
ap=int(input('Vai pagar em quantos anos: '))
tp=(s*30)/100
m=vc/(ap*12)
if m>tp:
    print('''Para pagar uma casa de R${:.2f} em {} anos
a prestação sera de R${:.2f} Empréstimo NEGADO!'''.format(vc,ap,m))
else:
    print('Emprestimo APROVADO! A prestação sera de R${:.2f} '.format(m))
