'''
** Inventário de produto ** - Crie um aplicativo que gerencie
um inventário de produtos. Crie uma classe de produto que tenha um preço,
 ID e quantidade à mão. Em seguida, crie uma classe
*inventory* que rastreie vários produtos e possa somar o valor do inventário.
'''
class Inventory:
    def __init__(self, produtos):
        self.produtos = produtos
        pass

    def soma(self):
        soma = 0
        for c in self.produtos:
            mt = (c.preco * c.qt)
            soma += mt
        return soma


class Produto:
    def __init__(self, preco, id, qt):
        self.preco = preco
        self.id = id
        self.qt = qt

    def info(self):
        print(f'Preço: R${self.preco}')
        print(f'ID: {self.id}')
        print(f'quantidade: {self.qt}')

p1 = Produto(600,1,2)
p2 = Produto(550,1,7)
p3 = Produto(4,1,10)
p4 = Produto(3000,1,0)
todos = Inventory([p1,p2,p3,p4])
print(f'A soma do inventario é: {todos.soma()}')