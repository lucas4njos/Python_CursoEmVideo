#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

while True:
    def contador(i, f, p):
        for a in range(1, 11):
            print(a, end=' ')
            sleep(0.4)

        print()

        for a in range(10, -1, -2):
            print(a, end=' ')
            sleep(0.4)

        print()

        for a in range(i, f, p):
            print(a, end=' ')
            sleep(0.4)
    print()

    inicio = int(input("Digite o início:"))
    fim = int(input("Digite o fim:"))
    passo = int(input("Digite o passo:"))

    contador(inicio, fim, passo)