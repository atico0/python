def primo(n):
    for c in range(n-1,1,-1):
        if n%c == 0:
            return False
    return True
l = [x for x in range(2,1000) if primo(x)]
cont = 0
soma = 0
somados = []
resultados = []
tam_soma = []
print(l)
print('=-'*30)
lista_somados = []
vrf = False
dicio = {}
for c in l:
    cont = l.index(c)
    soma = 0
    somados = []
    while cont<len(l) and soma + l[cont]< 1000:
        soma += l[cont]
        somados.append(l[cont])
        if primo(soma):
            dicio.update({soma: somados})
        cont += 1
    soma = max(list(dicio.keys()))
    somados = dicio[soma]
    if primo(soma) and len(somados) > 1:
        tam_soma.append(len(somados))
        resultados.append(soma)
        lista_somados.append(somados)
        vrf = True
    if vrf:
        break
indexf= tam_soma.index(max(tam_soma))
print(resultados)
print('=-'*30)
print(resultados[indexf],indexf)
print('=-'*30)
print(lista_somados[indexf],len(lista_somados[indexf]))
print('=-'*30)
print(lista_somados)
print('=-'*30)
print(tam_soma)