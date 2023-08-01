#CONTADOR DE LETRAS, CONSOANTES E VOGAIS

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

print("Quantidade de vogais: {0}. Quantidade de consoantes: {1}. Quantidade de letras: {2}.".format(count_vogais, count_consoantes, len(entrada)))
