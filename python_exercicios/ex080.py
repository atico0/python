#lista.insert(posiçao da lista,valor indexao a lista)
lista=[]
cont= 0
for c in range(0,5):
    num=int(input('Digite um valor: '))
    if c==0 :
        lista.append(num)
        print('Este número foi adicionado ao final  da lista...')
    elif num>=lista[-1]:
        print('Este número foi adicionado ao final da lista...')
        lista.append(num)
    else:
        pos=0
        while pos< len(lista):
           if num<=lista[pos]:
               lista.insert(pos,num)
               break
           pos+=1
        print(f'Este número foi adicionado a posição {pos} da lista')

print('-='*30)


print(f'Os valores digitados em ordem foram {lista}')
