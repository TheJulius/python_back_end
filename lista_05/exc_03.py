def numeros_impares(lista):

    for numero in lista:
        if numero % 2 != 0:
            print(numero)
        else:
            False
            break
            print(numero)

    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_impares(lista)