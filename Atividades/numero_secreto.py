#NÚMERO SECRETO

from random import randrange

print("Um número secreto será sorteado entre 1 e 20. Você consegue adivinhar qual é?")

while True:
    palpite = input("Digite aqui o seu palpite (Exemplo -> 3): ")

    numero_secreto = randrange(1,21)

    if palpite.isdigit():
        if int(palpite) == numero_secreto:
            print("O número secreto era {}. Parabéns, você acertou!".format(numero_secreto))
            break
        else:
            print("O número secreto era {}. Tente novamente.".format(numero_secreto))
    else:
        print("INSIRA UM NÚMERO VÁLIDO")        


    
               