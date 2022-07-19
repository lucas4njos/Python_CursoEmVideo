#Exercício Python 036: Escreva um programa para aprovar o
# empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário: R$ '))
anos = int(input('Digite em quantos anos será pago:  ')) * 12

prestacao = valor_da_casa / anos
print(f'\nValor da prestação: R$ {prestacao:.2f}')

if prestacao <= salario * 0.3:
    print('Empréstimo ACEITO!')
else:
    print('Empréstimo NEGADO!')
