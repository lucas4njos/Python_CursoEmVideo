#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
maior = 0

for i in range (0, 7):
    year = int(input(f'{i+1}º Digite o ano de nascimento: '))
    if (ano - year) < 18:
        maior += 1
if maior == 1:
    print(f'{maior} pessoa não atingiu a maioridade.')
else:
    print(f'{maior} pessoas não atingiram a maioridade.')
