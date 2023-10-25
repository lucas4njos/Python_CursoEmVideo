# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista = []
dicionario = {}
continuar = 0
media = 0

while True:
    dicionario["Nome"] = str(input("Digite o nome: "))
    dicionario["Sexo"] = str(input("Digite o Sexo:"))
    dicionario["Idade"] = int(input("Digite a idade:"))

    media += dicionario["Idade"]

    lista.append(dicionario.copy())

    continuar = int(input("Deseja continuar? "))
    if continuar == 0:
        break

print("-_" * 50)

print(lista)

print("-_" * 50)

media = media / len(lista)

print(f"Pessoas cadastradas: {len(lista)}")
print(f"Média de idade: {media}")

print("\nMulheres:")
for i in lista:
    if i["Sexo"] == "F":
        print(i["Nome"])

print("\nAcima da media:")
for i in lista:
    if i["Idade"] > media:
        print(i["Nome"])