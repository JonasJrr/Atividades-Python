#TABUADA

entrada = input("Digite aqui o número que você deseja visualizar a tabuada: ")

if entrada.isdigit():
    for numero in range(1,11):
        print(int(entrada), "x", numero, ":", int(entrada) * numero)
else:
    print("Insira um número válido.")        
       
    



   