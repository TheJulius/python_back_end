class Data():
    def __init__(self,dia,mes,ano):
        if (self.dia > 31 and self.mes > 12 and self.ano > 2999):
            print("Data Invalida")
        else:
            self.dia = dia
            self.mes = mes
            self.ano = ano

    def faz_data(self):
            print("{}/{}/{}/".format(self.dia, self.mes, self.ano))