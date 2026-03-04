import os

os.system("cls")

print("- solicitando dados-")
media = int(input("Insira sua média:"))
faltas = int(input("Insira suas faltas:"))

aprovado_por_media = media >= 7
aprovado_por_frequencias= faltas <40

if aprovado_por_media and aprovado_por_frequencias:
    print("Aprovado!")
else:
    print("Reprovado.")   