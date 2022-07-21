#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

price = float(input('Digite o valor a ser pago: '))
mode = int(input('1 - À vista dinheiro / cheque\n2 - À vista cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\nDigite: '))
if mode == 1:
    print(f'À vista dinheiro / cheque: 10% de desconto. Valor a ser pago: R$ {price - (price*0.1)}')
elif mode == 2:
    print(f'À vista cartão: 5% de desconto. Valor a ser pago: R$ {price - (price*0.05)}')
elif mode == 3:
    print(f'2x no cartão: preço formal. Valor a ser pago: R$ {price}')
elif mode == 4:
    print(f'3x ou mais no cartão: 20% de juros. Valor a ser pago: R$ {price+(price*0.2)}')

