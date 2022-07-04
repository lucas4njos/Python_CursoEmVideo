#Exercício Python 13: Faça um algoritmo que leia o salário
# de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: '))

print(f'Seu novo salário será correspondente a R$ {salario + (salario * 0.15)}')