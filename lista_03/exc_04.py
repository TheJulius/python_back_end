def lista_positivo():
    lista_de_positivo = [-2, 2, -3, 3, -4, 4]

    numero_positivo = [numero_positivo for numero_positivo in lista_de_positivo if numero_positivo > 0]
    lista_positivo = print(numero_positivo)

    return lista_positivo

lista_positivo()

