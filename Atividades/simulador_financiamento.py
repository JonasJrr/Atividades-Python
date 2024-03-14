# SIMULANDO O FINANCIAMENTO DE UMA CASA

from time import sleep

while True:
    valor_casa = input("Valor da casa (exemplo -> 50000): R$")
    salario = input("Salário do comprador (exemplo -> 1000): R$")
    tempo_financiamento = input("Gostaria de financiar em quantos anos (exemplo -> 10): ")

    if valor_casa.isnumeric() and salario.isnumeric() and tempo_financiamento.isnumeric():
        prestacao = float(valor_casa) / (12 * int(tempo_financiamento))

        print("Calculando...")
        sleep(1)

        if prestacao <= (float(salario) / 2.5):
            print(f"Para pagar uma casa de R${valor_casa} em {tempo_financiamento} anos a prestação será no valor de R${prestacao:.2f}\nO financiamento PODE ser realizado!")
            break
        else:
            print(f"Para pagar uma casa de R${valor_casa} em {tempo_financiamento} anos a prestação será no valor de R${prestacao:.2f}\nO financiamento NÃO PODE ser concedido pois o valor representa uma porcentagem muito grande do seu salário")
            break
    else:
        print("Algo deu errado. Tente novamente e insira os valores corretos sem pontos, vírgulas ou caracteres especiais\n")