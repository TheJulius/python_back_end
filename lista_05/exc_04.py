def verifica_lista(numero, lista):
    if numero in lista:
        return True
    else:
        return False

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
verifica_lista(2, lista)