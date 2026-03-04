import os

os.system ("cls || clear")
matricula = input("Digite a sua Matricula: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_de_trabalho  = int(input("Digite o tempo de trabalho em anos: "))

idade = 2026 - ano_nascimento

if idade >= 65 or tempo_de_trabalho >= 30:
    resultado = "Aposentadoria"
else:
    resultado = "Não requerer aposentadoria"
    
print(f"Idade: {idade}")
print(f"Tempo de Trabalho: {tempo_de_trabalho}")
