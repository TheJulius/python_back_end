import random

def jogar():

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("********************************")
    print("Bem Vindo no jogo de Adivinhacao")
    print("********************************")
    print("Qual o nivel de dificuldade desejado?")
    print("(1)Facil (2)Medio (3)Dificil")

    nivel = int(input("Define o Nivel de Dificuldade"))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)
        print("Voce Digitou: ", chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Voce Acertou")
            print("Voce fez {} pontos!".format(pontos))
        else:
            if(maior):
                print("Voce errou e seu chute foi maior do que o numero secreto")
                break

            elif(menor):
                print("Voce errou e seu chute foi menor do que o numero secreto")
                numeros_perdidos = abs(numero_secreto - chute)
                pontos = pontos - numeros_perdidos

        print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar()