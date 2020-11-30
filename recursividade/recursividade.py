class fatorial:

    def __init__(self, base):
        self.__base = base


    def recursivo(self):
        self.retorna_base = self.__base == 0 or self.__base == 1
        self.retorna_recursivo = print(self.__base * self.recursivo(self.base - 1))

        if self.retorna_base:
            return 1
        else:
            return self.retorna_recursivo









