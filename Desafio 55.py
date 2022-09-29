#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

peso = float(input('Digite o 1º peso: '))
maior = peso
menor = peso

for c in range(0, 4):
    peso = float(input('Digite mais um: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'\nMaior peso: {maior}\nMenor peso: {menor}')