#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadas = dict()
maior = 0

for i in range (0, 4):
    jogadas[f'Jogada {i+1}'] = randint(1, 6)
    if jogadas[f'Jogada {i+1}'] > maior:
        maior = jogadas[f'Jogada {i+1}']

ranking = sorted(jogadas.items(), key=itemgetter(1))

print(ranking)

print(maior)