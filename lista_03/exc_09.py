def lista_primos(inicio_intervalo, final_intervalo):
    lista_de_positivo = [10, 22, 37, 39, 50, 400]

    lista_primos = [numero for numero in lista_de_positivo if inicio_intervalo <= numero <= final_intervalo
                                and numero % 2]
    lista = print(lista_primos)

    return lista

lista_primos(10,50)
