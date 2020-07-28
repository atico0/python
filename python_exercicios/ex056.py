toot=0
maior=0
media=0
for c in range(1,5):
    print('-'*5,'{} PESSOA'.format(c),'-'*5)
    nome=(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=input('Sexo [M/F]: ')
    media+=idade
    if sexo in 'Mm' and  idade>maior:
        maior=idade
        hm=nome
    if sexo in 'fF' and idade<20:
        toot+=1
media= media/4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,hm))
print('Ao todo são {} mulheres com menos de 20 anos '.format(toot))