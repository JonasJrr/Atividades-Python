#CÁLCULO DE IMC

peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)
   
if imc > 35:
    print("O seu IMC é:", round(imc, 2), "e você está com obesidade extrema")
elif imc >= 30 and imc <= 35:
    print("O seu IMC é:", round(imc, 2), "e você está com obesidade")   
elif imc >= 25 and imc < 30:
    print("O seu IMC é:", round(imc, 2), "e você está com excesso de peso")
elif imc >= 18.5 and imc < 25:
    print("O seu IMC é:", round(imc, 2), "e você está com o peso normal")
else:
    print("O seu IMC é:", round(imc, 2), "e você está abaixo do peso")       


    
