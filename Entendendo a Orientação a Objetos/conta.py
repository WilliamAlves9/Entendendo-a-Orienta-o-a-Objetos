class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, __valor_a_sacar):
        __valor_disponivel_saque = self.__saldo + self.__limite
        return __valor_a_sacar <= __valor_disponivel_saque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(" O valor {} passou o limite".format(valor))

    def tranferir(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigos_bancos():
        return {'BB':"001", 'Caixa':"104", 'Bradesco':"237"}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
