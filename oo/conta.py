##para importar a classe em outro arquivo e necessario  usar:
##from nome_do_arquivo(onde a classe esta localizado) import nome_da_classe
##nesse exemplo: from conta import Conta
##repare que o nome do arquivo.py e conta.py, por isso o primeiro "conta" e minusculo

##para iniciar o objeto usa-se: nome_do_objeto = NomeDaClasse
##nesse exemplo: conta_do_julio = Conta(1234, julio, 100.0, 1000.0)

class Conta:
    def __init__(self, numero_da_conta, titular, saldo, limite):
        print("Contruindo o objeto... {}".format(self))
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Ola {}, seu saldo e de R${}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        saldo_e_limite = self.__saldo + self.__limite
        return valor_a_sacar > saldo_e_limite

    def saca(self, valor_a_sacar):
        if(self.__pode_sacar(valor_a_sacar)):
            print("Saldo Insuficiente")
        else:
            self.__saldo -= valor_a_sacar
            return "Saldo Atual: {}".format(self.__saldo)

    def transfere(self, valor, destino):
        self.saca(valor)
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
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite