#SORTEIO DE NÚMERO

import random

print("O número sorteado estará dentro dos números que você inserir.")

valor1 = input("Digite aqui o primeiro número: ")
valor2 = input("Digite aqui o segundo número: ")

if valor1.isdigit() and valor2.isdigit():
    print("O número sorteado foi: ", random.randrange(int(valor1), int(valor2)))
else:
    print("Insira um número válido.")    