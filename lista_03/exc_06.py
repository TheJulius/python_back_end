def lista_positivo():
    lista_de_positivo = [10, 22, 37, 39, 50, 400]

    numero_par_entre_10_e_50 = [numero_positivo for numero_positivo in lista_de_positivo if 10 <= numero_positivo <= 50
                                and numero_positivo % 2 == 0]
    lista_positivo = print(numero_par_entre_10_e_50)

    return lista_positivo

lista_positivo()