'''
** Gerente de Conta Bancária ** - Crie uma classe chamada Conta,
 que será uma classe abstrata para três outras
classes chamadas CheckingAccount, SavingsAccount e BusinessAccount. Gerenciar créditos
e débitos dessas contas através de um programa de estilo ATM.
'''
from abc import ABC, abstractclassmethod


class Conta(ABC):

    def __init__(self, dinheiro, credito):
        self.dinheiro = dinheiro
        self.credito = credito
        self.classe = self.__class__
        print(self.classe)

    def __str__(cls):
        print(cls.nome)

    @abstractclassmethod
    def saque(self):
        pass

    @abstractclassmethod
    def saldo(self):
        pass

    @abstractclassmethod
    def checa_credito(self):
        pass

    @abstractclassmethod
    def tipo_conta(self):
        pass


class CheckingAccount(Conta):
    nome = 'CheckingAccount'

    def saque(self, qt):
        if qt > (self.dinheiro+self.credito):
            print('Seu saldo e seu credito são menores')
            return
        self.dinheiro -= qt

    def saldo(self):
        print(f'Seu saldo é: {self.dinheiro}')

    def checa_credito(self):
        print(f'Seu credito é: {self.credito}')

    @classmethod
    def tipo_conta(cls):
        print(cls.nome)


class SavingsAccount(Conta):
    nome = 'SavingsAccount'

    def saque(self, qt):
        self.dinheiro -= qt

    def saldo(self):
        print(f'Seu saldo é: {self.dinheiro}')

    def checa_credito(self):
        print(f'Seu credito é: {self.credito}')

    def tipo_conta(cls):
        print(cls.nome)


class BusinessAccount(Conta):
    nome = 'BusinessAccount'

    def saque(self, qt):
        self.dinheiro -= qt

    def saldo(self):
        print(f'Seu saldo é: {self.dinheiro}')

    def checa_credito(self):
        print(f'Seu credito é: {self.credito}')

    def tipo_conta(cls):
        print(cls.nome)


a = CheckingAccount(700, 3000)
b = BusinessAccount(470, 2500)
a.saldo()
a.tipo_conta()
a.saque(700)
a.saldo()
a.saque(500)
a.saldo()
a.saque(2500)
a.saldo()
a.saque(3)
