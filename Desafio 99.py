#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

m = 0

from time import sleep

while True:
    def maior(lst):
        for i in range(0, len(lst)):
            if i == 0:
                m = lst[i]
            elif lst[i] > m:
                m = lst[i]
        print(f'Lista possui {len(lst)} e o maior número é {m}')

    lista = [0, 1, 2, 3, 258, 5, 4, 789, 1, 0, -45454, 2000]

    maior(lista)
    sleep(2)

