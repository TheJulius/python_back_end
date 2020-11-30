def retira_negativo(lista):
    nova_lista = []
    for numero in lista:
        if numero > 0:
            nova_lista.append(numero)
            print(nova_lista)

    return nova_lista

lista = [1, -2, 2, -25, 3, -89, 4, 5, -798, 6, 7, 8, 9]
retira_negativo(lista)