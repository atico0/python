c = 0
lista =[]
while True:
    lista.append(int(input('Digite um valor: ')))
    cont=input('Deseja continuar? [S/N]').strip().upper()
    c+=1
    while not cont[0] in 'SN':
        print('Desculpe mas não entendi.')
        cont=input('Deseja continuar? [S/N]').upper().strip()
    if cont[0]== 'N':
        break
print("-="*30)
lista.sort()
lista.reverse()
print(f'foram digitas {c} números')
print(f'os valores da lista em ordem decrescente são{lista}')
if lista.count(5)!=0:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte desta lista')