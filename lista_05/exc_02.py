import numpy as np

def lista_multiplicada(lista):
    lista_multiplicada = np.prod(lista)
    return lista_multiplicada

lista = [1,2,3,5]
lista_multiplicada(lista)