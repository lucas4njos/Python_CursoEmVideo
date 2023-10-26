#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    print(l*c)
l = int(input("Digite a largura: "))
c = int(input("Digite o comprimento: "))

area(l, c)