import adivinhacao
import forca

def escolher_jogo():
    print("********************************")
    print("********Escolha seu Jogo********")
    print("********************************")

    print("(1)Forca (2)Adivinhacao")

    jogo = int(input("Qual jogo gostaria?"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()