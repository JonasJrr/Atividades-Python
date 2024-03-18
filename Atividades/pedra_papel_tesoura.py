# PEDRA, PAPEL E TESOURA

from time import sleep
from random import randint

options = ["PEDRA", "PAPEL", "TESOURA"]

pontos_jogador = pontos_computador = 0

while True:

    print("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n[ 3 ] PARA SAIR")

    jogada = input("Qual é a sua opção? ")

    jogada_computador = options[randint(0,2)]

    if jogada.isdigit():

        jogada = int(jogada)

        if jogada in range(3):
            sleep(1)

            print(f"O computador jogou {jogada_computador} e você jogou {options[jogada]}")

            if options[jogada] == "PEDRA":
                if jogada_computador == "TESOURA":
                    pontos_jogador += 1
                    print("VOCÊ GANHOU!")
                elif jogada_computador == "PAPEL":
                    pontos_computador += 1
                    print("VOCÊ PERDEU!")
                else:
                    print("DEU EMPATE!\n")
            elif options[jogada] == "PAPEL":
                if jogada_computador == "PEDRA":
                    pontos_jogador += 1
                    print("VOCÊ GANHOU!")
                elif jogada_computador == "TESOURA":
                    pontos_computador += 1
                    print("VOCÊ PERDEU!")
                else:
                    print("DEU EMPATE!\n")
            elif options[jogada] == "TESOURA":
                if jogada_computador == "PAPEL":
                    pontos_jogador += 1
                    print("VOCÊ GANHOU!")
                elif jogada_computador == "PEDRA":
                    pontos_computador += 1
                    print("VOCÊ PERDEU!")
                else:
                    print("DEU EMPATE!\n")

            print(f"Sua pontuação: {pontos_jogador} | Pontuação do computador: {pontos_computador}\n")
            
        elif jogada == 3:
            print("Finalizando...")
            sleep(1)
            break
        else:
            print("Tente novamente e insira uma das opções listadas")
    else:
        print("Tente novamente e digite somente números")
