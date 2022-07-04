#Exercício Python 15: Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('----------------------> Quilômetros percorridos: '))
days = float(input('---> Quantidade de dias que o carro foi alugado: '))

price = (60 * days) + (0.15 * km)

print(f'\n\n\033[34:2mPreço a pagar: R$ {price:.2f}')