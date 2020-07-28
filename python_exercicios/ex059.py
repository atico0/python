from time import sleep
c=0
while c!=5:
    n1=int(input('Digite um número: '))
    n2=int(input('Outro número: '))
    print('''------- Escolha uma opçao -------
    [1] Somar
    [2] Mutiplicar
    [3] Mostrar maior número
    [4] Escolher novos números
    [5] Sair do programa''')
    c=int(input('>>>>> Escolha sua opção: '))
    if c==1:
        print('O resultado de {} + {} é igual a {}'.format(n1,n2,n1+n2))
    elif c==2:
        print('A mutiplicação entre {} x {} é igual a {}'.format(n1,n2,n1*n2))
    elif c==3:
        if n1>n2:
            mn=n1
        elif n1==n2:
            mn=n1
        else:
            mn=n2
        print('O maior número digitado foi {} '.format(mn))
    elif c==4:
        print('Informe os números novamente:')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif c==5:
        print('Finalizando...')
    else:
        print('Escolha invalida tente novamente')
    sleep(2)
    print('-=-'*20)
