import array as ar #EVITE!! #os arrays do python so podem ser de 1 tipo por array, nao pode misturar
import numpy as np #Use mais o numpy para Data Science e numeros em geral

#o primeiro parametro informa o tipo de array desejado
teste_array = ar.array("d", [1, 3.5]) # "d" porque e double
print(teste_array)

teste_numpy = np.array([1, 3.5])
print(teste_numpy)
