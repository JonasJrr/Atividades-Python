#CONTADOR DE LETRAS, CONSOANTES E VOGAIS

from time import sleep

print("Descubra quantas letras, vogais e consoantes uma frase ou palavra possui.")

entrada_com_espacamento = input("Digite aqui a frase ou palavra que você deseja verificar: ")

vogais = "aáãeéiíoóõuú"

count_vogais = 0 #Contador de vogais
count_consoantes = 0 #Contador de consoantes

entrada = entrada_com_espacamento.replace(" ", "").lower() #Tratando os espaçamentos do input e letras maiúsculas

for i in entrada:
    if i in vogais:
        count_vogais += 1
    else:
        count_consoantes += 1

print("Processando...")
sleep(1)

print(f"Quantidade de vogais: {count_vogais}\nQuantidade de consoantes: {count_consoantes}\nQuantidade de letras: {len(entrada)}")
