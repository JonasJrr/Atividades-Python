# CÁLCULO DE DESCONTOS

while True:
    try:
        valor = input("Qual é o preço do produto? R$")
        desconto = input("Qual é o desconto? (ex -> 10): ")

        valor_formatado = float(valor)
        desconto_formatado = int(desconto)
        
        if valor_formatado <= 0 or desconto_formatado <= 0 or desconto_formatado > 100:
            raise ValueError
        
        valor_com_desconto = valor_formatado - valor_formatado * (desconto_formatado/100) 
        break
    except ValueError:
        print(f"Digite um valor e um desconto válido. *Obs: O desconto precisa estar entre 0 e 100")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
        exit()
    except Exception:
        print(f"Ocorreu um erro: {Exception}")

print(f"O produto que custa R${valor_formatado:.2f}, na promoção com {desconto_formatado}% de desconto vai custar R${valor_com_desconto:.2f}")
