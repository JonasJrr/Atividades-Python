#CONVERSOR DE MOEDAS

print("Aqui você pode converter o valor do real para dólar ou vice-versa.")

option = input("Digite 1 para converter de real para dólar ou 2 para converter de dólar para real: ")

if int(option) == 1:
    entrada = input("Insira aqui o valor em real para converter para dólar: ")
    moeda = float(entrada) / 4.75
    print(entrada, "Reais equivale a", round(moeda, 2),"dolares") #COTA DO DIA 27/07/2023
elif int(option) == 2:
    entrada = input("Insira aqui o valor em dólar para converter para real: ")
    moeda = float(entrada) * 4.75
    print(entrada, "Dolares equivale a", round(moeda, 2), "reais") #COTA DO DIA 27/07/2023
else:
    print("Insira um valor válido.")        