lista=[]
while True:
    num = int(input('Digite um valor: '))
    if lista.count(num) == 0:
        lista.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado não vou adicionar')
    pergunta=input('Deseja continuar? [S/N]').strip().upper()[0]
    while not pergunta in 'SN':
        print('Não entendi. ')
        pergunta=input('Deseja continuar? [S/N]').upper().strip()[0]
    if pergunta== 'N':
        break
lista.sort()
print('Você digitou os valores:',lista)