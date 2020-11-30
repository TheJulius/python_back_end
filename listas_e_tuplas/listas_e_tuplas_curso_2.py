curso_data_science = [15, 23, 43, 56]
curso_machine_learning = [13, 23, 56, 42]

enviar_email = curso_data_science.copy()
enviar_email.extend(curso_machine_learning)

print(sorted(set(enviar_email)))

print(set([1, 2, 3, 1])) #o Set ignora duplicacoes de valores!!

criando_um_set = {1, 2, 3, 4, 1} #outra forma de criar um set!! usando COLCHETES!
print(criando_um_set)            # SET NAO TEM INDEX, a posicao e aleatoria!!

curso_machine_learning | curso_data_science #em conjuntos, isso e um OU (PIPE)

curso_machine_learning & curso_data_science #em conjuntos, isso e um E (E comercial),
                                            #ou seja, nesse caso, fez ambos os cursos.

curso_machine_learning - curso_data_science #em conjuntos, o MENOS deixa somente
                                            #os numeros que estao exclusivamente em 1 conjunto

curso_machine_learning ^ curso_data_science #em conjuntos, o CHAPEUZINHO, mais conhecido como
                                            #ou exclusivo, deixa somente os numeros exclusivos
                                            #de cada grupo

criando_um_set.add(654654) #em conjunto se usa ADD ao inves de APPEND, pois um conjunto nao tem
                           # um fim definido

frozenset(criando_um_set) #voce congela o conjunto! Que loucura!

frase = "Ola meu nome e Julio e meu pai e jose e meu avo e jose"
frase.split()
set(frase)