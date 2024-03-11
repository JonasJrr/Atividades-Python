# ANALISADOR DE NOMES

from time import sleep

nome = input("Digite o seu nome completo: ")
nome_sem_space = nome.strip().replace(" ", "")

if len(nome_sem_space) > 0:
    nome_separado = nome.split()
    print("Analisando o seu nome...")
    sleep(1)

    print(f"A letra 'A' se repete {nome.lower().count('a')} vezes")
    print(f"Seu nome em maiúsculas é: {nome.strip().upper()}")
    print(f"Seu nome em minúsculas é: {nome.strip().lower()}")
    print(f"Seu nome tem ao todo {len(nome_sem_space)} letras")
    print(f"Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras")
    print(f"Seu último nome é {nome_separado[-1]} e ele tem {len(nome_separado[-1])} letras")
else:
    print("Tente novamente e digite um nome válido")