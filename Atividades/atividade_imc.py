#CÁLCULO DE IMC

from time import sleep

try:
    peso = float(input("Digite o seu peso em KG (exemplo: 60.5): "))
    altura = float(input("Digite a sua altura em metros (exemplo: 1.70): "))

    imc = peso / (altura ** 2)
    
    print("Processando...")
    sleep(1)

    if imc > 35:
        print(f"O seu IMC é {imc:.2f} e você está com obesidade extrema")
    elif imc >= 30 and imc <= 35:
        print(f"O seu IMC é {imc:.2f} e você está com obesidade")  
    elif imc >= 25 and imc < 30:
        print(f"O seu IMC é {imc:.2f} e você está com excesso de peso")
    elif imc >= 18.5 and imc < 25:
        print(f"O seu IMC é {imc:.2f} e você está com o peso normal")
    else:
        print(f"O seu IMC é {imc:.2f} e você está abaixo do peso")  

except ValueError:
    print("Tente novamente e insira um valor numérico nas opções.")             


    
