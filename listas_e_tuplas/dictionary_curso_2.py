from collections import defaultdict
from collections import Counter
frase = "Ola meu nome e Julio e meu pai e jose e meu avo e jose"

aparicoes = {"julio": 1,
             "jose": 2,
             "meu": 3} #assim se faz um dicionario

dict(julio = 1, jose = 2, meu = 3) #outra forma de fazer um dicionario

aparicoes["carlos"] = 1 #adicionando o elemento carlos
del aparicoes["carlos"] #deletando o carlos do dicionario

for elemento in aparicoes.keys(): #imprimindo o nome
    print(elemento)

for elemento in aparicoes.values(): #imprimindo os valores
    print(elemento)

for chave, valor in aparicoes.items(): #imprimindo ambos
    print(chave, valor)

#######################################################################################
#contador de palavras em uma frase com defaultdict
#######################################################################################
frase_2 = "Ola meu nome e Julio e meu pai e jose e meu avo e jose"
frase_2 = frase_2.lower()

aparicoes_2 = defaultdict(int)

for palavra  in frase_2.split():
    aparicoes_2[palavra] += 1

print(aparicoes_2)

#######################################################################################
#contador de palavras em uma frase com COUNTER(muito melhor)
#######################################################################################
frase_3 = "Ola meu nome e Julio e meu pai e jose e meu avo e jose"
frase_3 = frase_3.lower()

aparicoes_3 = Counter(frase_3.split())
print(aparicoes_3)





