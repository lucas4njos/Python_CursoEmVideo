# Exercício Python 046: Faça um programa que mostre
# uma contagem regressiva na tela para o estouro
# de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

contagem = 10
for i in range(10, 0, -1):
    print(contagem)
    contagem -= 1
    sleep(1)
print('FELIZ ANO NOVO!')
