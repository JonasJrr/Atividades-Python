#CÁLCULO DA MÉDIA ESCOLAR

print("Aqui você poderá calcular com base na média da sua escola se você ira ser aprovado(a) ou não.")

media_escola = input("Digite a média da sua escola: ")

if media_escola.isdigit(): 

    nota1 = input("Digite qual a sua nota da primeira unidade: ")
    nota2 = input("Digite qual a sua nota da segunda unidade: ")
    nota3 = input("Digite qual a sua nota da terceira unidade: ")

    if nota1.isdigit() and nota2.isdigit() and nota3.isdigit(): 

        media = (float(nota1) + float(nota2) + float(nota3)) / 3

        if media >= int(media_escola):
            print("A sua média é {} e você foi aprovado(a)!".format(round(media, 2)))
        else:
            print("A sua média é {} e infelizmente você não foi aprovado(a).".format(round(media, 2)))    
                
    else:
        print("Tente novamente e digite uma nota válida.")
        
else:
    print("Insira uma média válida.")           
    
    

      
           

