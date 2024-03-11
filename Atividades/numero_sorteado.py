# SORTEIO DE NÚMERO

from random import randrange

print("O número sorteado estará dentro dos números que você inserir")

valor1 = input("Digite aqui o primeiro número (Exemplo -> 1): ")
valor2 = input("Digite aqui o segundo número: ")

if valor1.isdigit() and valor2.isdigit():
    print(f"O número sorteado foi: {randrange(int(valor1), int(valor2))}")
else:
    print("Insira somente números inteiros válidos")    