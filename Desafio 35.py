# Exercício Python 035: desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from operator import abs

a = int(input('Insira o valor do primeiro segmento: '))
b = int(input('Insira o valor do segundo segmento: '))
c = int(input('Insira o valor do terceiro segmento: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(b - a) < c < b + a:
    print('Os três segmentos formam um triângulo.')
else:
    print('Os três segmentos não formam um triângulo.')
