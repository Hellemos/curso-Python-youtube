class Conta(Banco):
    def __init__(self, saldo, ID, senha):
        super(Banco, self).__init__()
        self.__saldo = saldo
        self.ID = ID
        self.senha = senha

    def deposito(self, senha, valor):
        self.__saldo += valor
        self.saldo()
    def saque(self, senha, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        self.saldo()
    def podeReceberEmprestimo(self, valor):
        pass
    def saldo(self):
        print('Seu saldo atual eh: %.2f' % self.__saldo)
