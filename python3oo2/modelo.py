class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property  # metodo get
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property  # metodo get
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):  # metodo de imprimir
        return f"{self.nome} - {self.ano} - {self.likes} Likes"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min- {self.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self.programas)

    @property
    def listagem(self):
        return self._programas

from modelo import Filme, Serie

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores1 = Filme("vingadores1 - guerra infinita", 2017, 100)
vingadores2 = Filme("vingadores2 - guerra infinita", 2016, 120)

atlanta = Serie("atlanta", 2018, 1)
atlanta1 = Serie("atlanta1", 2019, 2)
atlanta2 = Serie("atlanta2", 2012, 3)

vingadores.dar_likes()
vingadores1.dar_likes()
vingadores1.dar_likes()
vingadores1.dar_likes()
vingadores2.dar_likes()

atlanta.dar_likes()
atlanta1.dar_likes()
atlanta2.dar_likes()
atlanta2.dar_likes()

filmes_e_series = [vingadores, vingadores1, vingadores2, atlanta, atlanta1, atlanta2]

playlist_fim_de_semana = Playlist("fim_de_semana",
                                  filmes_e_series)  ##Criando Objeto da classe PLAYLIST que tem todas as funcoes da classe e talz

print(f"Tamanho da Playlist {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)
