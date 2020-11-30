#Em python, str, list e tuple, tem as mesmas funcoes. (tirando as de alterar qqr coisa da tuple, pq tuple e imutavel)

pessoa_1 = ("Julio", 23) #tuples se iniciam com parenteses e sao listas imutaveis, pode misturar diferentes tipos de variaveis
pessoa_2 = ("Rogerinho da Van", 34)

pet_1 = ["ozob", 2] #listas se iniciam com colchetes e sao mutaveis!, pode misturar diferentes tipos de variaveis
pet_2 = ["coronga", 4]

print(pessoa_1[1]) #mostrando elemento na posicao 1 da tuple
print(pet_1[0]) #mostrando elemento na posicao 0 da lista

print(pessoa_1.count("Julio")) #conta quantas vezes tem a palavra "Julio" na tuple
print(pet_1.count("coronga")) #conta quantas vezes tem a palavra "coronga" na list

pet_2.insert(0,"Sousa") #insere um elemento, primeiro numero e o index, o segundo e o que voce quer inserir
pet_2.pop(0)
pet_2.insert(3,"calmo")
print(pet_2)

print(len(pessoa_2)) #mostra a quantidade de elementos da tuple

grupo_de_pessoas = [pessoa_1, pessoa_2] #inserindo uma tuple dentro de uma list
print(grupo_de_pessoas)

grupo_de_pets = (pet_1, pet_2) #inserindo uma list dentro de uma tuple
print(grupo_de_pets)

grupo_de_pessoas_2 = tuple(grupo_de_pessoas) #convertendo list em tuple

grupo_de_pets_2 = list(grupo_de_pets) #convertendo tuple em list

print(grupo_de_pessoas_2[0][1]) #mostrando o elemento da posicao 1 do elemento 0, que e uma list


################ DICIONARIO ####################

## O dicionario e uma lista que liga uma palavra com a outra
## Por exemplo, se voce atribuir a palavra celular com apple
## Ao buscar na lista a palavra celular, voce encontra apple
## sem a necessidade de saber em que posicao a palavra celular
## em relacao a lista

exemplo_dicionario = {"celular" : "apple"}
print(exemplo_dicionario["celular"])