#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo
# teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_par = soma_terceira = maior_segunda = 0

for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = (int(input('Digite um número: ')))

for c in range(0,3):
    for i in range(0,3):
        if matriz[c][i] % 2 == 0:
            soma_par += matriz[c][i]
        if c == 2:
            soma_terceira += matriz[c][i]
        if c == 1 and i == 0:
            maior_segunda = matriz[c][i]
        elif c == 1:
            if maior_segunda < matriz[c][i]:
                maior_segunda = matriz[c][i]

print('*-' * 50)

for c in range(0,3):
    for i in range(0,3):
        print(matriz[c][i], end = '   ')
    print('\n')

print('-' * 50)

print(f'A) A soma de todos os valores pares digitados: {soma_par}')
print(f'B) A soma dos valores da terceira coluna: {soma_terceira}')
print(f'C) O maior valor da segunda linha: {maior_segunda}')
