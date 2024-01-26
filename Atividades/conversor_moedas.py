#CONVERSOR DE MOEDAS

print("Aqui você pode converter o valor do REAL para DÓLAR ou vice-versa.")

taxa_cambio = 4.88 #COTA DO DIA 09/01/2024

try:
    option = int(input("Digite 1 para converter de real para dólar ou 2 para converter de dólar para real: "))

    if option == 1:
        entrada = input("Insira aqui o valor em REAL para converter para DÓLAR: ")
        moeda = float(entrada) / taxa_cambio
        print(f"{entrada} Reais equivale a {moeda:.2f} Dolares") 
    elif option == 2:
        entrada = input("Insira aqui o valor em DÓLAR para converter para REAL: ")
        moeda = float(entrada) * taxa_cambio
        print(f"{entrada} Dolares equivale a {moeda:.2f} Reais")
    else:
        print("Tente novamente e insira uma opção válida.")
except ValueError:
    print("Insira um valor numérico para a opção ou a quantia a ser convertida.")                