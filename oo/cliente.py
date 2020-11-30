class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("usando o getter do python")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("usando o setter do python")
        self.nome = nome

