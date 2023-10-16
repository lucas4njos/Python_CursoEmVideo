#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = (str(input('Digite um número: ')))

for c in range(0,3):
    for i in range(0,3):
        print(matriz[c][i], end = '   ')
    print('\n')