'''
class conta_corrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def deposita_para_todos(contas):
        for conta in contas:
            conta.deposita(100)

    def __str__(self):
        return "Codigo: {} Saldo: {}".format(self.codigo, self.saldo)

conta_do_julio = conta_corrente(10)
conta_do_julio.deposita(500)

conta_da_julia = conta_corrente(11)
conta_da_julia.deposita(1000)

contas = [conta_do_julio, conta_da_julia]
for conta in contas:
    print(conta)

conta_da_julia.deposita_para_todos(contas)
print(contas)
'''
from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

class conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo: {} Saldo: {}".format(self._codigo, self._saldo)

    @abstractmethod
    def passa_mes(self):
        pass


class conta_corrente(conta):

    def passa_mes(self):
        self._saldo -= 2


class conta_poupanca(conta):

    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class conta_investimento:
    pass


conta_do_julio = conta_corrente(22)
conta_do_julio.deposita(1000)
conta_do_julio.passa_mes()
print(conta_do_julio)

conta_da_julia = conta_poupanca(23)
conta_da_julia.deposita(1000)
conta_da_julia.passa_mes()
print(conta_da_julia)

contas = [conta_do_julio, conta_da_julia]

for conta in contas:
    conta.passa_mes()
    print(conta)

#######################################################################################################
#######################################################################################################

##Igualdade e __eq__
@total_ordering
class conta_salario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __lt__(self, other):          # o __lt__ serve para criar uma forma de ordenar objetos de uma classe
        if self._saldo < other._saldo:# voce escolhe um atributo e diz o que e menor que o outro e da um return
            return self._saldo  < other._saldo
        return self._codigo < other._codigo


    def __eq__(self, other):              # o __eq__ serve para voce criar as suas proprias condicoes de igualdade
                                          # dessa forma evitando erros de comparacao muito comuns!
        if type (other) != conta_salario: #comparando se o outro que esta sendo comparado e do mesmo tipo ou nao
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo #comparando se todos os atribuitos tem
                                                                             #o mesmo valor

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Codigo: {} Saldo: {}".format(self._codigo, self._saldo)

    def ordena_por_saldo(self): #ordenando um objeto por um atribuito especifico da lista
        for conta in contas:
            print(conta)

class conta_multiplo_salario(conta_salario): #a classe tambem herda o __eq__ da conta_salario
    pass


conta_1 = conta_salario(22)
conta_2 = conta_multiplo_salario(22)
conta_1 == conta_2
