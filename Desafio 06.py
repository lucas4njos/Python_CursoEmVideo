#Exercício Python 006: Crie um algoritmo que leia um
# número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
while True:
    num = int(input('Digite um número: '))

    print(f'Dobro = {num * 2}\nTriplo = {num * 3}\nRaiz quadrada: {sqrt(num)}')

    kg = str(input('Deseja continuar? [S] ou [N]: ')).upper().strip()
    if kg[0] == 'N':
        break
