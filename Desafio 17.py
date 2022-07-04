#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hip = sqrt(oposto**2 + adjacente**2)

print(f'A hipotenusa será igual a {hip:.1f}')