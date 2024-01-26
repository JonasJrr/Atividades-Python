#PALAVRAS SECRETAS

from random import randint

lista_palavras = ["programador", "python", "sistema", "computador"] # LISTA DE PALAVRAS QUE SERÃO SORTEADAS
palavra_secreta = lista_palavras[randint(0, ( len(lista_palavras) - 1 ))]
letras_acertadas = ""
tentativas = 0

print("JOGO DA PALAVRA SECRETA")

while True:
    letra_digitada = input("Digite uma letra: ")

    if letra_digitada and letra_digitada.isalpha():

        if len(letra_digitada) > 1:
            print("Digite apenas uma letra.")
        else:
            if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada

            palavra_formada = ""    
            
            for i in palavra_secreta:
                if i in letras_acertadas:
                    palavra_formada += i
                else:
                    palavra_formada += "*"

            tentativas += 1        

            print(palavra_formada)

            if tentativas == 20: # QUANTIDADE MÁXIMA DE TENTATIVAS PERMITADAS
                print("Você excedeu o número máximo de tentativas. Tente novamente!")
                break        

            if palavra_formada == palavra_secreta:
                print(f"Parabéns! A palavra secreta era {palavra_secreta}. Você acertou com {tentativas} tentativas!")
                break

    else:
        print("Você precisa digitar uma letra")