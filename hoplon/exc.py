class lista_de_nomes_por_ano:

    def __init__(self, ano): #Inicializador dos Atributos
        self._ano = ano
        self._nomes = []

    def __str__(self): #Um "String Builder"
        return "Ano: {} Lista de Nomes: {}".format(self._ano, self._nomes)

    def organiza_lista_nomes(self): #Metodo que organiza os nomes em ordem crescente
        self._nomes = sorted(self._nomes)

    def adiciona_nomes(self, novo_nome): #Metodo que adiciona nomes
        if novo_nome in self._nomes: #verificicacao e substituicao do nome adicionado e reordena a lista
            self._nomes.append(novo_nome)
            self._nomes.remove(novo_nome)
        else:
            self._nomes.append(novo_nome)
        self.organiza_lista_nomes()

    def deleta_nomes(self, deleta_nome): #Metodo que deleta os nomes e reordena a lista automaticamente
        for nomes in self._nomes:
            if deleta_nome == nomes:
                self._nomes.remove(deleta_nome)
        self.organiza_lista_nomes()

    def deleta_all(self, confirmacao): #Metodo que deleta todos os elementos da lista e setta o ano como Null
        if confirmacao == "s".lower():
            self._nomes.clear()
            self._ano = None
            return True
        else:
            return False
            raise ValueError

    def search_nomes(self, inicio, fim): #Metodo que faz a busca
        if inicio < 0: #validacao do atributo "inicio"
            inicio = 0
        if fim < 0: #validacao do atributo "fim"
            fim = len(self._nomes) - abs(fim) + 1
        elif fim > len(self._nomes):
            fim = len(self._nomes)
        for nome in range(inicio, fim):
            print(self._nomes[nome])

    def retorna_indice(self, nome): #Metodo que retorna a posicao e o nome da pessoa
        for index in range(len(self._nomes)):
            if nome == self._nomes[index]:
                print("Posicao: {} Nome: {}".format(index, self._nomes[index]))



#inicio dos testes unitarios

ano_2 = lista_de_nomes_por_ano(1983)
ano_2.adiciona_nomes("alberto")
ano_2.adiciona_nomes("claudio")
ano_2.adiciona_nomes("joao")
ano_2.adiciona_nomes("joao")
ano_2.adiciona_nomes("joao")
ano_2.adiciona_nomes("zenon")

print(ano_2)

ano_2.search_nomes(0, -1)
ano_2.search_nomes(-1, -2)

ano_2.retorna_indice("alberto")

ano_2.deleta_all("s")
print(ano_2)

cidades_sc = lista_de_nomes_por_ano(2000)
cidades_sc.adiciona_nomes("florianopolis")
cidades_sc.adiciona_nomes("balneario camboriu")
cidades_sc.adiciona_nomes("blumenau")
cidades_sc.adiciona_nomes("blumenau")
cidades_sc.adiciona_nomes("blumenau")
cidades_sc.adiciona_nomes("joinville")

print(cidades_sc)

cidades_sc.search_nomes(0, -2)
cidades_sc.search_nomes(-1, -3)

cidades_sc.retorna_indice("florianopolis")

cidades_sc.deleta_all("s")
print(cidades_sc)

