from extrator_argumentos_url import extrator_argumentos_url

'''
nome = "julio"
sub_nome = nome[3]
sub_nome2 = nome[3:5] #da posicao 3 ate a posicao 4, pois o ultimo numero e exclusivo

print(sub_nome)

##########################################################################################################

argumento = "www.bytebank.com/cambio?moedaorigem=real"

index = argumento.find("=") #o find retorna o indice(o numero da posicao) do que esta entre parenteses
substring = argumento[index + 1:]
print(substring)

##########################################################################################################


argumento2 = "moedaorigem=real"
lista_argumentos = argumento2.split("=") #toda vez que encontrar um sinal de = (igual), divida a string
print(lista_argumentos)

##########################################################################################################

'''

url_1 = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
url_2 = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=500"

argumento = extrator_argumentos_url(url_1)
argumento_2 = extrator_argumentos_url(url_2)

print(id(argumento))
print(id(argumento_2))
print(argumento == argumento_2)

############################################################################################################

moeda_origem, moeda_destino = argumento.extrai_argumentos()
valor = argumento.extrai_valor()

print(moeda_origem, moeda_destino, valor)
