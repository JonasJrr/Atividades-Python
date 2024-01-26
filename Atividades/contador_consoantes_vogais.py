#CONTADOR DE LETRAS, CONSOANTES E VOGAIS

from time import sleep

print("Descubra quantas letras, vogais e consoantes uma frase/palavra possui")

vogais = "aáãàeéèiìíoòóõuùú"
contador_vogais = contador_consoantes = 0 

while True:
    entrada_usuario = input("Digite aqui a frase ou palavra que você deseja verificar: ")

    entrada_formatada = entrada_usuario.replace(" ", "").strip().lower()

    if entrada_formatada.isalpha():

        for letra in entrada_formatada:
            if letra in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1

        print("Processando...")
        sleep(1)

        print(f"Quantidade de vogais: {contador_vogais}\nQuantidade de consoantes: {contador_consoantes}\nQuantidade de letras: {len(entrada_formatada)}")
        break

    else:
        print("TENTE NOVAMENTE E INSIRA UMA FRASE/PALAVRA VÁLIDA")
