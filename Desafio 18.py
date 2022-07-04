#Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo qualquer: '))

print(f'\nSeno     = {math.sin(math.radians((angulo))):.6f}'
      f'\nCosseno  = {math.cos(math.radians((angulo))):.6f}'
      f'\nTangente = {math.tan(math.radians((angulo))):.6f}')