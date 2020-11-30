def insere():

    elemento = 10
    lista = [1, 2, 3, 4, 5, 11]

    if elemento not in lista:
        lista.append(elemento)

    return print(lista)

insere()