#CÁLCULO DA MÉDIA ESCOLAR

from time import sleep

print("Aqui você poderá calcular se você foi aprovado(a) ou não com base na média da sua escola.")

while True:
    media_escola = input("Digite a média da sua escola (Exemplo -> 6): ")

    if media_escola.isdigit(): 

        nota1 = input("Digite a sua nota da primeira unidade (Exemplo -> 6.5): ")
        nota2 = input("Digite a sua nota da segunda unidade: ")
        nota3 = input("Digite a sua nota da terceira unidade: ")

        print("Processando...")
        sleep(1)

        try: 

            media = (float(nota1) + float(nota2) + float(nota3)) / 3

            if media >= int(media_escola):
                print(f"A sua média é {media:.1f} e você foi aprovado(a). Parabéns!")
                break
            else:
                print(f"A sua média é {media:.1f} e infelizmente você não foi aprovado(a).")
                break    
                    
        except:
            print("Tente novamente e digite somente notas válidas.")
            
    else:
        print("INSIRA UMA MÉDIA VÁLIDA")           
    
    

      
           

