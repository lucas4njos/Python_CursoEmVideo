#Exercício Python 23: Faça um programa que leia um número
# de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep

num = int(input('Informe um número: '))
sleep(1)
print('\n\033[34mAnalisando o número...')
sleep(1)
print('\n\033[35mAguarde...\033[m\n')

if num not in range (0, 10000):
    print('Número inválido. Tente novamente.')

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')