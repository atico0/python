from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, saldo, numero_conta):
        self.agencia = agencia
        self.saldo = saldo
        self.numero_conta = numero_conta

    @abstractclassmethod
    def sacar(self):
        pass

    @abstractclassmethod
    def depositar(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, angecia, saldo, numero_conta, limite):
        super().__init__(angecia, saldo, numero_conta)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print(f'Seu saldo é de {self.saldo}R$ e seu limite é {self.limite} logo você não pode sacar {valor}')
            return None
        self.saldo -= valor
        print(f'Seu novo saldo é de {self.saldo}R$')

    def depositar(self, valor):
        print(f'Você de depositou {valor}R$')
        self.saldo += valor
        print(f'Seu novo saldo é de {self.saldo}')

    def infos(self):
        print(f'Saldo: {self.saldo}; Limite: {self.limite}; Agencia: {self.agencia}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, saldo, numero_conta):
        super().__init__(agencia, saldo, numero_conta)

    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Seu saldo é de {self.saldo}R$ logo você não pode sacar {valor}')
            return None
        self.saldo -= valor
        print(f'Seu novo saldo é de {self.saldo}R$')

    def depositar(self, valor):
        print(f'Você de depositou {valor}R$')
        self.saldo += valor
        print(f'Seu novo saldo é de {self.saldo}')

    def infos(self):
        print(f'Saldo: {self.saldo}; Agencia: {self.agencia}')
