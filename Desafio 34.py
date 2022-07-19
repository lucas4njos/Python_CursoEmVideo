# Exercício Python 034: escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário: '))

if salario > 1250:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.15

print(f'O seu novo salário será igual a R$ {salario:.2f}')


