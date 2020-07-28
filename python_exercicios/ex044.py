print('{}LOJAS SARAIVA{}'.format('='*20,'='*20))
preço=float(input('Preço das compras: R$'))
print('Formas de pagamento')
print("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão  
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
n=int
m=float()
escolha=int(input('Qual é a opção? '))
if escolha==1:
    m=0.90*preço
elif escolha==2:
    m=0.95*preço
elif escolha==3:
    m=preço
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(preço/2))
else:
    n=int(input('Quantas parcelas? '))
    m = 0.20*preço+ preço
    s=preço
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(n,(m)/n))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,m))