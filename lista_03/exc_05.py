def combo_de_lista():
    lista_1 = [1, 2, 3, 10]
    lista_2 = [1, 2, 3, 10]
    lista_3 = zip(lista_1, lista_2)

    lista = [lista_1*lista_2 for lista_1, lista_2 in lista_3 if lista_1*lista_2 > 40]
    combo_de_lista = print(lista)

    return combo_de_lista

combo_de_lista()
