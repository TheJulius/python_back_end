idades = [10,22,85,79,46]
idades.extend([30,23]) # voce passa uma outra lista para adicionar na lista original
print(idades)

for i in range(len(idades)): #for que percorre a lista idades e printa a posicao do elemento e o elemento em si
    print(i, idades[i])


print(list(enumerate(idades))) #fazendo a mesma coisa so que em 1 linha

for indice, idade in enumerate(idades): #fazendo a mesma coisa, porem na medida do necessario e desempacotando os elementos
    print(indice, idade)

#######################################################################################

usuarios = [
    ("Julio", 22, 1997)
    ("Eva", 20, 1999)
    ("Nicole", 21, 1998)
]

for nome, idade, nascimento in usuarios: #percorre uma tupla com 3 elementos e imprime somente 1 dos 3 elementos
    print(nome)

for nome, _, _ in usuarios: #ao utlizar o underline, o for ignora os outros elementos da tupla
    print(nome)
#######################################################################################

numeros = [10,22,85,79,46]
numeros_novos = []

for numero in numeros: ##for que percorre a lista numeros
    numeros_novos.append(numero + 1) #usa-se o append na lista nova para adicionar os elementos no final dela
    print(numeros_novos)

########################################################################################
##faz o mesmo o que o for anterior, porem com uma condicao e reduzido em 1 linha

outros_numeros = [101,222,853,791,461]
outros_numeros_novos = [outros_numeros_mesmo + 1 for outros_numeros_mesmo in outros_numeros if outros_numeros_mesmo > 200]
print(outros_numeros_novos)

########################################################################################
########################################################################################



