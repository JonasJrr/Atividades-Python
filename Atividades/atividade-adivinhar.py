#NÚMERO SECRETO

import random

print("Um número secreto será sorteado entre 1 e 10. Você consegue adivinhar qual é?")

palpite = input("Digite aqui o seu palpite: ")

numero_secreto = random.randrange(1,11)

if palpite.isdigit():
    if int(palpite) == numero_secreto:
        print("O número secreto era {}. Parabéns, você acertou!".format(numero_secreto))
    else:
        print("O número secreto era {}. Tente novamente.".format(numero_secreto))
else:
    print("Insira um número válido.")        


    
               