#Exercício Python 052: faça um programa que leia
# um número inteiro e diga se ele é ou não um número primo.

while True:
    num = int(input('Digite um número: '))
    primo = 0
    for i in range(1, num+1):
        if num % i == 0:
            primo += 1
    if primo == 2:
        print(f'O número {num} é primo!')
    elif primo != 2:
        print(f'O número {num} NÃO é primo!')
    continuar = int(input('Deseja continuar? \n[1] SIM\n[2] NÃO\nDigite:   '))
    if continuar != 1:
        break