#Exercício Python 12: Faça um algoritmo que leia o
# preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Digite o preço: '))
discount = float(input('Qual será o desconto?: '))

dd = discount/100
pp = (price-(price*dd))

print(f'\n-> Preço anterior: R$ {price:.2f}'
      f'\n-> Desconto solicitado: {discount:.2f} %'
      f'\n\n-> Novo preço: R$ \033[36m{pp:.2f}\033[m'
      f'\nVocê irá economizar R$ {price-pp:.2f}')