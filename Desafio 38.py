# Exercício Python 038: escreva um programa que leia dois números inteiros e compare-os.
# Mostrando uma mensagem na tela:
# — O primeiro valor é maior
# — O segundo valor é maior
# — Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O primeiro número {n1} é maior que o segundo número {n2}.')
elif n2 > n1:
    print(f'O primeiro número {n1} é menor que o segundo número {n2}.')
elif n2 == n1:
    print(f'O primeiro número {n1} é igual ao segundo número {n2}.')