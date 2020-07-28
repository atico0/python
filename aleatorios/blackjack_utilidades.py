from random import randint
from time import sleep


def mostra_pontos(a):
    print(f'Você possui {a} pontos')
    sleep(1)


def comparar(b, a):
    if a > 21 and b > 21:
        return 'EMPATOU'
    elif a > 21 >= b:
        return 'PERDEU'
    elif a <= 21 < b:
        return 'GANHOU'
    elif a > b:
        return 'GANHOU'
    elif a == b:
        return 'EMPATOU'
    else:
        return 'PERDEU'


def mostrar(lista):
    for m in range(len(lista)):
        print(f'{lista[m][0]} de {lista[m][1]}')
        sleep(0.5)


def contador(lista):
    soma = 0
    for z in range(len(lista)):
        if lista[z][0].isnumeric():
            soma += int(lista[z][0])
        else:
            if lista[z][0] == 'J' or lista[z][0] == 'Q' or lista[z][0] == 'K':
                soma += 10
            elif lista[z][0] == 'A':
                if (soma + 11) > 21:
                    soma += 1
                else:
                    soma += 11
    return soma


def organizar(lista):
    lista.sort()
    for k in range(len(lista)):
        if lista[k].isnumeric:
            lista[k] = int(lista[k])


class baralho(object):
    def __init__(self, naipe1, naipe2, naipe3, naipe4):
        self.naipes = [naipe1, naipe2, naipe3, naipe4]
        self.cartas = []
        for c in self.naipes:
            for x in range(2, 11):
                self.cartas.append((str(x), c))
            self.cartas.append(('A', c))
            self.cartas.append(('J', c))
            self.cartas.append(('Q', c))
            self.cartas.append(('K', c))


class mao(object):
    choice = []
    choice2 = []
    choice_dealer = []
    choices = [choice, choice2]

    def __init__(self):
        self.mao_da_mao = []
        self.mao2_da_mao = []

    def pegar(self, cartas, lista2):
        self.lista2 = lista2
        self.tamanho = len(cartas) - 1
        escolha = randint(0, self.tamanho - 1)
        self.lista2.append(cartas[escolha])
        del cartas[escolha]

    def dividir(self, lista):
        if len(self.mao_da_mao) == 0:
            self.choice2.append(self.choice[len(self.choice) - 1])
            del (self.choice[len(self.choice) - 1])
        else:
            self.mao2_da_mao.append(self.mao_da_mao[len(self.mao_da_mao) - 1])


def sumario(l):
    print('JOGADORES                DINHEIRO              apostados')
    print('---------                --------              ----------')
    for c in l.keys():
        print(f'{c:<20}        {l[c][0]} {l[c][1]:>20}')
