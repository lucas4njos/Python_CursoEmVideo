# Exercício Python 037: Escreva um programa em Python
# que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão: 1
# para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('*-'*20)
opcao = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\nDigite qual conversão você deseja: '))

while opcao not in (1, 2, 3):
    print('*-' * 20)
    print('Opção INVÁLIDA. Tente novamente!')
    print('*-' * 20)
    opcao = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\nDigite qual conversão você deseja: '))


