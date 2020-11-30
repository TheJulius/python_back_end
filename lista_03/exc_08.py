def maior_que_x(numero):
    lista = [-2, 2, -3, 3, -4, 4]

    lista_maior_que_x = [numero_positivo for numero_positivo in lista if numero_positivo >= numero]
    mensagem = print(lista_maior_que_x)

    return mensagem

maior_que_x(3)