#TABUADA
from time import sleep

while True:
    entrada = input("Digite aqui o número que você deseja visualizar a tabuada (Exemplo -> 5): ")

    if entrada.isdigit():
        print("Processando...")
        sleep(1)
        
        for numero in range(1,11):
            print(int(entrada), "x", numero, ":", int(entrada) * numero)
        break    
    else:
        print("INSIRA UM NÚMERO VÁLIDO")        
       
    



   