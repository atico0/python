produtos = []
produtos.append((1,30))
produtos.append((2,20))
produtos.append((3,50))
soma = sum([x[1] for x in produtos])
print(soma)
print(__name__)