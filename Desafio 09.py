#Exercício Python 9: Faça um programa que leia um número
# Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número inteiro:'))

i = 1
for i in range (1, 11):
    print(f'{num} * {i} = {num * i}')
    i=+1